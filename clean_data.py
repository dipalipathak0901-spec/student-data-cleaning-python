import pandas as pd

# Sample student data
data = {
    'Name': ['Amit', 'Riya', None],
    'Marks': [85, None, 90]
}

df = pd.DataFrame(data)

# Cleaning data
df['Name'] = df['Name'].fillna('Unknown')
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print("Cleaned Data:")
print(df)
