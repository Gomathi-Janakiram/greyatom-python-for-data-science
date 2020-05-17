# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
print(bank_data.head())

#Code starts here
#step 1
"""Let's check which variable is categorical and which one is numerical so that you will get a basic idea about the features of the bank dataset."""
categorical_var=bank_data.select_dtypes(include="object")
print(categorical_var)
print(categorical_var.shape)
numerical_var=bank_data.select_dtypes(include="number")
print(numerical_var)
print(numerical_var.shape)

#step 2
"""Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them."""
banks=bank_data.drop(['Loan_ID'],axis=1)
print(banks.head())
print(banks.isnull().sum())
bank_mode=banks.mode()
print("mode",bank_mode)
banks.fillna(bank_mode,inplace=True)
banks['Gender']=banks['Gender'].fillna('Male')
banks['Married']=banks['Married'].fillna('Yes')
banks['Dependents']=banks['Dependents'].fillna(0)
banks['Self_Employed']=banks['Self_Employed'].fillna('No')
banks['LoanAmount']=banks['LoanAmount'].fillna(120)
banks['Loan_Amount_Term']=banks['Loan_Amount_Term'].fillna(360)
banks['Credit_History']=banks['Credit_History'].fillna(1)
print(banks.isnull().sum())

#step 3
"""Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person."""
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc="mean")
print(avg_loan_amount['LoanAmount'][1])

#step 4
""" Now let's check the percentage of loan approved based on a person's employment type."""
loan_approved_se=banks[(banks['Self_Employed']=="Yes") & (banks['Loan_Status']=="Y")].count()
print(loan_approved_se)

loan_approved_nse=banks[(banks['Self_Employed']=="No") & (banks['Loan_Status']=="Y")].count()
print(loan_approved_nse)

percentage_se=(56*100/614)
print("se",percentage_se)

percentage_nse=(366*100/614)
print("nse",percentage_nse)

#step 5
"""A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term."""
banks['loan_term']=banks['Loan_Amount_Term'].apply(lambda x:x/12)

big_loan_term=banks[banks['loan_term']>=25]
print(big_loan_term)
print("big_loan_term",big_loan_term.shape)

#step 6
""" Now let's check the average income of an applicant and the average loan given to a person based on their income."""
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
print("loan_groupby",loan_groupby.groups)
mean_values=loan_groupby.mean()
print("mean_values",mean_values.iloc[1,0])






