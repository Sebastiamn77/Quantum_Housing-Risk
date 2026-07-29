print("Starting program...")
from data.data_loader import load_housing_data
from quantum.qae import quantum_risk_estimate
import numpy as np
import time
import pandas as pd
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

        while True:

            year = int(input("Enter year (1987-2026): "))

            if selected_city == "Phoenix" and year in [1987,1988]:
                print("Not enough data. Pick another year.")
                continue

            if selected_city == "Seattle" and year in [1987,1988,1989]:
                print("Not enough data. Pick another year.")
                continue

            break


        data = data[data.index.year == year]
    elif time_choice == 3:

        years = int(input("How many recent years? "))

        latest_year = data.index[-1].year

        data = data[
            data.index.year >= latest_year - years
        ]
    # Future Simulation
    future_months = int(input("""
How many months into the future should we simulate?

Examples:
6  = 6 months
12 = 1 year
24 = 2 years
60 = 5 years

Months: """))

    # Historical Analysis
    returns = data.pct_change().dropna()

    crash_threshold = -0.025


    crash_probability = np.mean(
        returns < crash_threshold
    )


    volatility = returns.std()


    drawdowns = data / data.cummax() - 1

    max_drawdown = drawdowns.min()

    worst_drop_date = drawdowns.idxmin()

    peak_date = data.loc[:worst_drop_date].idxmax()



    risk_score = (
        crash_probability * 0.5
        +
        volatility * 0.3
        +
        abs(max_drawdown) * 0.2
    )



    print("\n=================================")
    print("        HOUSING RISK REPORT")
    print("=================================")


    print(f"""
Market:
{selected_city}

Analysis Period:
{data.index[0].strftime("%B %Y")}
-
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

Drop Started:
{peak_date.strftime("%B %Y")}

Bottom:
{worst_drop_date.strftime("%B %Y")}

Overall Risk Score:
{risk_score:.4f}

=================================
""")



    # Monte Carlo Simulation
    simulations = 100000
    future_crashes = []
    start_time = time.time()
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
    monte_carlo_time = time.time() - start_time
    # User Choice
    analysis = int(input("""

Choose Analysis

1. Historical
2. Monte Carlo
3. Quantum
4. Compare All

Choice: """))
    if analysis == 1:

        print("\nHistorical Crash Probability:")
        print(f"{crash_probability:.2%}")
    elif analysis == 2:

        print(f"""
      MONTE CARLO RESULT
Market:
{selected_city}

Future Risk:
{monte_carlo_probability:.2%}

Simulation Period:
{future_months} months

Simulations:
{simulations}

Runtime:
{monte_carlo_time:.6f} seconds

=================================
""")



    elif analysis == 3:

        print("\nRunning Quantum...")


        quantum_probability, difference, quantum_time = quantum_risk_estimate(
            monte_carlo_probability
        )


        print(f"""
=================================
        QUANTUM RESULT
=================================

Market:
{selected_city}

Monte Carlo:
{monte_carlo_probability:.2%}

Quantum Estimate:
{quantum_probability:.2%}

Difference:
{difference:.2%}

Quantum Runtime:
{quantum_time:.6f} seconds

=================================
""")
    elif analysis == 4:
        print("\nRunning Full Comparison...")
        quantum_probability, difference, quantum_time = quantum_risk_estimate(
            monte_carlo_probability
        )
        print(f"""
=================================
        FINAL COMPARISON
=================================

Market:
{selected_city}

Future Period:
{future_months} months


Historical Risk:
{crash_probability:.2%}


Monte Carlo:
{monte_carlo_probability:.2%}

Monte Carlo Runtime:
{monte_carlo_time:.6f} seconds


Quantum:
{quantum_probability:.2%}

Quantum Runtime:
{quantum_time:.6f} seconds


Quantum Difference:
{difference:.2%}

=================================
""")


        results = pd.DataFrame({
            "Market": [selected_city],
            "Future Months": [future_months],
            "Historical Risk": [crash_probability],
            "Monte Carlo Risk": [monte_carlo_probability],
            "Quantum Estimate": [quantum_probability],
            "Difference": [difference]
        })


        results.to_csv(
            "data/latest_prediction.csv",
            index=False
        )


        print("Results saved to data/latest_prediction.csv")
    else:

        print("Invalid choice")
    print("\nProgram finished!")
if __name__ == "__main__":
    print("Calling main()")
    main()