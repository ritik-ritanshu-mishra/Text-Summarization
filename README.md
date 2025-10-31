<h1 align="center" id="title">Text-Summarization</h1>

<p align="center"><img src="https://socialify.git.ci/RudraPrasadPanda1234/Text-Summarization/image?language=1&name=1&owner=1&pattern=Circuit%20Board&theme=Auto" alt="project-image"></p>

<p align="center">
    <br/>
    <a href="https://github.com/RudraPrasadPanda1234/Text-Summarization"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/RudraPrasadPanda1234/Text-Summarization">View Demo</a>
    .
    <a href="https://github.com/RudraPrasadPanda1234/Text-Summarization/issues">Report Bug</a>
    .
    <a href="https://github.com/RudraPrasadPanda1234/Text-Summarization/issues">Request Feature</a>
  </p>
</p>
<br/>

![Downloads](https://img.shields.io/github/downloads/RudraPrasadPanda1234/Text-Summarization/total)
![Contributors](https://img.shields.io/github/contributors/RudraPrasadPanda1234/Text-Summarization) 
![Forks](https://img.shields.io/github/forks/RudraPrasadPanda1234/Text-Summarization?style=flatl) 
![Stargazers](https://img.shields.io/github/stars/RudraPrasadPanda1234/Text-Summarization?style=flat) 
![Issues](https://img.shields.io/github/issues/RudraPrasadPanda1234/Text-Summarization)
![Pull Request](https://img.shields.io/github/issues-pr/RudraPrasadPanda1234/Text-Summarization)

## Table Of Contents
* [About The Project](#about-the-project)
* [Features](#features)
* [Built With](#built-with)
* [Project Screenshots](#project-screenshots)
* [How to run?](#how-to-run)
* [Contributing Guidlines](#contributing-guidlines)
# About The Project
The Text Summarization Project is an end-to-end Natural Language Processing (NLP) solution designed to extract concise summaries from extensive texts. This project leverages advanced transformer-based architectures to generate human-like, accurate, and context-aware text summaries. Built with flexibility and scalability in mind, the system is suitable for use cases ranging from summarizing news articles to legal documents, business reports, and beyond.<br>
This project includes robust functionalities such as data ingestion, preprocessing, model training, and deployment, and is designed to fit into a seamless machine learning pipeline. By integrating CI/CD pipelines and MLOps practices, this application ensures efficient development, deployment, and continuous improvement.

# Features
- **Text Summarization:**
  - Generates concise and meaningful summaries for long texts.
  - Supports **abstractive summarization** using **transformer-based models** such as **BART**, **T5**, and **GPT**.

- **Data Validation and Ingestion:**
  - Automated validation of dataset integrity.
  - Fetches data from specified sources and processes it for training.

- **Model Training and Fine-tuning:**
  - Fine-tunes pre-trained models like **BART**, **T5**, or **GPT** for summarization tasks.
  - Supports configurable hyperparameters for training.

- **Evaluation Metrics:**
  - Integrates evaluation metrics such as **ROUGE** and **BLEU** for comprehensive performance assessment.

- **API Deployment:**
  - Exposes summarization functionality via **REST APIs** using **FastAPI**.
  - Real-time summarization for user-provided input.

- **MLOps Monitoring:**
  - Implements monitoring for deployed models to ensure performance consistency.
  - Tracks **model versioning**, training metrics, and deployment logs using tools like **MLflow**.

- **User-Friendly Interface:**
  - Dynamic backend integration with visual representations of results.

- **Scalable Deployment:**
  - **Dockerized application** for scalable and portable deployments.
  - **CI/CD pipelines** using **GitHub Actions** for seamless updates and maintenance.


<!-- # Workflows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py -->
   
# Built With
* ***Programming Language:*** Python
* ***Frameworks:*** PyTorch, Hugging Face Transformers, FastAPI
* ***Libraries:***
  - **NLP and Summarization**: Hugging Face Transformers, NLTK, Datasets
  - **Evaluation:** SacreBLEU, ROUGE-Score
  - **Utilities:** tqdm, pandas, PyYAML, matplotlib
* ***MLOps Tools***:
  - **Version Control:** Git, GitHub Actions
  - **Model Deployment:** FastAPI, Uvicorn, Docker
  - **Monitoring:** MLflow, Prometheus
  - **Cloud Services:** AWS S3 For storing training data and model checkpoints, Boto3, CI/CD pipelines for deployment automation.
  


# How to run?
### STEPS:
### STEP 01- Clone the repository
```bash
git clone https://github.com/RudraPrasadPanda1234/Text-Summarization.git
```
### STEP 02- Create a conda environment after opening the repository
```bash
conda create -n texts python=3.9 -y
```

```bash
conda activate texts
```

### STEP 03- Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 04- Finally run the following command
```bash
streamlit run run.py
```

Now,
```bash
open up you local host and port
```

# Project Screenshots
<img src="https://github.com/user-attachments/assets/bb2e27da-452e-4c62-b64f-bbc9ceb4b03a" alt="Home Page">
<img src="https://github.com/user-attachments/assets/e32ee150-3465-438b-9282-2f0de4a478f7" alt="Model Training">
<img src="https://github.com/user-attachments/assets/561b0de8-1183-4c46-b05b-7bf365dd34a0" alt="Predict Text">
<img src="https://github.com/user-attachments/assets/d2878f7e-9557-4ca0-8000-a8bd9d6dcf8f" alt="Output">
<img src="https://github.com/user-attachments/assets/789f7d37-7df3-47ec-8c29-37e73fa9ee6d" alt="Settings">

## Contributing Guidlines

Contributions to improve the app's functionality add new features or fix bugs are welcome! If you'd like to contribute please fork the repository make your changes