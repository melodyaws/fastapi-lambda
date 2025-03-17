# FastAPI on AWS Lambda with SAM

A project template for deploying FastAPI applications to AWS Lambda using the AWS Serverless Application Model (SAM) framework, providing a complete solution for building serverless APIs.

## Features

- High-performance REST API built with FastAPI
- Seamless integration with AWS Lambda using the Mangum adapter
- Container-based Lambda deployment using Docker
- Automatic API documentation generation
- Simplified deployment and infrastructure management with AWS SAM
- Support for local development and testing

## Prerequisites

Before getting started, ensure you have the following tools installed:

- [Python 3.11](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- AWS account with configured credentials

## Project Structure

```
fastapi-lambda
├── .aws-sam/                  # SAM build folder (auto-generated)
├── .venv/                     # Virtual environment directory
├── app/                       # Application code directory
│   ├── __init__.py
│   └── main.py                # FastAPI main application
├── docs/                      # Documentation files
│   ├── infra.dot
│   └── infra.svg
├── Dockerfile                 # Docker container configuration
├── README.md                  # This document
├── requirements.txt           # Python dependencies
├── samconfig.toml             # SAM configuration file
└── template.yaml              # SAM template file
```

## Part 1: Deployment to AWS

### 1. Install Dependencies and Build the Project

After cloning the repository:

```bash
# Navigate to project directory (if not already there)
cd fastapi-lambda

# Build the project
sam build
```

### 2. Create ECR Repository

Before deploying, you need to create an ECR repository to store your container image:

```bash
aws ecr create-repository --repository-name fastapi-lambda --region us-east-1
```

Take note of the repository URI in the output (it will look like: `account-id.dkr.ecr.us-east-1.amazonaws.com/fastapi-lambda`).

### 3. Deploy to AWS

```bash
sam deploy --image-repository account-id.dkr.ecr.us-east-1.amazonaws.com/fastapi-lambda
```

### 4. Verify Deployment

After deployment completes, you can view the deployed resources and API Gateway URL:

```bash
aws cloudformation describe-stacks --stack-name fastapi-lambda --query "Stacks[0].Outputs"
```

Look for the `ApiGatewayEndpoint` value in the output - this is the URL of your deployed API.


This README provides a comprehensive guide to get started with your FastAPI on AWS Lambda project. Customize it to match your specific project requirements and preferences.