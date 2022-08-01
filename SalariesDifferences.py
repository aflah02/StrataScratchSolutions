# Import your libraries
import pandas as pd

# Start writing code
max_engineering = db_employee[db_employee['department_id'] == db_dept[db_dept['department'] == 'engineering']['id'].iloc[0]]['salary'].max()
max_marketing = db_employee[db_employee['department_id'] == db_dept[db_dept['department'] == 'marketing']['id'].iloc[0]]['salary'].max()

max_marketing-max_engineering
