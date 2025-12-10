# Auto-Scaling Web Application with S3 Data Storage (AWS Project)

## Overview
This project demonstrates an auto-scaling web application on AWS that allows users to upload files to Amazon S3. The infrastructure automatically scales based on traffic, providing high availability and fault tolerance.

## Features
- Flask web app that uploads files to S3
- EC2 user-data script for automatic bootstrapping
- Placeholder Terraform configuration for infrastructure-as-code
- Simple Auto Scaling recommendations (CloudWatch + ASG + ALB)

## Local development (quick)
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables and run:
   ```bash
   export S3_BUCKET=your-s3-bucket-name
   export AWS_ACCESS_KEY_ID=...
   export AWS_SECRET_ACCESS_KEY=...
   export AWS_DEFAULT_REGION=us-east-1
   python app.py
   ```
4. Open http://localhost (or port 80) to use the app.

## Recommended AWS Deployment Steps (short)
- Create S3 bucket
- Create an IAM role with a policy allowing PutObject/GetObject to the bucket, and attach to EC2
- Create a Launch Template or Launch Configuration that pulls this repo on boot (user-data) and runs app
- Create an Auto Scaling Group with the Launch Template and attach to an Application Load Balancer
- Create CloudWatch Alarms to scale out/in based on CPU or RequestCount

## Repository structure
```
auto-scaling-webapp-s3/
├─ app/
│  ├─ app.py
│  └─ templates/index.html
├─ scripts/
│  └─ user-data.sh
├─ terraform/
│  └─ main.tf
├─ requirements.txt
└─ README.md
```

## Next steps I can help with
- Add a production-ready systemd unit or Supervisor config
- Provide a full Terraform implementation (security groups, ALB, ASG, IAM)
- Dockerize the app and provide ECS/Fargate or EKS deployment
- Create GitHub Actions workflow to auto-deploy
