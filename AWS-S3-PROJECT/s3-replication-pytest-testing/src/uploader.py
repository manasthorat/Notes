import boto3
from datetime import datetime
from config import REGION, BUCKET_1_NAME


def upload_object(credentials):
    s3_client = boto3.client(
        's3',
        region_name=REGION,
        **credentials)
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    key= f"uploader-uploads/file-{timestamp}.txt"
    body= f"This is a test file uploaded at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    response = s3_client.put_object(
        Bucket=BUCKET_1_NAME,
        Key=key,
        Body=body,
        ContentType='text/plain',
        ServerSideEncryption='aws:kms'  # Use KMS encryption

    )

    print(f"File uploaded successfully. Key: {key}, ETag: {response['ETag']}")
    return key