import mysql.connector as c
con=c.connect(host="localhost",user="root",password="Subhash15@",database="office")
class office:
    def __init__(self,__emp_id,emp_name):
        self.__emp_id=__emp_id
        self.emp_name=emp_name
        self.__current_password="hudco@2022"
    def password(self,__password):
        self.__password=__password
        if (self.__password==self.__current_password):
            return True
        else:
            return False
    def new_pass(self,__new_pass):
        self.__new_pass=__new_pass
        self.__current_pass=self.__new_pass
    def income(self,__account_no,balance_salary,credit_ammount,bonus):
        self.__account_no=__account_no
        self.balance_salary=balance_salary
        self.credit_ammount=credit_ammount
        self.bonus=bonus
        self.balance_salary+=self.credit_ammount
        self.balance_salary+=self.bonus
        print(self.balance_salary, "total salary")
cursor=con.cursor()
while True:
    __emp_id=int(input("enter the your emp id:"))
    emp_name=input("enter your name")
    emp=office(__emp_id,emp_name)
    __password=input("enter your password:")
    if emp.password(__password):
        print("correct password")
        __account_no=int(input("enter the account no. :"))
        balance_salary=float(input("enter the balance in the account:"))
        credit_ammount=float(input("enter the ammount to be credited:"))
        bonus=float(input("enter bonus if any:"))
        emp.income(__account_no,balance_salary,credit_ammount,bonus)
    else:
        print("incorrect password")
        code=int(input("enter the code:"))
        if (code==2022):
            reset_choice=input("forget password ? (yes/no):").strip().lower()
            if reset_choice=="yes":
                __new_pass=input("enter new password")
                emp.new_pass(__new_pass)
                __emp_id=int(input("enter the your emp id:"))
                emp_name=input("enter your name")
                emp=office(__emp_id,emp_name)
                __password=input("enter your password:")
                emp.password(__password)
                __account_no=int(input("enter the account no. :"))
                balance_salary=float(input("enter the balance in the account:"))
                credit_ammount=float(input("enter the ammount to be credited:"))
                bonus=float(input("enter bonus if any:"))
                emp.income(__account_no,balance_salary,credit_ammount,bonus)
            else:
                print("can'not access")
        else:
            print("access denied")
    query="insert into employee values({},'{}','{}')".format(__emp_id,emp_name,__password)
    cursor.execute(query)
    con.commit()
    query2="insert into salary values({},{},{},{},{})".format(__account_no,__emp_id,credit_ammount,bonus,balance_salary)
    cursor.execute(query2)
    con.commit()
    x=int(input("1--->Enter More\n2--->Exit\n enter your choice"))
    if x==2:
          break
          
        
        
         
    
    
