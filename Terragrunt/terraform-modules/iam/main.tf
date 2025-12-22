resource "aws_iam_role" "main" {
  name = var.role_name
  
  # Trust policy: This role can be assumed by EC2 instances

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
  
  tags = var.tags
}


resource "aws_iam_role" "main" {
    name = "${var.role_name}--policy"
    description= "Policy for ${var.role_name} with S3 read and CloudWatch logs write"

    policy = jsonencode({
        version = "2012-10-17"
        Statement = [ 
            {
                Effect = "Allow"
                Action = [ 
                    "s3:GetObject",
                    "s3.ListBucket",
                    "s3.GetBucketLocation"

                ]
                resource = [
                    "arn:aws:s3:::*",
                    "arn:aws:s3:::*/*"
                ]
            },
                Effect = "Allow"
                Action = [
                    "logs:CreateLogGroup",    
                    "logs:CreateLogStream",  
                    "logs:PutLogEvents" 
                ]
                resource = "arn:aws:logs:*:*:*"
        ]
    })


}


resource "aws_iam_role_policy_attachment" "main" {
    role = aws_iam_role.main.name
    policy_arn = aws_iam_policy.main.arn
}

