from pytest_bdd import given, when, then, parsers ,scenarios
import botocore.exceptions

scenarios('../features/s3.feature')
@given(parsers.parse('an S3 bucket named "{bucket_name}"'))
def s3_bucket_name(context, bucket_name):
    context['bucket_name'] = bucket_name


@when('I check the S3 bucket')
def check_s3_bucket_exists(context, s3_client):
    try:
        s3_client.head_bucket(Bucket=context['bucket_name'])
        context['bucket_exists'] = True
    except botocore.exceptions.ClientError as e:
        context['bucket_exists'] = False


@then('the S3 bucket should exist')
def verify_bucket_exists(context):
    assert context['bucket_exists'] == True



@when("I fetch the bucket tags")
def fetch_bucket_tags(context, s3_client): 
    response = s3_client.get_bucket_tagging(
        Bucket=context["bucket_name"]
    )
    context["bucket_tags"] = {
        tag["Key"]: tag["Value"]
        for tag in response["TagSet"]
    }

@then(parsers.parse('the bucket should have tag "{tag_key}" with value "{tag_value}"'))
def verify_bucket_tag(context, tag_key, tag_value):
    assert context["bucket_tags"].get(tag_key) == tag_value

