from pytest_bdd import scenarios, given, when, then

from src.uploader import upload_object
from src.validator import read_from_replica
from config import ROLE_1_ARN, ROLE_2_ARN , ROLE_3_ARN
from src.roles import assume_role
scenarios('../features/s3_replication.feature')


@given('I have assumed the replication role')
def assume_replication_role(context):
    context['replication_credentials'] = assume_role("s3-developer", ROLE_1_ARN , "ReplicationSession")
    assert context['replication_credentials'] is not None, "Failed to assume replication role"


@when('I upload a file to the source bucket')
def upload_file(context):
    key = upload_object(context['replication_credentials'])
    context['uploaded_key'] = key


@then('the file should be accessible from the replica bucket ussing access point')
def validate_replica(context):
    content = read_from_replica(context['replication_credentials'], context['uploaded_key'])
    assert "This is a test file" in content

