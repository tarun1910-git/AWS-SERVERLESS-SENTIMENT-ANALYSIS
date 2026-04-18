# AWS-SERVERLESS-SENTIMENT-ANALYSIS

# ☁️ AWS Serverless Sentiment Analysis

A scalable **serverless application** that analyzes text sentiment using AWS services.
This project demonstrates how to build a cloud-based sentiment analysis pipeline without managing servers.

---

## 🚀 Project Overview

This system processes input text and determines its sentiment as:

* 😊 Positive
* 😐 Neutral
* 😡 Negative

The application is built using AWS serverless architecture, ensuring **high scalability, low cost, and no infrastructure management**.

---

## 🏗️ Architecture

The workflow follows a typical AWS serverless pattern:

1. User provides input (text)
2. Request is processed via AWS Lambda
3. Sentiment analysis is performed using AWS services
4. Result is returned to the user

Serverless architectures like this eliminate the need for managing infrastructure and allow automatic scaling ([GitHub][1])

---

## 🛠️ Tech Stack

* **AWS Lambda** – Backend processing
* **Amazon Comprehend** – Sentiment analysis
* **Amazon S3** – Storage (if used)
* **API Gateway** – API handling (if implemented)
* **IAM** – Security & permissions
* **Python / Node.js** – Backend logic

---

## 📂 Project Structure

id="proj-struct"
AWS-SERVERLESS-SENTIMENT-ANALYSIS/
│── lambda_function/
│── events/
│── template.yaml
│── README.md

---

## ⚙️ How It Works

* Input text is sent to the Lambda function
* Lambda calls **Amazon Comprehend API**
* Comprehend analyzes text using NLP
* Response is returned with sentiment score

---

## 🧪 Example

**Input:**

id="input"
"I really love this product!"


**Output:**

id="output"
Sentiment: Positive
Confidence: High

---

## 📦 Setup & Deployment

### Prerequisites

* AWS Account
* AWS CLI configured
* AWS SAM / Serverless framework
* Git

---

### Steps

`id="setup"
git clone https://github.com/tarun1910-git/AWS-SERVERLESS-SENTIMENT-ANALYSIS
cd AWS-SERVERLESS-SENTIMENT-ANALYSIS


Deploy using AWS SAM:

id="deploy"
sam build
sam deploy --guided

## 📌 Features

* Serverless architecture
* Real-time sentiment analysis
* Scalable & cost-efficient
* No infrastructure management
* Cloud-native design

---

## 📸 Screenshots

(Add architecture diagram / output screenshots here)

---

## 🔮 Future Improvements

* 🌐 Web frontend integration
* 📊 Dashboard for analytics
* 🧠 Multi-language sentiment support
* 🔍 Batch processing of large datasets

---

## 👨‍💻 Author

**Tarun Ankana**
B.Tech Student (2026)

---

