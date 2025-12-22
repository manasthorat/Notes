variable "bucket_name" {
    description = "Name of s3 bucket"
    type = string
}

variable "tags" {
    description = "Tags to apply to the s3 bucket"
    type = map(string)
    default = {}
}