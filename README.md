# DevOps-GPT

Use a brilliant assistant as your friend in your DevOps Journey.

## What does this project offer?

This project helps you to balance your daily work as a DevOps engineer, from simple bug fixes to project template generation.
You don't need to search on Google for some routine jobs, and it helps you with a robust prompt to simplify your career.

## How it works?

This is a wrapper between DevOps engineers and large language models like GPT-4-mini. The main strength of it is prompt engineering.

We have developed some (extendable) prompt-driven solutions with a simplified interface for the DevOps process cost reduction.

### Docker services

We run our services using docker-compose (the main Fast-API-based backend and MongoDB), so we package all dependencies and don't use any external service.
The second one is MongoDB. We need to save the prompt and GPT-4-mini response in the Mongo document for future use (e.g., fine-tuning another model with our data).

### Media directory

The third one is the media directory. For now, we save a project called (MyTerraform), which is a Terraform template generated based on user requirements, so users can download it and use it.
Surely we can save any static data in the `/media`.

This is an example of a template generated in the `/media`

The input is something like this:

### directory_generators

This directory gets updated when we trigger the template generation API. Finally, it generates the MyTerraform directory based on user input, which is a template.

## ToolChain

1. Python
2. Docker
3. GPT-4-mini
4. FastAPI
5. Helm

## Pre-requisites

1. Python
2. Docker

## How to use?

Execute `sh run.sh` in your terminal

> [!WARNING]\
> Do Not change the GPT model! Prompts have been developed for the GPT-4-mini model, and they can't be integrated with other GPT models. It can cause horrible incompatibility.

## Run it locally on Kubernetes

If you want to run and use this chatbot app within your Kubernetes cluster, you can easily install it using the Helm chart provided in this repository:

```
helm install [RELEASE_NAME] helm/ -f helm/values.yaml
```

## Tests

We have added unit tests to ensure the stability and reliability of the project.

### Running Tests

To run the tests, use the following command:

```
cd app
pytest tests/
```

This command will execute all the test cases present in the `tests` folder. The tests include validation of the API endpoints, ensuring correct interactions with GPT services, and verifying that the generated outputs meet expected standards.

# Contributing

Please read the [Contribution guide](https://github.com/abolfazl8131/devops-gpt/blob/master/CONTRIBUTING.md)

# Maintenance

**[Abolfazl Andalib](https://github.com/abolfazl8131)** - [abolfazlandalib@gmail.com](mailto:abolfazlandalib@gmail.com)
**[Mohammad Madanipour](https://github.com/mohammadll)** - [m.madanipourr@gmail.com](mailto:m.madanipourr@gmail.com)
