**# Local AI Assistant using Ollama**



**## Overview**



**This project is an offline AI assistant built using Ollama, FastAPI, and Small Language Models (SLMs).**



**## Features**



**\* Fully offline AI assistant**

**\* Supports multiple models:**



&#x20; **\* Mistral**

&#x20; **\* Llama 3.2**

&#x20; **\* Phi-3**

**\* FastAPI backend**

**\* HTML/CSS/JavaScript frontend**

**\* Conversation memory**

**\* Model benchmarking**

**\* Privacy-focused design**



**## Technologies Used**



**\* Python 3.11**

**\* Ollama**

**\* FastAPI**

**\* HTML**

**\* CSS**

**\* JavaScript**



**## Installation**



**1. Install Python 3.11**

**2. Install Ollama**

**3. Create virtual environment**



**```bash**

**python -m venv venv**

**```**



**4. Activate virtual environment**



**```bash**

**venv\\Scripts\\activate**

**```**



**5. Install dependencies**



**```bash**

**pip install fastapi uvicorn requests jinja2 matplotlib**

**```**



**6. Download models**



**```bash**

**ollama pull mistral**

**ollama pull llama3.2**

**ollama pull phi3**

**```**



**7. Run application**



**```bash**

**python -m uvicorn app:app --reload**

**```**



**8. Open**



**http://127.0.0.1:8000**



**## Benchmark Results**



**Models compared:**



**\* Mistral**

**\* Llama 3.2**

**\* Phi-3**



**Benchmark categories:**



**\* Knowledge**

**\* Coding**

**\* Reasoning**



**## Advantages**



**\* No cloud dependency**

**\* No API cost**

**\* Better privacy**

**\* Low latency**



