# Minimal placeholder Terraform files. Customize before use.
terraform {
  required_version = ">= 1.0"
}

provider "aws" {
  region = "us-east-1"
}

# Resources to create:
# - aws_s3_bucket
# - aws_iam_role + policy for EC2 to access S3
# - aws_launch_template or aws_launch_configuration
# - aws_autoscaling_group
# - aws_lb (ALB) + target group
