class department:
    def __init__(self,deptid,deptname):
        self.deptid=deptid
        self.deptname=deptname
    def update_deptname(self,updtdname):
        self.deptname=updtdname
    def print_department(self):
        print("deptid:",self.deptid,"deptname:",self.deptname)
