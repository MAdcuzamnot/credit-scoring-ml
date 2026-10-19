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