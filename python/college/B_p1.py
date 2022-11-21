class emp:
    def __init__(self):
        self.emp=[]
        self.n=0
    def getemp(self):
        self.n=int(input("Enter how many employees: "))
        for i in range(self.n):
            self.emp.append(int(input("\nEnter ID: ")))
            self.emp.append(input("Enter Name: "))
            self.emp.append(int(input("Enter Age: ")))
            self.emp.append(input("Enter Designation: "))
            self.emp.append(input("Enter Department: "))
            self.emp.append(int(input("Enter Salary: ")))
    def disemp(self):
        print("---EMPLOYEE DETAILS---")
        for i in range(0,len(self.emp),6):
            print("Employee ID:",self.emp[i])
            print("Employee Name:",self.emp[i+1])
            print("Employee Age:",self.emp[i+2])
            print("Employee Designation:",self.emp[i+3])
            print("Employee Department:",self.emp[i+4])
            print("Employee Salary:",self.emp[i+5])
            print("----------------------")
    def searchemp(self):
        flag=0
        empNo=int(input("Enter Employee ID to Search: "))
        for i in range(0,len(self.emp),6):
            if self.emp[i]==empNo:
                print("The Entered Employee ID ",empNo," is Found.")
                print("Employee ID:",self.emp[i])
                print("Employee Name:",self.emp[i+1])
                print("Employee Age:",self.emp[i+2])
                print("Employee Designation:",self.emp[i+3])
                print("Employee Department:",self.emp[i+4])
                print("Employee Salary:",self.emp[i+5])
                flag=1
                break
            if flag==0:
                print("No Such Employee Found.")
e=emp()
e.getemp()
e.disemp()
e.searchemp()