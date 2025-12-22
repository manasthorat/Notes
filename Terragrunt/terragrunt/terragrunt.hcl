#root terragrunt configuration

generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<EOF
terraform {
  required_version = ">= 1.5"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}
EOF
}


remote_state {
    backend = "s3"
    config = {
        bucket = "manas-terraform-state-9001002"
        key = "${path_relative_to_include()}/terraform.tfstate"
        region = "ap-south-1"
        dynamodb_table = "terraform-locks"
        encrypt = true
    }

    generate = {
        path = "backend.tf"
        if_exists = "overwrite_terragrunt"
    }
}