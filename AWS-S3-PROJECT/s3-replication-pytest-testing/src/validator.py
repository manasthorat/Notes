import boto3
from config import REGION, Replica_access_point_arn

def read_from_replica(credentials, key):
    s3 = boto3.client(
        's3',
        region_name=REGION,
        **credentials
    )

    response = s3.get_object(
        Bucket=Replica_access_point_arn,
        Key=key
    )

    return response['Body'].read().decode()
