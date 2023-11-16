from Model import Employee, Job, Assignment, Project
from db import session
from datetime import datetime

'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''
# employees = session.query(Employee).all()
# employees = session.query(Employee).filter(Employee.emp_num > 101).all()
# for employee in employees:
#     print(employee.emp_lname, employee.emp_fname, employee.emp_hiredate)


'''
Join employee with job
'''
# employees = session.query(Employee, Job).filter(Employee.job_code == Job.job_code).all()
# for employee in employees:
#     print(employee.Employee.emp_lname, employee.Employee.emp_fname, employee.Job.job_description)

'''
Insert new employee record
'''
# employee = Employee(emp_num=999, emp_lname="Doe", emp_fname="John", emp_initial="D", emp_hiredate="2020-01-01")
# session.add(employee)
# session.commit()

'''
Update employee record

'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# employee.job_code = 510
# session.commit()

'''
Delete employee record
'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# session.delete(employee)
# session.commit()

'''
Query assigment where assign_date is larger than 2010-01-01
'''

'''
1. add new employee record to employee table with id = 168, 
firstname = 'John', lastname = 'Doe', initials = 'JD', 
job = 'Programmer', hire_date = today's date.
'''

# today = datetime.now()

# employee = Employee(emp_num = 168, emp_fname = "John", emp_lname = "Doe", emp_initial = "JD", job_code = 500, emp_hiredate = today)
# session.add(employee)
# session.commit()

'''
2. query the new created employee (id=168) from employee table, 
with information of employee id, firstname, lastname, initials, 
job description (join with job), charge per hour (join with job) 
and hire_date.
'''

# employees = session.query(Employee, Job).filter(Employee.job_code == Job.job_code).filter(Employee.emp_num == 168).all()

# for employee in employees:
#     print(employee.Employee.emp_num, employee.Employee.emp_fname, employee.Employee.emp_lname, employee.Employee.emp_initial, employee.Job.job_description, employee.Job.job_chg_hour, employee.Employee.emp_hiredate)
    
'''
3. update the new created employee (id=168) job, from 'Programmer' to 
'Database Designer'.
'''

# employee = session.query(Employee).filter(Employee.emp_num == 168).first()
# employee.job_code = 502
# session.commit()

'''
4. query all project that has "Programmer" assigned to, 
with information of project id, project name and program manager 
(join with employee).
'''

# projects = session.query(Project, Employee).filter(Project.emp_num == Employee.emp_num).filter(Employee.job_code == 500).all()

# for project in projects:
#     print(project.Project.proj_num, project.Project.proj_name, project.Employee.emp_fname, project.Employee.emp_lname)

'''
5. delete the new created employee (id=168) from employee table.
'''

# employee = session.query(Employee).filter(Employee.emp_num == 168).first()
# session.delete(employee)
# session.commit()