# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))

# if(a>b and a>c):
#     print("a is gretatest among all:",a)
# elif(b>c):
#     print("b is the greatest among all:",b)
# else:
#     print("c is greatest amon all",c)

# list=["m","a","d","a","m"]

# new_list=list.copy()
# new_list.reverse()

# if(new_list==list):
#     print("it is palindrome")
# else:
#     print("not a palindrome")

# list=["A","C","B","B","A","A","C"]
# X=list.count("A")

# print(X)

# list=[]

# list.append("A")
# list.append("C")
# list.append("D")
# list.append("A")
# list.append("B")

# list.sort()
# print(list)


# set={
#     "python","java","javascript","c++","python","java"
# }

# print(set)


# marks={}

# x=int(input("Enter the marks:"))
# y=int(input("Enter the marks:"))
# z=int(input("Enter the marks:"))


# marks.update({"Physics":x})
# marks.update({"chemitry":y})
# marks.update({"maths":z})

# print(marks)

# dict={"9",9.0}
# print(dict)

# num=100
# while num>=100:
#     print(num)
#     num-=1


# n=int(input("enter the number:"))

# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# list=[1,4,6,7,8,9,0,1,3,5,6,7]

# i=0
# while(i<len(list)):
#     print(list[i])
#     i+=1

# tuple=(1,4,6,7,8,9,0,1,3,5,6,7)

# x=5
# i=0
# while i<len(tuple):
#     if(tuple[i]==x):
#         print("the number found at the index:",i)
#         i+=1


# list=[1,4,6,7,8,9,0,1,3,5,6,7]

# i=0
# for val in list:
#     print(list[i]) 
#     i+=1

# list=[25,67,89,78,45,35,22,18]

# x=89

# i=0
# for val in list:
#     if(list[i]==x):
#         print("element found at index:",i)
#     i+=1

# print("END")

# i=0
# for i in range(1,101):
#     print(i)
    

# n=7

# sum=0
# i=0
# while i<=n:
#     sum+=i
#     i+=1
# print("the sum of n numbers:",sum)


# n=5
# sum=0
# for i in range(n+1):
#     sum+=i
# print("sum of numbers:",sum)

# names=["manju","ronaldo","virat"]

# def print_list(list):
#     print(len(list))

# print_list(names)
    

# names=["manju","ronaldo","virat"]

# def print_list(list):
#      for item in list:
#           print(item,end=" ")

# print_list(names)

# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print("factorial of",n,"is:",fact)


# cal_fact(5)


# def converter(usd_value):
#     inr_value=usd_value * 83
#     print(usd_value,"USD=",inr_value,"INR")

# converter(5)


# def show(n):
#     if(n==0):
#         return 
#     print(n)
#     show(n-1)
# show(5)


# def fact(n):
#     if(n==0 or n==1 ):
#         return 1
#     else:
#         return n * fact(n-1) 

# factorial=fact(4)
# print(factorial)


# def cal_sum(n):
#     if(n==0):
#         return 0
#     else:
#         return n + cal_sum(n-1)

# sum=cal_sum(5)
# print(sum)

# names=["manju","ronaldo","virat"]

# def print_list(list,i):
#     if(i==len(list)):
#         return
#     print(list[i])
#     print_list(list,i+1)
        
# print_list(names,0)


# with open("pract.txt","w") as f:
#     f.write("Hi everyone\ni am manjunath\nand i am legend\ni am going to be succesful person")

# with open("pract.txt","r") as f:
#     data=f.read()

#     new_txt=data.replace("manjunath","virat")
#     print(new_txt)

# with open("pract.txt","w") as f:
#     f.write(new_txt)


# word="legend"
# def check_word():
#     with open("pract.txt","r") as f:
#         data=f.read()
#     if(data.find(word) !=-1):
#         print("found")
#     else:
#         print("not found")

# check_word()

# def check_line():
#     data=True
#     word="legend"
#     line_no=1
#     with open("pract.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print("found in the line:",line_no)
#                 return
#             line_no+=1

#     return -1  

# check_line() 

# count=0
# with open("pract.txt","r") as f:
#     data=f.read()

#     num=data.split(",")
#     for val in num:
#         if(int(val)%2==0):
#             count+=1
# print(count)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def cal_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("the avg of the student",self.name,"is:",sum/3)

        

# s1=student("Manjunath",[99,98,100])
# s1.cal_avg()




    


