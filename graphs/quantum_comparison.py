import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/quantum_results.csv")

plt.bar(
    data["Method"],
    data["Crash Probability"]
)

plt.ylabel("Crash Probability")
plt.title("Classical vs Quantum Housing Risk Estimate")

plt.savefig("graphs/quantum_comparison.png")

print("Graph saved!")