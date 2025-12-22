include "root" {
    path = find_in_parent_folders()
}

terraform {
    source = "/Users/manas/notes/Notes/Terragrunt/terraform-modules/s3"

}

inputs = {
    role_name = "myapp-dev-role"
    tags = {
        Environment = "dev"
        ManagedBy = "Terragrunt"
        Project = "AWS-IAC-BDD"
    }
}