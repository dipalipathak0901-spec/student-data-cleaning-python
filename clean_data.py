import pandas as pd

df = pd.read_csv("student_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Save cleaned data
df.to_csv("cleaned_student_data.csv", index=False)

print("Data cleaned successfully")
print(df)
