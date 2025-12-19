import boto3
from config import REGION

def assume_role(profile, role_arn , session_name):

    print("Step1 - Creating STS Client")

    session = boto3.Session(profile_name=profile)
    sts= session.client('sts', region_name=REGION)

    response = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name,
        DurationSeconds=3600
    )
    creds = response["Credentials"]
    return {
        'aws_access_key_id': creds['AccessKeyId'],
        'aws_secret_access_key': creds['SecretAccessKey'],
        'aws_session_token': creds['SessionToken']
    }

    