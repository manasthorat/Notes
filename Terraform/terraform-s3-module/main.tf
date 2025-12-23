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
  region = var.aws_region
}


module "s3_buckets" {
  source = "./modules/s3"

  for_each = toset(var.s3_buckets)

  bucket_name = each.value

  tags = {
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}

