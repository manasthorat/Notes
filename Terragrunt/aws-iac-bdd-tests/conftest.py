import boto3
import pytest

@pytest.fixture
def context():
    """
    Shared storage for BDD steps
    """
    return {}

@pytest.fixture(scope="session")
def aws_session():
    return boto3.Session(profile_name="default", region_name="ap-south-1")

@pytest.fixture(scope="session")
def s3_client(aws_session):
    return aws_session.client("s3")

@pytest.fixture(scope="session")
def iam_client(aws_session):
    return aws_session.client("iam")



