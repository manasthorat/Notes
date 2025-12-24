include "root" {
  path = find_in_parent_folders("root.hcl")  # Updated reference
}

terraform {
  source = "terraform-aws-modules/eks/aws"
  version = "~> 20.31"  # Updated to latest stable version compatible with AWS provider 5.x
}

dependency "vpc" {
  config_path = "../vpc"
  
  mock_outputs = {
    vpc_id          = "vpc-12345678"
    private_subnets = ["subnet-12345678", "subnet-87654321"]
  }
}

inputs = {
  cluster_name    = "eks-learning-cluster"
  cluster_version = "1.31"  # Updated to latest stable EKS version
  
  vpc_id     = dependency.vpc.outputs.vpc_id
  subnet_ids = dependency.vpc.outputs.private_subnets
  
  # Control plane logging (optional but useful for learning)
  cluster_enabled_log_types = ["api", "audit", "authenticator"]
  
  cluster_endpoint_public_access = true
  
  # Enable IRSA (IAM Roles for Service Accounts)
  enable_irsa = true
  
  # Cluster access configuration
  enable_cluster_creator_admin_permissions = true
  
  eks_managed_node_groups = {
    default = {
      name = "eks-learning-nodes"
      
      instance_types = ["t3.medium"]
      
      min_size     = 2
      max_size     = 3
      desired_size = 2
      
      disk_size = 20
      
      # Labels to help identify nodes
      labels = {
        Environment = "learning"
        NodeGroup   = "default"
      }
      
      # Tags for the node group
      tags = {
        Name = "eks-learning-node"
      }
    }
  }
  
  tags = {
    Name = "eks-learning-cluster"
  }
}


