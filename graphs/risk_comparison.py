import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(
    "data/latest_prediction.csv"
)


methods = [
    "Historical Risk",
    "Monte Carlo Risk",
    "Quantum Estimate"
]


values = [
    data["Historical Risk"][0],
    data["Monte Carlo Risk"][0],
    data["Quantum Estimate"][0]
]


plt.figure(figsize=(8,5))

plt.bar(
    methods,
    values
)


plt.ylabel("Probability")

plt.title(
    f"{data['Market'][0]} Housing Risk Comparison"
)


plt.ylim(0,1)

plt.xticks(rotation=20)

plt.tight_layout()


plt.savefig(
    "graphs/risk_comparison.png"
)


print("Graph saved!")