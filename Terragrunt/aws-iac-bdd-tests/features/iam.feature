Feature: Validate IAM role created by Terragrunt

  Scenario: IAM role exists
    Given an IAM role named "myapp-dev-role"
    When I fetch the IAM role
    Then the IAM role should exist

  Scenario: IAM role trust policy allows EC2
    Given an IAM role named "myapp-dev-role"
    When I fetch the IAM role
    And I fetch the IAM role trust policy
    Then the trust policy should allow "ec2.amazonaws.com"
