class Project:
    def __init__(self, project_id, name,  budget, deadline):
        self.project_id = project_id
        self.__name= name
        self.__budget= budget
        self.__deadline= deadline
        self.__employess=[]

    def assign_employee(self, emp_id):
        self.__employess.append(emp_id)

    def remove_employee(self, emp_id):
        for i in range(len(self.__employess)):
            if emp_id == self.__employess[i]:
                self.__employess.pop(i)

    def update_budget(self, budget=None):
        if budget:
            self.__budget = budget

    def update_deadline(self, deadline=None):
        if deadline:
            self.__deadline = deadline

    def get_project_details(self):
        return f" ID: {self.project_id}, name: {self.__name}, budget: {self.__budget} , deadline: {self.__deadline} , project employees: {self.__employess}"
