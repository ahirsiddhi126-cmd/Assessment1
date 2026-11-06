"""
RECORD CHECK  -  my version
===========================

Name  : Ahir Siddhi
Lane  :  AI      (delete two)
Date  : 06-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ai_data.csv")

df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

# Classify each dataset so it is easy to identify loading problems
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)

print(df)

# Show datasets that did not load as expected
print("\nRows that are not OK:")   # Display datasets that need attention
print(df[df["status"] != "OK"])

print("\nCount per status:") #display the count of datasets in each status
counts = df.groupby("status").size()
print(counts)

df.to_csv("ai_data.csv", index=False)

# A bar chart to compare the different statuses
counts.plot(kind="bar")
plt.title("Dataset Loading Status")
plt.xlabel("Status")
plt.ylabel("Number of Datasets")
plt.tight_layout()   # Adjust the chart to fit the labels
plt.savefig("ai_status_counts.png") #Saves the chart as a PNG file
plt.show()


print(df)

