from service.departmentservice import department_service
from service.employeeservice import employee_service


class executor_service:
    def __init__(self):
        self.emp_service=employee_service()
        self.dept_service= department_service()
        self.dept_service.load_departments()
        self.emp_service.load_employees(self.dept_service)


    def run(self):
        while(True):
            main_input = input("welcome what do you want to do\n"
                  "0. exit "
                  "1. Employee "
                  "2. Department \n")
            if main_input == "0":
                print("thank you")
                break

            elif main_input == "1":
                self.emp_service.run(self.dept_service.dept_lst)
            elif main_input == "2":
                self.dept_service.run()


