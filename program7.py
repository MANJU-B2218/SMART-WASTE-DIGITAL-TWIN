# # with open("practice.txt","w") as f:
# #     f.write("i am legend\ni am learning python and\ni will become pro\n")
# #     f.write("i will achieve great thing\nand bcome great succesful man")


# # with open("practice.txt","r") as f:
# #     data=f.read()

# # new_data=data.replace("python","java")
# # print(new_data)

# # with open("practice.txt","w") as f:
# #     f.write(new_data)

# # word="succesful"
# # with open("practice.txt","r") as f:
# #     data=f.read()

# #     if(data.find(word) !=-1):
# #         print("found")
# #     else:
# #         print("not")

# def check_line():
#     word="succesful"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1

# two dice probalities
# for i in range(1,7):
#     for j in range(1,7):
#         print("(",i," ,",j,")")
#         j+=1
#     i+=1 

# for i in range(1,6):
#     j=1
#     while(j<=i):
#         print("*",end=" ")
#         j+=1
#     i+=1
#     print()
