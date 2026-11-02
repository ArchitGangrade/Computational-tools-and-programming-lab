import numpy as np
import pandas as pd


def clean_dataset():
    file_path = input(
        "Enter path to CSV dataset (press Enter to use a generated sample dataset):"
    ).strip()

    if not file_path:
        print("No dataset path provided.")
        return

    df = pd.read_csv(file_path)

    print("\n--- Original Dataset Loaded ---")
    print(df)

    df = df.drop_duplicates()

    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

    df["Cabin"] = df["Cabin"].fillna("Unknown")
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    print("\n--- Cleaned & Preprocessed Dataset ---")
    print(df)

    df.to_csv("output.csv", index=False)

    print("\nCleaned dataset saved to output.csv")

    return df


if __name__ == "__main__":
    clean_dataset()

