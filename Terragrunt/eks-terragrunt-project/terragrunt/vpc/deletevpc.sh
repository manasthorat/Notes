#!/bin/bash

# Configuration
REGION="us-west-2"
VPC_NAME="eks-learning-vpc"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Finding VPC...${NC}"
VPC_ID=$(aws ec2 describe-vpcs \
  --filters "Name=tag:Name,Values=$VPC_NAME" \
  --query "Vpcs[0].VpcId" \
  --output text \
  --region $REGION)

if [ "$VPC_ID" == "None" ] || [ -z "$VPC_ID" ]; then
  echo -e "${RED}VPC not found!${NC}"
  exit 1
fi

echo -e "${GREEN}Found VPC: $VPC_ID${NC}"
echo -e "${YELLOW}This will delete ALL resources in this VPC!${NC}"
read -p "Are you sure? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
  echo "Aborted."
  exit 0
fi

# Function to retry commands
retry_delete() {
  local cmd=$1
  local max_attempts=3
  local attempt=1
  
  while [ $attempt -le $max_attempts ]; do
    if eval $cmd 2>/dev/null; then
      return 0
    fi
    echo "Retry $attempt/$max_attempts..."
    sleep 5
    ((attempt++))
  done
  return 1
}

# 1. NAT Gateways
echo -e "\n${YELLOW}Step 1: Deleting NAT Gateways...${NC}"
NAT_GW_IDS=$(aws ec2 describe-nat-gateways \
  --filter "Name=vpc-id,Values=$VPC_ID" "Name=state,Values=available" \
  --query "NatGateways[*].NatGatewayId" \
  --output text --region $REGION)

for NAT_ID in $NAT_GW_IDS; do
  echo "Deleting: $NAT_ID"
  aws ec2 delete-nat-gateway --nat-gateway-id $NAT_ID --region $REGION
done

if [ ! -z "$NAT_GW_IDS" ]; then
  echo "Waiting for NAT Gateways to delete (3 minutes)..."
  sleep 180
fi

# 2. Elastic IPs
echo -e "\n${YELLOW}Step 2: Releasing Elastic IPs...${NC}"
EIP_ALLOC_IDS=$(aws ec2 describe-addresses \
  --filters "Name=domain,Values=vpc" \
  --query "Addresses[?Tags[?Key=='Name' && contains(Value, '$VPC_NAME')]].AllocationId" \
  --output text --region $REGION)

for ALLOC_ID in $EIP_ALLOC_IDS; do
  echo "Releasing: $ALLOC_ID"
  retry_delete "aws ec2 release-address --allocation-id $ALLOC_ID --region $REGION"
done

# 3. Network Interfaces
echo -e "\n${YELLOW}Step 3: Deleting Network Interfaces...${NC}"
ENI_IDS=$(aws ec2 describe-network-interfaces \
  --filters "Name=vpc-id,Values=$VPC_ID" \
  --query "NetworkInterfaces[*].NetworkInterfaceId" \
  --output text --region $REGION)

for ENI_ID in $ENI_IDS; do
  echo "Deleting: $ENI_ID"
  retry_delete "aws ec2 delete-network-interface --network-interface-id $ENI_ID --region $REGION"
done

# 4. Security Groups
echo -e "\n${YELLOW}Step 4: Deleting Security Groups...${NC}"
SG_IDS=$(aws ec2 describe-security-groups \
  --filters "Name=vpc-id,Values=$VPC_ID" \
  --query "SecurityGroups[?GroupName!='default'].GroupId" \
  --output text --region $REGION)

for SG_ID in $SG_IDS; do
  echo "Deleting: $SG_ID"
  retry_delete "aws ec2 delete-security-group --group-id $SG_ID --region $REGION"
done

# 5. Route Tables
echo -e "\n${YELLOW}Step 5: Deleting Route Tables...${NC}"
RT_IDS=$(aws ec2 describe-route-tables \
  --filters "Name=vpc-id,Values=$VPC_ID" \
  --query "RouteTables[?Associations[0].Main != \`true\`].RouteTableId" \
  --output text --region $REGION)

for RT_ID in $RT_IDS; do
  ASSOC_IDS=$(aws ec2 describe-route-tables \
    --route-table-ids $RT_ID \
    --query "RouteTables[*].Associations[?Main != \`true\`].RouteTableAssociationId" \
    --output text --region $REGION)
  
  for ASSOC_ID in $ASSOC_IDS; do
    echo "Disassociating: $ASSOC_ID"
    aws ec2 disassociate-route-table --association-id $ASSOC_ID --region $REGION 2>/dev/null || true
  done
  
  echo "Deleting: $RT_ID"
  retry_delete "aws ec2 delete-route-table --route-table-id $RT_ID --region $REGION"
done

# 6. Internet Gateways
echo -e "\n${YELLOW}Step 6: Deleting Internet Gateways...${NC}"
IGW_IDS=$(aws ec2 describe-internet-gateways \
  --filters "Name=attachment.vpc-id,Values=$VPC_ID" \
  --query "InternetGateways[*].InternetGatewayId" \
  --output text --region $REGION)

for IGW_ID in $IGW_IDS; do
  echo "Detaching: $IGW_ID"
  aws ec2 detach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID --region $REGION
  echo "Deleting: $IGW_ID"
  aws ec2 delete-internet-gateway --internet-gateway-id $IGW_ID --region $REGION
done

# 7. Subnets
echo -e "\n${YELLOW}Step 7: Deleting Subnets...${NC}"
SUBNET_IDS=$(aws ec2 describe-subnets \
  --filters "Name=vpc-id,Values=$VPC_ID" \
  --query "Subnets[*].SubnetId" \
  --output text --region $REGION)

for SUBNET_ID in $SUBNET_IDS; do
  echo "Deleting: $SUBNET_ID"
  retry_delete "aws ec2 delete-subnet --subnet-id $SUBNET_ID --region $REGION"
done

# 8. VPC
echo -e "\n${YELLOW}Step 8: Deleting VPC...${NC}"
aws ec2 delete-vpc --vpc-id $VPC_ID --region $REGION

echo -e "\n${GREEN}✓ VPC deletion complete!${NC}"