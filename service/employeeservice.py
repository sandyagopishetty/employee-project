from model.department import department
from model.employee import employee


class employee_service:
    def __init__(self):
        self.emp_lst=[]

    def load_employees(self, department_service, filename = "service/employee.txt"):

        with open(filename, "r") as file:

            for line in file:
                eid, ename, esal, deptid = line.strip().split(",")
                # Find Department object
                dept = None
                for d in department_service.dept_lst:
                    if d.deptid == int(deptid):
                        dept = d
                        break

                # Create Employee with Department object
                emp = employee(
                    int(eid),
                    ename,
                    float(esal),
                    dept
                )
                self.emp_lst.append(emp)

    def create_employee(self, dept_lst):

        emp_id   = input("enter employee id:")
        emp_name = input("enter employee name:")
        emp_sal  = input("enter employee salary:")
        dept = None
        if dept_lst:
            for d in dept_lst:
                print("deptid:",d.deptid,"deptName:",d.deptname)
            user=input("do you want to select department from above list.y/n?")
            usersel=input("which department do you select from department")
            for u in dept_lst:
                if u.deptname == usersel:
                    dept=u

        else:
            dept_id  = input("enter department id:")
            dept_name = input("enter depatment name:")
            dept = department(dept_id,dept_name)
        emp = employee(emp_id,emp_name,emp_sal,dept)
        self.emp_lst.append(emp)
        print("employee added successfully")
    def update_employee_name(self):
        print("these are employee list.")
        for emp in self.emp_lst:
            print("employee id:",emp.eid,"employee name:",emp.ename)
        userinput=input("which employee id do you want to change name? ")
        changename=input("enter new name of that employee:")
        for n in self.emp_lst:
            if n.eid == userinput:
                n.ename=changename
                break
        print("updated successfully")
    def show_employees(self):
        for s in self.emp_lst:
            print(s.eid,s.ename,s.esal,s.edept.deptname)
        else:
            print("no employee is available")
    def update_employee_salary(self):
        for em in self.emp_lst:
            print("employeName:",em.ename,"employeSalary:",em.esal)
        usrinput=input("which employee salary do you want to change?")
        changesalary=input("enter new salary ")
        for sa in self.emp_lst:
            if sa.ename == usrinput:
                sa.esal = changesalary
                break
        print("updated salary successfully. ")
    def update_employee_department(self):
        for d in self.emp_lst:
            print("empId:",d.eid,"empDepartment:",d.edept.deptname)
        userdept=input("which employee department do you want to change by employee id?")
        changedept=input("enter new department")
        for cd in self.emp_lst:
            if cd.eid == userdept:
                cd.edept.deptname = changedept
                break
        print("updated successfully ")
    def delete_employee_employeeid(self):
        for s in self.emp_lst:
            print("employeeId:",s.eid,"employeeName:",s.ename)
        userip=input("which employee do you want to delete by employeeid?")
        for d in self.emp_lst:
            if d.eid == userip:
                self.emp_lst.remove(d)
                break

        print("deleted successfully")
    def show_employee_dept(self):
        user=input("which department employees do you want to see?")
        for d in self.emp_lst:
            if d.edept.deptname  == user:
                print(d.eid,d.ename,d.esal,d.edept.deptname)
    def max_sal_by_dept(self):
        userm=input("which department employee max salary do u want?")
        max_sal_emp=None
        for u in self.emp_lst:
            if u.edept.deptname == userm:
                if max_sal_emp == None or u.esal > max_sal_emp.esal:
                    max_sal_emp = u

        print(max_sal_emp.ename, max_sal_emp.esal)
    def show_All_employees_By_dept(self):
        res_dict={}
        for i in self.emp_lst:
            if i.edept.deptname in res_dict:
                res_dict[i.edept.deptname].append(i.ename)
            else:
                res_dict[i.edept.deptname]=[i.ename]
        print(res_dict)
















    def run(self, dept_lst):
       while(True):
           x = input("on employee what do you want to do\n"
                 "0. go to menu menu "
                 "1. create new employee "
                 "2. update employee name "
                 "3. update employee salary "
                 "4. update employee department "
                 "5. delete employee by employee id"
                 "6. show all employee details"
                 "7. show employees by department"
                 "8. show max employess by department"
                 "9. show all employees by department"
           )
           if x == "0":
               break
           elif x == "1":
               self.create_employee(dept_lst)
           elif x == "2":
               self.update_employee_name()
           elif x == "3":
               self.update_employee_salary()
           elif x == "4":
               self.update_employee_department()
           elif x =="5":
               self.delete_employee_employeeid()
           elif x == "6":
               self.show_employees()
           elif x == "7":
               self.show_employee_dept()
           elif x == "8":
               self.max_sal_by_dept()
           elif x == "9":
               self.show_All_employees_By_dept()

