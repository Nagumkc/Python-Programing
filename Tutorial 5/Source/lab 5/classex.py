class classex:
  "this is example of employee class"
  empcnt=0
  def __init__(self,ename,sal):
      self.ename=ename
      self.sal=sal
      classex.empcnt+=1

  def display(self):
      print("name:",self.ename,"salary:",self.sal)

class manager(classex):
    def __init__(self,n,s):
        classex.__init__(self,n,s)

emplpoyee1=classex("nag",1000)
emplpoyee2=classex("revanth",1500)
emplpoyee3=classex("dev",2000)
emplpoyee4=manager("syed",3000)
emplpoyee4.display()
print("total employees", classex.empcnt)
