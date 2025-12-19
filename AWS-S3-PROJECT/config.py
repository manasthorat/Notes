# AWS Configuration
ACCOUNT_ID = "708037417421"  # Your account ID
REGION = "ap-south-1"  # Your region
BUCKET_1_NAME = "manaskawstestbucket1"  # Your Bucket-1 name
ROLE_1_ARN = f"arn:aws:iam::708037417421:role/S3-Application-Role"
ROLE_2_ARN = f"arn:aws:iam::708037417421:role/S3-Replication-Role"

# Display config (for verification)
if __name__ == "__main__":
    print("AWS Configuration:")
    print(f"  Account ID: {ACCOUNT_ID}")
    print(f"  Region: {REGION}")
    print(f"  Bucket 1: {BUCKET_1_NAME}")
    print(f"  Role 1 ARN: {ROLE_1_ARN}")
    print(f" Role 2 ARN: {ROLE_2_ARN} ")