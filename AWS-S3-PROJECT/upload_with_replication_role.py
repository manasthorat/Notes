import boto3
from datetime import datetime
from config import ACCOUNT_ID,ROLE_2_ARN,BUCKET_1_NAME,REGION,ROLE_1_ARN

def assume_replication_role():
    print("Step1 - Creating STS Client")
    session = boto3.Session(profile_name="s3-developer")

    sts_client = session.client('sts', region_name=REGION)
    print("\n" + "="*70)
    print("STEP 2: CHECKING CURRENT IDENTITY")
    print("="*70)

    try:
        identity=sts_client.get_caller_identity()
        print(identity)

    except Exception as e:
        print("could not get identity :{e}")
        return None
    

    print("="*70)
    print("Step 3 - calling assuming role api")
    try:
        response=sts_client.assume_role(RoleArn=ROLE_2_ARN,RoleSessionName="ReplicationSession",
                                        DurationSeconds=3000)
        print("\n" + "="*70)
        print("STEP 4: EXAMINING THE RESPONSE")
        print("="*70)
        
        # EXPLANATION: Understanding the response structure
        print("The API returned a response object (Python dictionary)")
        print(f"  • Response type: {type(response)}")
        print(f"  • Response keys: {list(response.keys())}")


        credentials = response["Credentials"]
        assumed_role = response["AssumedRoleUser"]
        creds = {
            'access_key': credentials['AccessKeyId'],
            'secret_key': credentials['SecretAccessKey'],
            'session_token': credentials['SessionToken'],
            'expiration': credentials['Expiration']
        }

        return creds
    
    except Exception as e:
        print(f"Error : {e}")
        print("Failed to assume the role")



def assume_application_role(replication_creds, app_role_arn ):
    print("\nASSUMING APPLICATION ROLE")
    sts_client = boto3.client(
        "sts",
        region_name=REGION,
        aws_access_key_id=replication_creds["access_key"],
        aws_secret_access_key=replication_creds["secret_key"],
        aws_session_token=replication_creds["session_token"],
    )

    response = sts_client.assume_role(
        RoleArn=app_role_arn,
        RoleSessionName="ApplicationSession",
        DurationSeconds=3000
    )

    credentials = response["Credentials"]
    return {
        "access_key": credentials["AccessKeyId"],
        "secret_key": credentials["SecretAccessKey"],
        "session_token": credentials["SessionToken"],
        "expiration": credentials["Expiration"],
    }

def upload_with_tmp_credentials(credentials):
    print("\n" + "="*70)
    print("STEP: CREATING S3 CLIENT WITH TEMP CREDENTIALS")
    print("="*70)


    s3_client = boto3.client(
        "s3",
        region_name=REGION,
        aws_access_key_id=credentials['access_key'],
        aws_secret_access_key=credentials['secret_key'],
        aws_session_token=credentials['session_token']
    )

    print("S3 CLIIENT CREATED")
        # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_key = f"replication-role-uploads/test-{timestamp}.txt"
    
    # Create file content
    file_content = f"""
Upload Test via Replication Role
==================================
Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Role Used: S3-Replication-Role (Role 2)
Bucket: {BUCKET_1_NAME}
File Key: {file_key}

This file was uploaded using temporary credentials
obtained by assuming the Replication Role.

Credentials expire at: {credentials['expiration']}
"""
    
    try:
        response= s3_client.put_object(
            Bucket=BUCKET_1_NAME,
            Key=file_key,
            Body=file_content,
            ContentType='text/plain',
            ServerSideEncryption='aws:kms',
            Metadata={
                'uploaded-by': 'replication-role-script',
                'role': 'S3-Replication-Role'
            }
        )
        # EXPLANATION: Understanding S3 response
        print("S3 returned response:")
        print(f"  • ETag: {response.get('ETag', 'N/A')}")
        print(f"  • Encryption: {response.get('ServerSideEncryption', 'N/A')}")
        print(f"  • Version ID: {response.get('VersionId', 'N/A')}")
        
        print("FILE UPLOADED SUCCESFULLY")


    


        print("CHECKING IF FILE IS UPLOADED CORRECLTY")

        get_response = s3_client.get_object(
            Bucket=BUCKET_1_NAME,
            Key=file_key
        )

        retrieved_content = get_response['Body'].read().decode('utf-8')
        content_matches = (retrieved_content == file_content)

        print("Verification completed - File Matches")

        if get_response.get('Metadata'):
            print(f"    - Custom metadata: {get_response['Metadata']}")
            return file_key
    
    
    except Exception as e:
        print(f"Error: {e}")
        print("ERROR UPLOADING FILE")
        return None
    

def main():
    print("\n" + "="*70)
    print("AWS S3 UPLOAD USING REPLICATION ROLE")


    repl_credentials=assume_replication_role()

    if repl_credentials is None:
        print("\nfailed to assue role")
        return
    
    app_credentials = assume_application_role(repl_credentials,ROLE_1_ARN)
    file_key = upload_with_tmp_credentials(app_credentials)
    if file_key is None:
        print("\n❌ Failed to upload file. Exiting.")
        return
    
if __name__ == "__main__":
    
    main()

