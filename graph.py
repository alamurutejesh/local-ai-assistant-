import matplotlib.pyplot as plt

models = ["Mistral", "Llama3.2", "Phi3"]

knowledge = [28.53, 19.40, 23.78]
coding = [39.90, 16.86, 91.60]
reasoning = [10.35, 10.83, 98.55]

x = range(len(models))

plt.figure(figsize=(8,5))

plt.plot(x, knowledge, marker="o", label="Knowledge")
plt.plot(x, coding, marker="o", label="Coding")
plt.plot(x, reasoning, marker="o", label="Reasoning")

plt.xticks(x, models)

plt.xlabel("Models")
plt.ylabel("Time (seconds)")
plt.title("Local SLM Benchmark")
plt.legend()

plt.grid()

plt.show()