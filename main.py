print("Starting program...")

from data.data_loader import load_housing_data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

print("Import successful!")


def main():
    print("Inside main()")

    cities = [
        "Los Angeles",
        "San Francisco",
        "San Diego",
        "Las Vegas",
        "Phoenix",
        "Seattle",
        "Denver",
        "Miami",
        "New York",
        "Chicago",
        "Boston",
        "Washington DC"
    ]

    print("\nAvailable Cities:\n")

    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    choice = int(input("\nChoose a city (1-12): "))

    selected_city = cities[choice - 1]

    print(f"\nLoading {selected_city}...\n")


    data = load_housing_data(selected_city)[selected_city]

    print("Loading data...")


    # -----------------------------
    # Time Selection
    # -----------------------------

    print("""
Choose Time Period:

1. All Historical Data
2. Specific Year
3. Recent Years

""")

    time_choice = int(input("Choice: "))


    if time_choice == 2:

        year = int(input("Enter year (1987-2026): "))
        if year in [1987, 1988] and selected_city == "Phoenix":
            print ("Sorry there is not enough data to run a simulation, Pick a diffrent year")
            year = int(input("Enter year (1987-2026): "))
        elif year in [1987, 1988, 1989] and selected_city == "Seattle":
            print ("Sorry there is not enough data to run a simulation, Pick a diffrent year")
            year = int(input("Enter year (1987-2026): "))

        data = data[
            data.index.year == year
        ]


    elif time_choice == 3:

        years = int(input("How many recent years? "))

        latest_year = data.index[-1].year

        data = data[
            data.index.year >= latest_year - years
        ]


    # -----------------------------
    # Future Prediction Settings
    # -----------------------------

    future_months = int(input("""
How many months into the future should we simulate?

6  = 6 months
12 = 1 year
24 = 2 years

Months: """))



    # -----------------------------
    # Classical Risk Analysis
    # -----------------------------

    returns = data.pct_change().dropna()

    crash_threshold = -0.025

    crashes = returns < crash_threshold

    crash_probability = crashes.mean()

    volatility = returns.std()

    max_drawdown = (data / data.cummax() - 1).min()

# Find when the worst drop happened
    drawdowns = data / data.cummax() - 1

    worst_drop_date = drawdowns.idxmin()

# Find the peak before the drop
    peak_date = data.loc[:worst_drop_date].idxmax()

    print("Worst Historical Drop:")
    print(f"{max_drawdown:.2%}")

    print("Peak Before Drop:")
    print(peak_date.strftime("%B %Y"))

    print("Bottom Of Drop:")
    print(worst_drop_date.strftime("%B %Y"))

    risk_score = (
        crash_probability * 0.5
        + volatility * 0.3
        + abs(max_drawdown) * 0.2
    )


    print("\n=================================")
    print("        HOUSING RISK REPORT")
    print("=================================")

    print(f"""
    Market:
    {selected_city}

    Analysis Period:
    {data.index[0].strftime("%B %Y")} -
    {data.index[-1].strftime("%B %Y")}

    Future Simulation:
    {future_months} months

    Risk Metrics:

    Crash Probability:
    {crash_probability:.2%}

    Market Volatility:
    {volatility:.2%}

    Worst Historical Drop:
    {max_drawdown:.2%}

    Overall Risk Score:
    {risk_score:.4f}

    =================================
    """)



    # -----------------------------
    # User chooses analysis
    # -----------------------------

    analysis = int(input("""

Choose Analysis

1. Historical
2. Monte Carlo
3. Quantum
4. Compare All

Choice: """))



    if analysis == 1:

        print("\nRunning Historical Analysis...")
        print(f"{selected_city} historical crash probability:")
        print(f"{crash_probability:.2%}")



    elif analysis == 2:

        print("\nRunning Monte Carlo Future Simulation...")

        start_time = time.time()

        simulations = 10000

        future_crashes = []


        for i in range(simulations):

            simulated_returns = np.random.choice(
                returns,
                size=future_months
            )

            crash_happened = np.any(
                simulated_returns < crash_threshold
            )

            future_crashes.append(crash_happened)



        monte_carlo_probability = np.mean(
            future_crashes
        )


        end_time = time.time()


        print("\nMonte Carlo Future Crash Probability:")
        print(f"{monte_carlo_probability:.2%}")

        print("Forecast Period:")
        print(f"{future_months} months")

        print("Simulations:")
        print(simulations)

        print("Runtime:")
        print(end_time - start_time, "seconds")



    elif analysis == 3:

        print("\nRunning Quantum...")
        print("Quantum model coming next!")



    elif analysis == 4:

        print("\nRunning Full Comparison...")

        print("\nHistorical:")
        print(f"{crash_probability:.2%}")


        print("\nMonte Carlo:")

        simulations = 10000

        future_crashes = []


        for i in range(simulations):

            simulated_returns = np.random.choice(
                returns,
                size=future_months
            )

            future_crashes.append(
                np.any(simulated_returns < crash_threshold)
            )


        monte_carlo_probability = np.mean(
            future_crashes
        )


        print(f"{monte_carlo_probability:.2%}")


        print("\nQuantum:")
        print("Connecting QAE model next!")



    else:
        print("Invalid choice")


    print("\nProgram finished!")



if __name__ == "__main__":
    print("Calling main()")
    main()