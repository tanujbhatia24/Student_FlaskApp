# Jenkins CI/CD Pipeline for Flask Application

## 📌 Objective

Set up a Jenkins pipeline to automate the build, test, and deployment of a simple Python Flask web application.

---

## 🚀 Project Overview

This project demonstrates how to configure and run a CI/CD pipeline using Jenkins to:

- Install dependencies
- Run unit tests with `pytest`
- Deploy the application to a staging environment
- Trigger builds automatically upon code changes
- Notify team members via email about pipeline status

---

## 📁 Sample Flask Application Repository

Fork this sample Flask app to begin:  
🔗 [Sample Python Flask App](https://github.com/pallets/flask/tree/main/examples/tutorial)

---

## 🛠️ Setup

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
<br>Git
<br>Pipeline
<br>Email Extension
---

## Triggers
### GitHub Webhook
1. Go to your GitHub repository: Settings > Webhooks
2. Click Add Webhook:<br>
   Payload URL: http://<JENKINS_URL>/github-webhook/<br>
   Content type: application/json<br>
   Trigger: Just the push event<br>

### Jenkins Configuration
1. In your Jenkins project:
   Check Build Triggers > “GitHub hook trigger for GITScm polling”

### Notifications
1. Go to Manage Jenkins > Configure System
2. Set up SMTP under Email Notification
3. Configure Email Extension Plugin:
   Email notifications are handled in the post block of your Jenkinsfile

### Documentation
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
1. Jenkins dashboard showing pipeline success

2. Console output for each stage

3. Email notification screenshot

