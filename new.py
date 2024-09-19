import pandas as pd 
df = pd.read_csv("indeed1_jobs.csv")
df.drop_duplicates(inplace=True)
pd.options.display.max_rows = 99999
df.to_csv("indeed2.csv",index=False)
import numpy as np

# Define the list of types
type_list = ['Part-time', 'Full-time', 'Internship', 'Permanent']

# Randomly assign values from type_list to 'type' column
df['type'] = np.random.choice(type_list, size=len(df))

import numpy as np

# Define salary conditions using np.where with ₹ sign and proper formatting
df['salary_package'] = np.where(df['type'] == 'Full-time', '₹ 10000',
                       np.where(df['type'] == 'Permanent', '₹ 15000',
                       np.where(df['type'] == 'Part-time', '₹ 8000',
                       np.where(df['type'] == 'Internship', '₹ 5000', '₹ 0'))))
df.to_csv("New_indeed.csv",index=False)
print(df)


