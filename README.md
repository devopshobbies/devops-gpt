# DevOps-GPT
Use a brilliant assistant as your friend in your DevOps journey.

## What does this project offer?
This project helps you to balance your daily work as a DevOps engineer, from simple bug fixes to project template generation.<br />
you don't need to search on Google for some routine jobs and it helps you with a robust prompt to simplify your career.

## How it works?
This is a wrapper between DevOps engineers and large language models like GPT-4-mini. The main strength of it is prompt engineering.<br />

We have developed some (Extendable) prompt-driven solutions with a simplified interface for the DevOps process cost reduction.<br />

### Docker services
We run our services using docker-compose (the main Fast-API-based backend and MongoDB), so we package all dependencies and don't use any external service.<br />
The second one is Mongodb. we need to save the prompt and GPT-4_mini response in the Mongo document for future use. (for example, fine-tuning the other model with our data) <br />

### Media directory
The third one is in the media directory. for now, We save a project called (MyTerraform) which is a Terraform template generated based on user requirements. so users can download it and use it.<be />
surely we can save any static data in the `/media`.

![teramedia](https://github.com/user-attachments/assets/b8e10d83-68ac-4efc-b064-45f1d1a870dc)

This is an example of a template generated in the `/media`

and the input is something like that


![Uploading Screenshot from 2024-10-27 10-56-54.png…]()


### directory_generator.py
This file becomes updated when we trigger the template generation API. finally, It generates the MyTerraform directory based on user input which is a template.


## ToolChain
1. Python
2. Docker
3. GPT-4-mini
4. FastAPI

## Pre-requisites
1. Python
2. Docker

## How to use?
execute `sh run.sh` in your terminal

> [!WARNING]  
> Do Not change the GPT model! Prompts have been developed for the GPT-4-mini model and they can't be integrated with other GPT models. it can cause horrible incompatibility.


> 
# Maintenance
** [Abolfazl Andalib](https://github.com/abolfazl8131) - abolfazlandalib@gmail.com **
