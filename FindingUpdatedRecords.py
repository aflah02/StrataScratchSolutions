# Import your libraries
import pandas as pd

ms_employee_salary = ms_employee_salary.sort_values(by = 'salary', ascending = False)

ms_employee_salary = ms_employee_salary.drop_duplicates(['id'])

ms_employee_salary = ms_employee_salary.sort_values(by = 'id')

ms_employee_salary
