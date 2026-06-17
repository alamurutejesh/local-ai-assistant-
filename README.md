## Local AI Assistant Using Ollama

## Overview

Local AI Assistant is an offline chatbot built using **Ollama**, **FastAPI**, and **Small Language Models (SLMs)**. The application runs entirely on a local machine without requiring cloud APIs, providing enhanced privacy, zero API costs, and low-latency responses.

## Features

* Fully offline AI assistant
* Multiple model support:

  * Mistral
  * Llama 3.2
  * Phi-3
* FastAPI backend
* Modern web interface using HTML, CSS, and JavaScript
* Conversation memory
* Model benchmarking and performance comparison
* Privacy-focused architecture
* No external API dependency

## Technologies Used

* Python 3.11
* Ollama
* FastAPI
* HTML5
* CSS3
* JavaScript
* Requests
* Jinja2
* Matplotlib

## Project Structure

```text
local-ai-assistant/
│
├── app.py
├── benchmark.py
├── graph.py
├── results.csv
├── README.md
├── report.md
│
├── screenshots/
│
├── templates/
│   └── index.html
│
└── venv/
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/local-ai-assistant-.git
cd local-ai-assistant-
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn requests jinja2 matplotlib
```

### 5. Install Ollama

Download and install Ollama from:

https://ollama.com

### 6. Download Models

```bash
ollama pull mistral
ollama pull llama3.2
ollama pull phi3
```

### 7. Run the Application

```bash
python -m uvicorn app:app --reload
```

### 8. Open in Browser

```text
http://127.0.0.1:8000
```

## Benchmark Evaluation

The following models were evaluated:

* Mistral
* Llama 3.2
* Phi-3

### Benchmark Categories

* Knowledge Tasks
* Coding Tasks
* Reasoning Tasks

### Sample Prompts

**Knowledge**

> Explain Machine Learning in 100 words.

**Coding**

> Write a Python function for Binary Search.

**Reasoning**

> A farmer has 17 sheep. All but 9 die. How many remain?

## Advantages

* Runs completely offline
* No subscription costs
* No API token usage
* Better privacy and security
* Supports multiple local language models
* Easy deployment and customization

## Future Enhancements

* Streaming responses
* Voice input support
* PDF question answering
* Chat export functionality
* Model comparison dashboard
* Dark/Light theme toggle

## Author

Tejesh Naidu

## License

This project is developed for educational and learning purposes.




