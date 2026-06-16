**# Local AI Assistant using Ollama**



**## 1. Objective**



**The objective of this project is to build a fully offline AI assistant using Small Language Models (SLMs) running locally through Ollama. The system provides AI-powered responses without relying on cloud APIs, ensuring privacy, reduced latency, and zero API costs.**



**---**



**## 2. System Architecture**



**The system consists of four main components:**



**1. User Interface (HTML, CSS, JavaScript)**

**2. FastAPI Backend**

**3. Ollama Runtime**

**4. Local Language Models**



**Architecture Flow:**



**User → Web Interface → FastAPI → Ollama → Local SLM → Response**



**---**



**## 3. Technologies Used**



**\* Python 3.11**

**\* Ollama**

**\* FastAPI**

**\* HTML**

**\* CSS**

**\* JavaScript**

**\* Matplotlib**



**Models Used:**



**\* Mistral**

**\* Llama 3.2**

**\* Phi-3**



**---**



**## 4. Implementation**



**### Frontend**



**A browser-based chat interface was developed using HTML, CSS, and JavaScript. Users can:**



**\* Enter prompts**

**\* Select a model**

**\* View AI responses**

**\* Clear chat history**



**### Backend**



**FastAPI handles incoming requests and forwards them to Ollama.**



**### Model Execution**



**Ollama runs all language models locally on the user's machine.**



**---**



**## 5. Benchmarking**



**Three benchmark categories were used:**



**### Knowledge Task**



**Prompt:**

**"Explain machine learning in 100 words."**



**### Coding Task**



**Prompt:**

**"Write a Python function for binary search."**



**### Reasoning Task**



**Prompt:**

**"A farmer has 17 sheep. All but 9 die. How many remain?"**



**---**



**## 6. Benchmark Results**



**| Model     | Knowledge (s) | Coding (s) | Reasoning (s) |**

**| --------- | ------------- | ---------- | ------------- |**

**| Mistral   | 28.53         | 39.90      | 10.35         |**

**| Llama 3.2 | 19.40         | 16.86      | 10.83         |**

**| Phi-3     | 23.78         | 91.60      | 98.55         |**



**---**



**## 7. Analysis**



**### Mistral**



**Advantages:**



**\* Detailed answers**

**\* Good coding capability**



**Disadvantages:**



**\* Slower than Llama 3.2**



**### Llama 3.2**



**Advantages:**



**\* Fastest overall model**

**\* Good balance between quality and speed**



**Disadvantages:**



**\* Slightly less detailed than Mistral**



**### Phi-3**



**Advantages:**



**\* Acceptable knowledge responses**



**Disadvantages:**



**\* Very high response times for coding and reasoning tasks**



**---**



**## 8. Privacy Considerations**



**Since all models run locally:**



**\* User data never leaves the device**

**\* No third-party API is required**

**\* Better privacy and security**



**---**



**## 9. Cost Analysis**



**The system operates without paid AI APIs.**



**Benefits:**



**\* No subscription fees**

**\* No token costs**

**\* Only local hardware resources are used**



**---**



**## 10. Latency Analysis**



**Latency varies depending on:**



**\* Model size**

**\* Prompt complexity**

**\* System hardware**



**Among the tested models, Llama 3.2 provided the best latency-performance balance.**



**---**



**## 11. Conclusion**



**A fully functional offline AI assistant was successfully developed using Ollama and FastAPI. Three Small Language Models were benchmarked and compared. The results demonstrate that local AI systems can provide useful responses while maintaining privacy, eliminating API costs, and reducing dependency on cloud services.**



**Llama 3.2 achieved the best overall balance between response quality and speed on the tested hardware.**



