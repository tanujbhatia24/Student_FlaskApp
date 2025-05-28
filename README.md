# Jenkins CI/CD Pipeline for Flask Application

## Objective
Set up a Jenkins pipeline to automate the build, test, and deployment of a simple Python Flask web application.

## Project Overview
This project demonstrates how to configure and run a CI/CD pipeline using Jenkins to:
- Install dependencies
- Run unit tests with `pytest`
- Deploy the application to a staging environment
- Trigger builds automatically upon code changes
- Notify team members via email about pipeline status
---

## Sample Flask Application Repository
Fork this sample Flask app to begin:  
🔗 [Sample Python Flask App](https://github.com/mohanDevOps-arch/Student_App)
---

## Setup
### 1. Jenkins Installation
- **Option 1**: Install Jenkins on a local or cloud-based VM (e.g., AWS EC2, DigitalOcean, GCP Compute Engine).
- **Option 2**: Use a cloud-based Jenkins service (e.g., CloudBees, Jenkins X).

Follow the official [Jenkins Installation Guide](https://www.jenkins.io/doc/book/installing/).

### 2. Install Required Tools on Jenkins Server
```bash
sudo yum update
sudo yum install python3 python3-pip
pip3 install virtualenv pytest
```

### 3. Install Jenkins Plugins<br>
Install the following plugins from Manage Jenkins > Plugin Manager:<br>
1. Git
2. Pipeline
3. Email Extension

### 4. Add MongoDB URI as Jenkins Credential
1. Go to Jenkins Dashboard > Manage Jenkins > Credentials
2. Choose the domain (usually (global))
3. Click Add Credentialsbr<>
   Kind: Secret text<br>
   Secret: Your MongoDB URI (e.g., mongodb+srv://user:pass@cluster.mongodb.net/db)<br>
   ID: tanuj-MONGO-URI (must match the ID used in Jenkinsfile)<br>
   Description: MongoDB connection string<br>

### 5. Add EC2 SSH Private Key in Jenkins
1. Go to Jenkins Dashboard > Manage Jenkins > Credentials
2. Select the appropriate domain (e.g., (global))
3. Click Add Credentials<br>
   Kind: SSH Username with private key<br>
   Username: ec2-user (or whatever your EC2 login username is)<br>
   Private Key: Choose "Enter directly", and paste your .pem key (e.g., tanuj-ec2-key.pem)<br>
   ID: tanuj-EC2-SSH (you will use this ID in Jenkinsfile)<br>
---

## Triggers
### GitHub Webhook
1. Go to your GitHub repository: Settings > Webhooks
2. Click Add Webhook:<br>
   Payload URL: http://<JENKINS_URL>/github-webhook/<br>
   Content type: application/json<br>
   Trigger: Just the push event<br>

### Jenkins Configuration
1. In your Jenkins project:<br>
   Check Build Triggers > “GitHub hook trigger for GITScm polling”

### Notifications
1. Go to Manage Jenkins > Configure System
2. Set up SMTP under Email Notification
3. Configure Email Extension Plugin:
   Email notifications are handled in the post block of your Jenkinsfile
---

## Documentation
### Prerequisites
1. Python 3.x and pip
2. Jenkins installed and running
3. Jenkins plugins: Git, Pipeline, Email Extension
4. GitHub repository with Flask app and Jenkinsfile

### Submission Checklist
1. Forked GitHub repo with Flask app and Jenkinsfile
2. Jenkins pipeline with build, test, and deploy stages
3. Email notifications on build success/failure
4. GitHub webhook triggers on push to main
5. Screenshots showing each pipeline stage (build, test, deploy)

### Screenshots
1. Jenkins dashboard showing pipeline success<br>
   <img width="686" alt="image" src="https://github.com/user-attachments/assets/17ac6ed3-44bd-4e6a-bc25-7a99691eb34f" /><br>

2. Automatic pipeline build trigger<br>
   <img width="932" alt="image" src="https://github.com/user-attachments/assets/ef6ba821-f5de-44ef-812b-240704757369" /><br>
   
3. Jenkins pripeline overview<br>
   ![image](https://github.com/user-attachments/assets/dc0405cc-72a5-4b72-afb6-4f4d3eadb6dc)<br>

4. Email notifications<br>
   Failure Email<br>
   <img width="331" alt="image" src="https://github.com/user-attachments/assets/2b38ac01-276c-4d2e-9511-4ef56213ec86" /><br>
   Success Email<br>
   <img width="487" alt="image" src="https://github.com/user-attachments/assets/ae8a57b1-0910-4453-b5be-859fb123e301" /><br>

5. Application Screenshots<br>
   ![image](https://github.com/user-attachments/assets/5702d435-98f7-4d02-9ac3-8568ac377a6a)<br>
   ![image](https://github.com/user-attachments/assets/71514d29-61f4-4685-ac2c-053ec411debe)<br>
   <img width="271" alt="image" src="https://github.com/user-attachments/assets/dcac4fde-e7ae-4eb2-8f1b-69a73a29a2be" /><br>

6. Adding new users<br>
   <img width="489" alt="image" src="https://github.com/user-attachments/assets/139c1aff-2719-46f0-b817-730960f4e66d" /><br>
   <img width="217" alt="image" src="https://github.com/user-attachments/assets/35ec39d1-beb5-4ad6-ab36-b8db842bebef" /><br>
   <img width="418" alt="image" src="https://github.com/user-attachments/assets/8ba4da7c-c4ed-4416-ab1b-c0eaf95fc93d" /><br>
---

## License
This project is intended for educational and demonstration purposes. You are welcome to use and adapt it as a reference; however, please ensure that your work represents your own understanding and is not reproduced verbatim.
