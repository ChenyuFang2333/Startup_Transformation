import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
print(financial_data)
print(financial_data.info())
month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses
#revenue
plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
plt.clf()
#expenses
plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()
plt.clf()
'''
The company's revenue decreases drastically over the 6 month whilst the expenses increase over the same time period.
'''
expense_overview = pd.read_csv('expenses.csv')
print(expense_overview)
# expense_categories = expense_overview.Expense
# proportions = expense_overview.Proportion
# plt.pie(proportions, labels = expense_categories)
# plt.title('Expense Categories')
# plt.axis('equal')
# plt.tight_layout()
# plt.show()
# plt.clf()
'''
Salaries make up most of the data. Food and supples are not so significant.
'''
expense_overview.loc[expense_overview.Proportion < 0.05, 'Expense'] = 'other'
#print(expense_overview.groupby('Expense').sum())
expense_overview_new = expense_overview.groupby('Expense', as_index = False).sum()
print(expense_overview_new)

expense_categories = expense_overview_new.Expense
proportions = expense_overview_new.Proportion
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.clf()

expense_cut = 'Salaries'
#employee productivity
employee = pd.read_csv('employees.csv')
print(employee.head())
print(employee.info())
sorted_productivity = employee.sort_values(by=['Productivity'])
print(sorted_productivity)
employees_cut = sorted_productivity.head(100)
print(employees_cut)
transformation = 'standardization'
#income vs productivity (standardization)
from sklearn.preprocessing import StandardScaler
income_productivity = employee[['Salary', 'Productivity']]
# income = employee.Salary
# productivity = employee.Productivity
#print(income_productivity)
#print(productivity)
scaler = StandardScaler()

standardized = scaler.fit_transform(income_productivity)
'''Sorting arrays in NumPy by column
sorted_standardized = standardized[standardized[:, 0].argsort()] #sorting by the first column
'''
#print(sorted_standardized)
#print(standardized[:,[0]])
standardized_income = standardized[:,[0]]
standardized_productivity = standardized[:,[1]]
# print(standardized_productivity)
# print(standardized)
plt.clf()
plt.plot(standardized_income,standardized_productivity,'o')
plt.show()
'''
There is no obvious relationship between income and productivity.There are people with high and low productivity in both high and low income categories
'''
#commute times
commute_times = employee['Commute Time']
print(commute_times)
print(commute_times.describe())
'''average commute times = 33.44
median = 31.06
the commute times is not that long for most employees in the company. There is no need for indefinite remote work.
'''
plt.clf()
plt.hist(commute_times, bins = 20)
plt.xlabel('Commute Times (minutes)')
plt.ylabel('Count')
plt.title('Employees Commute Times')
plt.show()
'''right skewed'''
#using scikit-learn
# from sklearn.preprocessing import PowerTransformer
# long_transform = PowerTransformer()
# commute_times_log = long_transform.fit_transform(commute_times.reset_index())
# print(commute_times_log)
# plt.clf()
# plt.hist(commute_times_log[:,[1]], bins = 20)
# plt.xlabel('Commute Times (minutes)')
# plt.ylabel('Count')
# plt.title('Employees Commute Times')
# plt.show()

#using numpy log()
commute_times_log = np.log(commute_times)
print(commute_times_log)
plt.clf()
plt.hist(commute_times_log, bins = 20)
plt.xlabel('Commute Times (minutes)')
plt.ylabel('Count')
plt.title('Employees Commute Times')
plt.show()
print(commute_times.skew()) #1.15
print(commute_times_log.skew())
