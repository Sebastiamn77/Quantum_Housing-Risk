print("Starting program...")
from data.data_loader import load_housing_data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
print("Import successful!")
def main():
    print("Inside main()")
    data = load_housing_data()
    print("Saving data...")
    data.to_csv("los_angeles_housing_data.csv")
    print("Saved!")
    print(data.head())
    returns = data.pct_change()
    print("Monthly returns:")
    print(returns.head())
    crash_threshold = -0.025
    crashes = returns < crash_threshold
    print("Crash events:")
    print(crashes.head())
    crash_probability = crashes.sum() / len(crashes)

    print("Historical crash probability:")
    print(crash_probability)


    # Volatility (how unstable the market is)
    volatility = returns.std()

    print("Market volatility:")
    print(volatility)


    # Maximum drawdown (largest historical fall)
    max_drawdown = (data / data.cummax() - 1).min()

    print("Maximum drawdown:")
    print(max_drawdown)


    # Combined classical risk score
    risk_score = (
        (crash_probability * 0.5)
        +
        (volatility * 0.3)
        +
        (abs(max_drawdown) * 0.2)
    )

    print("Risk score:")
    print(risk_score)
        # Classical Monte Carlo benchmark

    start_time = time.time()

    simulations = 10000

    phoenix_returns = returns["Phoenix"].dropna()

    samples = np.random.choice(
        phoenix_returns,
        size=simulations
    )

    crash_probability_mc = np.mean(samples < crash_threshold)

    end_time = time.time()

    print("Monte Carlo crash probability:")
    print(crash_probability_mc)

    print("Monte Carlo runtime:")
    print(end_time - start_time, "seconds")
        # Quantum input preparation

    phoenix_crashes = (
        returns["Phoenix"]
        .dropna()
        < crash_threshold
    )

    quantum_data = phoenix_crashes.astype(int)

    print("Quantum input data:")
    print(quantum_data.head(20))

    print("Total crash events:")
    print(quantum_data.sum())

    print("Total observations:")
    print(len(quantum_data))


    # Save final classical model output
    risk_dataset = pd.DataFrame({
        "crash_probability": crash_probability,
        "volatility": volatility,
        "max_drawdown": max_drawdown,
        "risk_score": risk_score
    })
    risk_dataset.to_csv("data/housing_risk_scores.csv")
    print("Risk dataset saved!")
        # Risk ranking graph
    risk_score.sort_values().plot(
        kind="bar",
        title="Housing Market Risk Score"
    )
    plt.ylabel("Risk Score")
    plt.xlabel("Market")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graphs/risk_score_graph.png")
    print("Graph saved!")
    risk_data = returns.copy()
    risk_data.to_csv("data/housing_returns.csv")
if __name__ == "__main__":
    print("Calling main()")
    main()
print("Program finished!")