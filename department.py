class Department:
    def __init__(self,dept_id, name):
        self.__name= name
        self.__dept_id= dept_id
        self.__manager = None
        self.__employees = []

    def assign_manager(self,  manager_id):
        self.__manager = manager_id

    def add_employee(self, emp_id):
        self.__employees.append(emp_id)

    def remove_employee(self, emp_id):
        for i in range(len(self.__employees)):
            if emp_id == self.__employees[i]:
                self.__employees.pop(emp_id)

    def get_department_details(self):
        #return f" The department Name-ID: {self.__name} - {self.__dept_id} \n Department Manager: {self.__manager} \n Employees of the department: {self.__employees} "
        return f" ID: {self.__dept_id} , Name: {self.__name} , Manager: {self.__manager} , Employees: {self.__employees} "


