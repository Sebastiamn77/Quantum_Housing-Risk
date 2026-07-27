import pandas as pd

results = pd.DataFrame({
    "Method": [
        "Classical Historical",
        "Quantum Sampling"
    ],
    "Crash Probability": [
        17/447,
        35/1000
    ]
})

print(results)

results.to_csv(
    "data/quantum_results.csv",
    index=False
)

print("Saved quantum results")