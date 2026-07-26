print("Starting program...")

from data.data_loader import load_housing_data

print("Import successful!")

def main():
    print("Inside main()")

    data = load_housing_data()
    print("Saving data...")

    data.to_csv("los_angeles_housing_data.csv")

    print("Saved!")
    print(data.head())


if __name__ == "__main__":
    print("Calling main()")
    main()

print("Program finished!")