Feature: S3 Replication using Iam Roles
    as a cloud engineer
    I want to upload to the source bucke
    Replicate files
    Check replica bucket

    Scenario: Upload object using replication role and validate via access point

        Given I have assumed the replication role
        When I upload a file to the source bucket
        Then the file should be accessible from the replica bucket using access point

