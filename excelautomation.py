import pandas as pd
# 1. Imagine this is raw data (or load it with pd.read_csv('data.csv'))
data = {
    'Employee': ['Naga', 'Raju', 'Sam', 'Anita'],
    'Department': ['IT', 'HR', 'IT', 'Sales'],
    'Salary': [50000, 45000, 52000, 48000],
    'Bonus_Percent': [0.10, 0.05, 0.10, 0.15] # 10%, 5%, etc.
}

print("Reading Data...")
df = pd.DataFrame(data)
# 2. AUTOMATION: Calculate the Total Bonus
# Instead of doing math manually for 1000 rows, Python does it instantly.
df['Bonus_Amount'] = df['Salary'] * df['Bonus_Percent']
df['Total_Pay'] = df['Salary'] + df['Bonus_Amount']
# 3. Filter Data: Show only IT Department
it_team = df[df['Department'] == 'IT']
print("Calculations Done! Sample:")
print(it_team)
# 4. Save to a real Excel file
df.to_excel("Salary_Report_2026.xlsx", index=False)
print("Excel File Created Successfully!")
