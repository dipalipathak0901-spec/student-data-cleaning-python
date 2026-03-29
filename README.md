# Student Data Cleaning (Python)

This project demonstrates basic data cleaning using Python and pandas.

## Features
- Handling missing values
- Simple data processing

## Code Example

```python
import pandas as pd

data = {
    'Name': ['Amit', 'Riya', None],
    'Marks': [85, None, 90]
}

df = pd.DataFrame(data)

df['Name'] = df['Name'].fillna('Unknown')
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print(df)# student-data-cleaning-python
Simple Python script for cleaning student data
