include "root" {
    path = find_in_parent_folders()



}

terraform {
    source = "/Users/manas/notes/Notes/Terragrunt/terraform-modules/s3"

}

inputs = {
    bucket_name = "myapp-dev-bucket-${get_aws_account_id()}"
    tags = {
        Environment = "dev"
        ManagedBy = "Terragrunt"
        Project = "AWS-IAC-BDD"
    }
}