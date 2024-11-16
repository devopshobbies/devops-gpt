
# DevOps-GPT

This project helps you to balance your daily work as a DevOps engineer, from simple bug fixes to project template generation. you don't need to search on Google for some routine jobs and it helps you with a robust prompt to simplify your career.


## Run Locally

Clone the project

```
git clone https://github.com/devopshobbies/devops-gpt.git
```

Go to the project directory

```
cd devops-gpt
```

Run the project by its docker-compose

```
sh run.sh
```




## Deployment

If you want to run and use this chatbot app within your Kubernetes cluster, you can easily install it using the Helm chart provided in this repository

```
helm install [RELEASE_NAME] helm/ -f helm/values.yaml
```




## Running Tests

To run tests, run the following command

```
cd app && pytest tests/
```




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`KEY` (OpenAI API Key)




## API Reference

#### Get helm items

```
GET /download-helm/{filename}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `filename` | `string` | **Required** |

#### Get terraform items

```
GET /download-terraform/{filename}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `filename`      | `string` | **Required** |

#### Get list dirs

```
GET /list-directory
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `folder`      | `string` | **Required** |


#### Post terraform basic questions

```
POST /IaC-basic/
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `max_tokens`      | `int` | **Required** |
| `min_tokens`      | `int` | **Required** |
| `service`      | `string` | **Required** |
| `input`      | `string` | **Required** |


#### Post terraform bugfix

```
POST /IaC-bugfix/
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `max_tokens`      | `int` | **Required** |
| `min_tokens`      | `int` | **Required** |
| `service`      | `string` | **Required** |
| `bug_description`      | `string` | **Required** |
| `version`      | `string` | **Required** |



#### Post terraform installation

```
POST /IaC-install/
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `os`      | `string` | **Required** |
| `service`      | `string` | **Required** |


#### Post terraform template generation of docker resources

```
POST /IaC-template/docker
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `docker_image`      | `boolean` | **Required** |
| `docker_container`      | `boolean` | **Required** |


#### Post terraform template generation of Ec2 resources

```
POST /IaC-template/aws/ec2
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `key_pair`      | `boolean` | **Required** |
| `security_group`      | `boolean` | **Required** |
| `aws_instance`      | `boolean` | **Required** |
| `ami_from_instance`      | `boolean` | **Required** |

#### Post terraform template generation of S3 resources

```
POST /IaC-template/aws/s3
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `s3_bucket`      | `boolean` | **Required** |
| `s3_bucket_versioning`      | `boolean` | **Required** |


#### Post terraform template generation of IAM resources

```
POST /IaC-template/aws/iam
```

| Request Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `iam_user`      | `boolean` | **Required** |
| `iam_group`      | `boolean` | **Required** |



## Tech Stack

**Client:** React + TypeScript + Vite

**Server:** Python + FastAPI

**Containerization:** Docker + Kubernetes

**CI/CD**: Github Actions




## Contributing

Contributions are always welcome!

See `CONTRIBUTING.md` for ways to get started.




# Maintenance

** [Abolfazl Andalib](https://github.com/abolfazl8131) - abolfazlandalib@gmail.com **

** [Mohammad Madanipour](https://github.com/mohammadll) - m.madanipourr@gmail.com **
