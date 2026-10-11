class employee:
    def __init__(self,eid,ename,esal,edept):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.edept=edept
    def update_ename(self,uptename):
        self.ename=uptename
    def update_esal(self,uptesal):
        self.esal=uptesal
