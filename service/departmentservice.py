from model.department import department


class department_service:
    def __init__(self):
        self.dept_lst=[]

    def load_departments(self, filename = "service/department.txt"):
        with open(filename, "r") as file:
            for line in file:
                deptid, deptname = line.strip().split(",")
                dept = department(
                    int(deptid),
                    deptname
                )
                self.dept_lst.append(dept)

    def create_department(self):
        dptid=input("enter department id:")
        dptname=input("enter department name:")
        dept=department(dptid,dptname)
        self.dept_lst.append(dept)
        print("department created successfully")
    def update_department_nameById(self):
        for d in self.dept_lst:
            print("deptId:",d.deptid,"deptName:",d.deptname)
        userip=input("which department name change by id?")
        chngedptname=input("enter new department name:")
        for dn in self.dept_lst:
            if dn.deptid == userip:
                dn.deptname=chngedptname
                break
        print("updated sucessfully")
    def delete_departmentById(self):
        for d in self.dept_lst:
            print("deptId:",d.deptid,"deptName:",d.deptname)
        usrd=input("which department do you want to delete by dept id?")
        for dn in self.dept_lst:
            if dn.deptid == usrd:
                self.dept_lst.remove(dn)
        print("deleted sucessfully.")
    def show_all_depts(self):
        for ds in self.dept_lst:
            print("deptid:",ds.deptid,"deptname:",ds.deptname)




    def run(self):
        while(True):
            y = input("on department, what do you want to do\n"
                      "0. go to main menu\n"
                      "1. create department\n"
                      "2. update department by dept id\n"
                      "3. delete department by department id\n"
                      "4. show all departments"
                      )
            if y == '0':
                break
            elif y == '1':
                self.create_department()
            elif y == '2':
                self.update_department_nameById()
            elif y == '3':
                self.delete_departmentById()
            elif y == '4':
                self.show_all_depts()