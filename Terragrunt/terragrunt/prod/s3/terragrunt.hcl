include "root" {
    path = find_in_parent_folders("root.hcl")



}

terraform {
    source = "/Users/manas/notes/Notes/Terragrunt/terraform-modules/s3""

}

inputs = {
    bucket_name = "myapp-prod-bucket-${get_aws_account_id()}"
    tags = {
        Environment = "prod"
        ManagedBy = "Terragrunt"
        Project = "AWS-IAC-BDD"
    }
}