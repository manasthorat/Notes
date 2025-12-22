output "role_name" {
  description = "Name of the IAM role"
  value       = aws_iam_role.main.name
}

# Output the role ARN
# ARN is needed when assigning this role to EC2 instances or other services
output "role_arn" {
  description = "ARN of the IAM role"
  value       = aws_iam_role.main.arn
}

# Output the policy ARN
output "policy_arn" {
  description = "ARN of the IAM policy"
  value       = aws_iam_policy.main.arn
}