# a=22
# b=18
# sum=a+b
# print(sum)

# side=int(input("Enter the number:"))
# area=side*side
# print("area of square:",area)

# num1=float(input("enter the number:"))
# num2=float(input("enter the number:"))
# sum=num1+num2
# avg=sum/2
# print("Average of this numbers:",avg)


# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# if a>=b:
#     print("TRUE")
# else:
#     print("FALSE")


# a=int(input("enter the number:"))
# if (a%2==0):
#     print("the number is even")
# else:
#     print("it is odd ")

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))

# if(a>b and a>c):
#     print("a is greatesst")
# elif(b>c) :
#     print("b is greatest")
# else:
#     print("c is greatest")

# movies=[]
# movies.append("kgf")
# movies.append("kantara")
# movies.append("toxic")
# movies.append("kd")

# print(movies)

# list=["1","2","3","2","1"]
# copy_list=list.copy()
# copy_list.reverse()
# if (copy_list==list):
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


# grades=["C","D","A","B","B","A"]
# x=grades.count("A")

# print(x)

# list=[]
# list.append("C")
# list.append("D")
# list.append("A")
# list.append("B")
# list.append("B")
# list.append("A")

# list.sort()
# print(list)

# dict={
#     "table":"a piece of furniture",
#     "cat":"a small animal"
# }

# print(list(dict.items()))

# subjects={
#     "python","java","c++","python","java","c"
# }
# print(subjects)

# dict={}

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))

# dict.update({"phy":a})
# dict.update({"chem":b})
# dict.update({"maths":c})

# print(dict)

# set={"9","9.0"}
# print(set)

# i=0
# while i<=100:
#     print(i)
#     i+=1

# i=100
# while i>=1:
#     print(i)
#     i-=1


# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1

# num=(1,4,9,16,25,36,49,64,81,100)

# x=81

# i=0
# while i<len(num):
#     if(num[i]==x):
#         print("element found at index:",i)
#     i+=1
        
# i=0
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1

# i=1
# while i<=5:
#     if(i==4):
#         i+=1
#         continue
#     print(i)
#     i+=1

# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# for val in list:
#     print(list[i])
#     i+=1


# list=[1,4,9,16,25,36,49,64,81,100]

# x=25
# i=0
# for val in list:
#     if(val==x):
#         print("elements found at index:",i)
#     i+=1

# i=0
# for i in range(1,101):
#     print(i)
#     i+=1

# i=100
# for i in range(100,0,-1):
#     print(i)
#     i-=1
        
# n=int(input("enter the number:"))
# for i in range(1,11):
#     print(n*i)

# n=3
# sum=0
# i=0
# while i<=n:
#     sum+=i
#     i+=1
# print("sum of the numbers:",sum)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)    


# teams=["portugal","argentina","france","spain"]

# def print_list(list):
#     print(len(list))

# print_list(teams)


# teams=["portugal","argentina","france","spain"]
# def print_list(list):
#     for items in teams:
#         print(items,end=" ")

# print_list(teams)


# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# cal_fact(5)    


# def converter(usd_value):
#     inr_value=usd_value*83
#     print(usd_value,"USD=",inr_value,"INR")

# converter(5)


# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)

# factorial=fact(5)
# print(factorial)    


# def cal_sum(n):
#     if (n==0):
#         return 0
#     else:
#         return cal_sum(n-1) + n
    
# sum=cal_sum(6)
# print(sum)


# teams=["portugal","argentina","france","spain"]

# def print_list(list,i=0):
#     if(i==len(list)):
#         return
#     print(list[i])
#     print_list(list,i+1)

# print_list(teams)

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning python\nits is so much intersting.\nlets go")
   

# with open("practice.txt","r") as f:
#     data=f.read()
#     new_data=data.replace("python","java")
    

# with open("practice.txt","w") as f:
#     f.write(new_data


# oops
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"your average marks is:",sum/3)

# s1=Student("Manjunath",[99,98,99])
# s2=Student("Praman",[99,97,96])

# print(s1.name)
# print(s1.marks)
# s1.get_avg()



# class Account:
#     def __init__(self,acc,bal):
#         self.account_no = acc
#         self.balance = bal
    
#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount, "was debited..")
#         print("total balance:",self.get_balance())

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount," was credited..")
#         print("total balance:",self.get_balance())

#     def get_balance(self):
#         return self.balance
    
    
# acco1 = Account(182294,10000)
# # print(acco1.balance)
# # print(acco1.account_no)
# acco1.debit(5000)
# acco1.credit(10000)
# acco1.debit(3400)

# with open("practice.txt","w") as f:
#     f.write("i am legend\ni am going to achieve something great\ni will be succesful person in my bloodline\ni am the best.")


# with open("practice.txt","r") as f:
#     data=f.read()
#     new_txt=data.replace("legend","Supreme")
#     print(new_txt)

# with open("practice.txt","w") as f:
#     f.write(new_txt)

# word="succesful"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word) !=-1):
#         print("found")
#     else:
#         print("not found")


# def check_for_line():
#     data=True
#     word="Supreme"
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print("found at line:",line_no)
#                 return
#             line_no+=1
#     return -1
  
# check_for_line()    

# with open("num.txt","r") as f:
#     data=f.read()

# count=0    
# nums=data.split(",")
# for val in nums:
#     if(int(val)%2==0):
#         count+=1

# print(count)
    
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def cal_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("the avg of the student's marks is:",sum/3)

# s1=Student("Manjunath",[99,100,99])
# print(s1.name)
# print(s1.marks)
# s1.cal_avg()


# class Account:
#     def __init__(self,bal,acc_no):
#         self.balance=bal
#         self.account_no=acc_no

#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount, "is debited")
#         print("total balance:",self.get_balance())

#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount, "is credited..")
#         print("total balance:",self.get_balance())
    
    
#     def get_balance(self):
#         return self.balance
    

# acc=Account(16000,182294)
# print(acc.account_no)
# acc.debit(14500)

        
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
    
#     def cal_area(self):
#         area=22/7 * self.radius ** 2
#         print("the area of circle is:",area)

#     def cal_perimeter(self):
#         perimeter=2 * 22/7 * self.radius
#         print("the area of perimeter is:",perimeter)
    
# a1=circle(10)
# a1.cal_area()
# a1.cal_perimeter()


# class employee:
#     def __init__(self,role,dept,slry):
#         self.role=role
#         self.dept=dept
#         self.slry=slry

#     def showdetails(self):
#         print("Role=",self.role)        
#         print("Department=",self.dept)
#         print("salary=",self.slry)

# class engineer(employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","Cybersecurity",200000)

# e1=engineer("Manjunath",25)
# print(e1.name)
# e1.showdetails()



# class order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price

#     def __gt__(self,odr2):
#         return self.price > odr2.price
    
# odr1=order("chips",20)
# odr2=order("tea",15)

# print(odr1 > odr2)


# import random

# target=random.randint(1,100)

# while True:
#     user_choice=input("Guess any number or Quit:")
#     if(user_choice=="quit"):
#         break
    
#     user_choice=int(user_choice)
#     if(user_choice==target):
#         print("SUPERB!! ITS A CORRECT GUESS")
#         break

#     elif(user_choice<target):
#         print("the guessed number is too small ,Guess the big number!!")
#     elif(user_choice>target):
#         print("the guessed number is bigger one,Guess smaller one!!")

# print("-----GAME OVER-----")



import random
import string

pass_len=8
char_val=string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(pass_len):
    password+= random.choice(char_val)


print("the random password is generated:",password)








