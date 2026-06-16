import requests
import time

models = [
    "mistral",
    "llama3.2",
    "phi3"
]

prompts = {
    "Knowledge": "Explain machine learning in 100 words.",
    "Coding": "Write a Python function for binary search.",
    "Reasoning": "A farmer has 17 sheep. All but 9 die. How many remain?"
}

for model in models:

    print("\n" + "=" * 60)
    print("MODEL:", model)

    for category, prompt in prompts.items():

        start = time.time()

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        end = time.time()

        data = response.json()

        print("\nCATEGORY:", category)
        print("TIME:", round(end - start, 2), "seconds")

        if "response" in data:
            print(data["response"][:200])
        else:
            print("ERROR:", data)