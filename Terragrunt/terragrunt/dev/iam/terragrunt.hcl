include "root" {
    path = find_in_parent_folders("root.hcl")
}

terraform {
    source = "/Users/manas/notes/Notes/Terragrunt/terraform-modules/iam"

}

inputs = {
    role_name = "myapp-dev-role"
    tags = {
        Environment = "dev"
        ManagedBy = "Terragrunt"
        Project = "AWS-IAC-BDD"
    }
}