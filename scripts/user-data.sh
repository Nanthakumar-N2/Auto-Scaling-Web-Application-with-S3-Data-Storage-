#!/bin/bash
set -e
# Basic setup for Amazon Linux / Amazon Linux 2
yum update -y
yum install -y python3 git
pip3 install --upgrade pip
pip3 install -r /home/ec2-user/auto-scaling-webapp-s3/requirements.txt

# Export S3_BUCKET via instance profile ideally; fallback example:
# export S3_BUCKET=your-s3-bucket-name

# Run app (use a process manager in production)
cd /home/ec2-user/auto-scaling-webapp-s3/app || exit 0
nohup python3 app.py > app.log 2>&1 &
