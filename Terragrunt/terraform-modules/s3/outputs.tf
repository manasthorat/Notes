output "bucket_name" {
    description = "The name of s3 bucket"
    value = aws_s3_bucket.main.id
}


output "bucket_arn" {
    description = " Arn of s3 bucket"
    value = aws_s3_bucket.main.arn
}