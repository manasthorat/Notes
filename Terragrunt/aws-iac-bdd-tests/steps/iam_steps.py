from pytest_bdd import given, when, then, parsers ,scenarios
import botocore.exceptions
import json


scenarios('../features/iam.feature')
@given(parsers.parse('an IAM role named "{role_name}"'))
def iam_role_name(context, role_name):
    context["role_name"] = role_name


@when("I fetch the IAM role")
def fetch_iam_role(context, iam_client):
    try:
        response = iam_client.get_role(RoleName=context["role_name"])
        context["role"] = response["Role"]
        context["role_exists"] = True
    except botocore.exceptions.ClientError:
        context["role_exists"] = False


@then("the IAM role should exist")
def iam_role_should_exist(context):
    assert context["role_exists"] is True


@when("I fetch the IAM role trust policy")
def fetch_trust_policy(context):
    policy = context["role"]["AssumeRolePolicyDocument"]
    context["trust_policy"] = policy


@then(parsers.parse('the trust policy should allow "{service}"'))
def validate_trust_policy(context, service):
    statements = context["trust_policy"]["Statement"]
    principals = [
        stmt["Principal"]["Service"]
        for stmt in statements
        if "Service" in stmt.get("Principal", {})
    ]
    assert service in principals
