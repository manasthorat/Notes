Feature: Validate S3 bucket created by Terragrunt

  Scenario: S3 bucket exists
    Given an S3 bucket named "myapp-dev-bucket-708037417421"
    When I check the S3 bucket
    Then the S3 bucket should exist

  Scenario: S3 bucket has correct tags
    Given an S3 bucket named "myapp-dev-bucket-708037417421"
    When I fetch the bucket tags
    Then the bucket should have tag "Environment" with value "dev"
