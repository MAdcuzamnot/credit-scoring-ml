import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset/lending_club_clean.csv')

print(df.head())
print('-----')
print(df.shape)
print('-----')
print(df.columns)
print('-----')
print(df.info())
print('-----')
print(df.isnull().sum())
print('-----')
print(df["default"].value_counts())
print(df["default"].value_counts(normalize=True) * 100)
print('-----')
df["default"].value_counts().sort_index().plot(
    kind="bar",
    color=["steelblue", "salmon"]
)

plt.title("Distribution of Credit Defaults")
plt.xlabel("Default Status")
plt.ylabel("Number of Borrowers")

plt.xticks(
    ticks=[0, 1],
    labels=["No Default", "Default"],
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "images/class_distribution.png",
    dpi=300
)
plt.show()

print(df["loan_amnt"].describe())

print('-----')

plt.figure(figsize=(10, 6))

plt.hist(df["loan_amnt"], bins=30, edgecolor="black")

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Number of Loans")

plt.tight_layout()

plt.savefig("images/loan_amount_distribution.png", dpi=300)

plt.show()

print('-----')

plt.figure(figsize=(10, 4))

plt.boxplot(df["loan_amnt"], vert=False)

plt.title("Loan Amount Boxplot")
plt.xlabel("Loan Amount")

plt.tight_layout()

plt.savefig("images/loan_amount_boxplot.png", dpi=300)

plt.show()