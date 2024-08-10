# Text-Summarizer-Project

This repository contains an end-to-end text summarization project utilizing a transformer model from HuggingFace. The project includes Docker containerization for easy deployment and is designed to be deployed on AWS infrastructure. A web interface powered by FastAPI enables users to interact with the summarization model, accessible from an AWS EC2 instance.

## Overview

Text summarization is a critical task in natural language processing (NLP) that involves condensing large amounts of text into shorter summaries while preserving the key information. This project aims to provide a solution for text summarization using transformer-based models, leveraging the capabilities offered by HuggingFace's transformers library.

## Features

-	Transformer-based Summarization: Utilizes a state-of-the-art HuggingFace transformer model for text summarization tasks.

-	Docker Containerization: Enables easy deployment and reproducibility of the summarization system using Docker containers.

-	AWS Deployment: Designed for deployment on AWS infrastructure, leveraging EC2 service for hosting the summarization application.

-	Web Interface with FastAPI: Provides a user-friendly web interface powered by FastAPI for interacting with the summarization model.

-	End-to-End Solution: Offers a complete pipeline from data ingestion to model deployment, simplifying the deployment process for users.

## Code Repository structure

1) config/config.yaml:
	It contains all parameters to be defined in the dataclasses inside src/entity.  
	
2) params.yaml:
	It contains parameters for training.

3) main.py:
	It executes the pipeline from data ingestion to model evaluation.

3) app.py:
	It runs the application with FastAPI.

4) template.py
	It creates empty folders and files needed to run the pipeline from main.py.

5) requirements.txt
	It contains all the dependency requirements to run the application.

4) src/
	1) entity:
		It contains all dataclasses for configuring the different components
		An example is DataIngestionConfig, which has attributes:
		- root_dir
		- source_URL
		- local_data_file
		- unzip_dir

	2) config/configuration.py:
		Create class ConfigurationManager, containing the parsed parameters and configurations read from the files params.yaml and config/config.yaml.
	
	3) components:
		- data_ingestion
		- data_validation
		- data_transformation
		- model_trainer	
		- model_evaluation
		
		Each component contains a class reading the entity and performing tasks in a modular fashion.

	4) pipeline:
		- data_ingestion
		- data_validation
		- data_transformation
		- model_trainer
		- model_evaluation
		- prediction

		Each submodule execute the following steps:
			- Import ConfigurationManager class and parse params and config yaml files.
			- Initialize the entity class relative to the pipeline.
			- Initialize the component by passing the entity instance. 
			- Invoke class methods. 

		The prediction submodule is used to make predictions in the script app.py

	5) constants:
		The following constant paths are defined:
			CONFIG_FILE_PATH
			PARAMS_FILE_PATH

	6) logging:
		It defines logger class.
	
	7) utils/common.py:
		It contains utility functions to be used within the codebase.
	

## Run the application

### 1- Create a virtual environment with python3.8

```bash
python3.8 -m venv ~/sandbox/python3.8-TextSummarizer
```

Activate environment:

```bash
. ~/sandbox/python3.8-TextSummarizer/bin/activate
```

### 2- install the requirements

Clone the repository:

```bash
git clone https://github.com/Zarasim/Text-Summarizer-Project.git
cd Text-Summarizer-Project
```

Install requirements inside GitHub repo:

```bash
pip install -r requirements.txt
```

### 4 - Run the application

```bash
python app.py
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Add Policy to IAM user:

	1. AmazonEC2ContainerRegistryFullAccess
	2. AmazonEC2FullAccess

## 2. Create pass key for IAM user

## 3. Create ECR repo to store/save docker image
	Save the URI: 011528284190.dkr.ecr.eu-west-2.amazonaws.com/text-s

## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	#optional

	sudo apt-get update -y

	sudo apt-get upgrade -y
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    Add new self-hosted runner on GitHub and copy commands on EC2 instance.

# 7. Setup GitHub secrets:

    AWS_ACCESS_KEY_ID =

    AWS_SECRET_ACCESS_KEY =

    AWS_REGION = 

    AWS_ECR_LOGIN_URI = 

    ECR_REPOSITORY_NAME = 
