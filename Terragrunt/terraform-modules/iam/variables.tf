variable "role_name" {
  description = "Name of the IAM role"
  type        = string
}

# Input variable for tags
variable "tags" {
  description = "Tags to apply to IAM resources"
  type        = map(string)
  default     = {}
}