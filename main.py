# Import necessary classes
from employee import Employee
from department import Department
from project import Project
from hr_system import HRSystem
# Initialize the HR System
hr = HRSystem()
# Create employees
emp1 = Employee(1, "Ali", "Software Engineer", 15000)
emp2 = Employee(2, "Mona", "Data Scientist", 18000)
emp3 = Employee(3, "Kareem", "Project Manager", 25000)
# Add employees to HR system
hr.add_employee(emp1)
hr.add_employee(emp2)
hr.add_employee(emp3)
# Create departments
dept1 = Department(101, "Engineering")
dept2 = Department(102, "Data Science")
# Add departments to HR system
hr.add_department(dept1)
hr.add_department(dept2)
# Assign managers to departments
dept1.assign_manager(emp1.emp_id)
dept2.assign_manager(emp2.emp_id)
# Add employees to departments
dept1.add_employee(emp1.emp_id)
dept1.add_employee(emp3.emp_id)
dept2.add_employee(emp2.emp_id)
# Create projects
proj1 = Project(201, "AI Chatbot", 50000, "30-Apr-2025")
proj2 = Project(202, "E-commerce Platform", 75000, "15-May-2025")
# Add projects to HR system
hr.add_project(proj1)
hr.add_project(proj2)
# Assign employees to projects
proj1.assign_employee(emp1.emp_id)
proj1.assign_employee(emp2.emp_id)
proj2.assign_employee(emp3.emp_id)
# Employees join projects
emp1.assign_project(proj1.project_id)
emp2.assign_project(proj1.project_id)
emp3.assign_project(proj2.project_id)
# Display details
print("\n--- Employees ---")
for employee in hr.employees:
    print(employee.get_details())
print("\n--- Departments ---")
for department in hr.departments:
    print(department.get_department_details())
print("\n--- Projects ---")
for project in hr.projects:
    print(project.get_project_details())


"""Expected Output:
--- Employees ---
{'ID': 1, 'Name': 'Ali', 'Position': 'Software Engineer', 'Salary': 15000,
'Projects': [201]}
{'ID': 2, 'Name': 'Mona', 'Position': 'Data Scientist', 'Salary': 18000,
'Projects': [201]}
{'ID': 3, 'Name': 'Kareem', 'Position': 'Project Manager', 'Salary': 25000,
'Projects': [202]}
--- Departments ---
{'ID': 101, 'Name': 'Engineering', 'Manager': 1, 'Employees': [1, 3]}
{'ID': 102, 'Name': 'Data Science', 'Manager': 2, 'Employees': [2]}
--- Projects ---
{'ID': 201, 'Name': 'AI Chatbot', 'Budget': 50000, 'Deadline': '30-Apr-2025',
'Employees': [1, 2]}
{'ID': 202, 'Name': 'E-commerce Platform', 'Budget': 75000, 'Deadline': '15-
May-2025', 'Employees': [3]}"""