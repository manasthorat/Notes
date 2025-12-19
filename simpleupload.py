#!/usr/bin/env python3
"""
Simple S3 Upload Script using IAM Role
This script demonstrates how to:
1. Assume an IAM role
2. Get temporary credentials
3. Upload a file to S3
"""

import boto3
from datetime import datetime
from config import ACCOUNT_ID, REGION, BUCKET_1_NAME, ROLE_1_ARN

def assume_role():
    """
    Assume Role 1 and get temporary credentials
    Returns: Dictionary with temporary credentials
    """
    print("=" * 60)
    print("STEP 1: Assuming IAM Role")
    print("=" * 60)
    
    # Create STS client (Security Token Service)
    session = boto3.Session(profile_name='s3-developer')
    sts_client = session.client('sts', region_name=REGION)
    
    print(f"🔐 Attempting to assume role:")
    print(f"   Role ARN: {ROLE_1_ARN}")
    
    try:
        # Call AssumeRole
        response = sts_client.assume_role(
            RoleArn=ROLE_1_ARN,
            RoleSessionName='MyUploadSession',  # Can be any name
            DurationSeconds=3600  # Credentials valid for 1 hour
        )
        
        print("✅ Successfully assumed role!")
        print(f"   Session name: MyUploadSession")
        print(f"   Valid for: 1 hour")
        
        # Extract credentials from response
        credentials = response['Credentials']
        
        return {
            'access_key': credentials['AccessKeyId'],
            'secret_key': credentials['SecretAccessKey'],
            'session_token': credentials['SessionToken']
        }
        
    except Exception as e:
        print(f"❌ Failed to assume role!")
        print(f"   Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Check if Role 1 trust policy allows your user")
        print("2. Verify your AWS credentials: aws sts get-caller-identity")
        print("3. Ensure Role ARN is correct")
        return None


def upload_to_s3(credentials):
    """
    Upload a test file to S3 using temporary credentials
    """
    print("\n" + "=" * 60)
    print("STEP 2: Creating S3 Client with Temp Credentials")
    print("=" * 60)
    
    # Create S3 client with temporary credentials
    s3_client = boto3.client(
        's3',
        region_name=REGION,
        aws_access_key_id=credentials['access_key'],
        aws_secret_access_key=credentials['secret_key'],
        aws_session_token=credentials['session_token']
    )
    
    print("✅ S3 client created successfully")
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_key = f"uploads/test-file-{timestamp}.txt"
    
    # Create file content
    file_content = f"""
Hello from boto3!
===================
Upload Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Bucket: {BUCKET_1_NAME}
File: {file_key}

This file was uploaded using IAM Role 1 with temporary credentials.
It should automatically replicate to Bucket 2.
"""
    
    print("\n" + "=" * 60)
    print("STEP 3: Uploading File to S3")
    print("=" * 60)
    print(f"📤 Uploading to:")
    print(f"   Bucket: {BUCKET_1_NAME}")
    print(f"   Key: {file_key}")
    print(f"   Content length: {len(file_content)} bytes")
    
    try:
        # Upload file to S3
        response = s3_client.put_object(
            Bucket=BUCKET_1_NAME,
            Key=file_key,
            Body=file_content,
            ServerSideEncryption='aws:kms',  # Use KMS encryption
            ContentType='text/plain'
        )
        
        print("✅ Upload successful!")
        print(f"   ETag: {response['ETag']}")
        print(f"   Server-side encryption: {response.get('ServerSideEncryption', 'N/A')}")
        
        # Verify upload by reading the file back
        print("\n" + "=" * 60)
        print("STEP 4: Verifying Upload")
        print("=" * 60)
        
        verify_response = s3_client.get_object(
            Bucket=BUCKET_1_NAME,
            Key=file_key
        )
        
        retrieved_content = verify_response['Body'].read().decode('utf-8')
        print("✅ Verification successful!")
        print(f"   Retrieved {len(retrieved_content)} bytes")
        print(f"   Content matches: {retrieved_content == file_content}")
        
        return file_key
        
    except Exception as e:
        print(f"❌ Upload failed!")
        print(f"   Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Check if Role 1 has s3:PutObject permission")
        print("2. Verify bucket name is correct")
        print("3. Check KMS key permissions")
        return None


def main():
    """
    Main function
    """
    print("\n" + "=" * 60)
    print("AWS S3 UPLOAD USING IAM ROLE")
    print("=" * 60)
    print(f"Target: {BUCKET_1_NAME}")
    print(f"Region: {REGION}")
    
    # Step 1: Assume Role
    credentials = assume_role()
    
    if credentials is None:
        print("\n❌ Script failed: Could not assume role")
        return
    
    # Step 2 & 3: Upload to S3
    uploaded_key = upload_to_s3(credentials)
    
    if uploaded_key:
        print("\n" + "=" * 60)
        print("SUCCESS! 🎉")
        print("=" * 60)
        print(f"File uploaded: {uploaded_key}")
        print(f"\nNext steps:")
        print(f"1. Check AWS Console → S3 → {BUCKET_1_NAME}")
        print(f"2. Wait 2-5 minutes for replication")
        print(f"3. Check Bucket 2 for replicated file")
        print(f"\nSave this file key for verification:")
        print(f"   {uploaded_key}")
    else:
        print("\n❌ Script failed: Upload unsuccessful")


if __name__ == "__main__":
    main()