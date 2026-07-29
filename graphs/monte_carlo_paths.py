import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(
    "data/latest_prediction.csv"
)
months = int(data["Future Months"][0])
print("Months from CSV:", months)
print(data)
starting_price = 100
returns = np.random.normal(
    0,
    0.01,
    (100, months)
)
paths = []
for r in returns:

    price = starting_price * np.cumprod(
        1 + r
    )

    paths.append(price)
plt.figure(figsize=(20,10))
for path in paths:

    plt.plot(path)
plt.title(
    f"{data['Market'][0]} Monte Carlo Future Simulations"
)
plt.xlabel("Months")
plt.ylabel("Housing Index")
plt.tight_layout()
plt.savefig(
    "graphs/monte_carlo_paths.png",
    dpi=600,
    bbox_inches="tight"
)
print("Monte Carlo graph saved!")