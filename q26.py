import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"],
    "Study_Hours": [8, 10, 12, 15, 18, 20, 7, 14, 16, 22],
    "Exam_Score": [65, 72, 75, 82, 88, 90, 60, 80, 85, 95],
}
df = pd.DataFrame(data)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(
    df["Study_Hours"],
    df["Exam_Score"],
    color="purple",
    s=100,
    edgecolors="black",
)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours/Week")
plt.ylabel("Exam Score")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.hist(
    df["Exam_Score"], bins=5, color="teal", edgecolor="black", alpha=0.7
)
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
