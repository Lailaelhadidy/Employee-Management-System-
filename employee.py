class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.__name= name
        self.emp_id= emp_id
        self.__position= position
        self.__salary= salary
        self.__projects= []

    def update_info(self, name=None, position=None, salary=None):
        if name:
            self.__name = name
        if position:
            self.__position = position
        if salary:
            self.__salary = salary

    def assign_project(self, project_id):
        self.__projects.append(project_id)

    def remove_project(self, project_id):
        if project_id in self.__projects:  #3ways will test all
            self.__projects.pop(project_id)

        """for i in range(len(self.__projects)): #parameter was used
            if project_id == self.__projects[i]:
                self.__projects.pop(project_id)
                
                    for project_id in self.__projects:
            if project_id:
                self.__projects.pop(project_id)
"""

    def get_details(self):
        return f" [ ID: {self.emp_id} , name: {self.__name} , Position: {self.__position} , Salary: {self.__salary} , projects: {self.__projects} ]"


