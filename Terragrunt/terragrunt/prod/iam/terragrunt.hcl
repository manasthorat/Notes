include "root" {
    path = find_in_parent_folders("root.hcl")
}

terraform {
    source = "/Users/manas/notes/Notes/Terragrunt/terraform-modules/s3""

}

input = {
    role_name = "myapp-prod-role"
    tags = {
        Environment = "prod"
        ManagedBy = "Terragrunt"
        Project = "AWS-IAC-BDD"
    }
}