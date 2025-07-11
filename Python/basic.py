print("hellow")
# a ="hello"
# num= 10 

# print = 22
# print(print)pyth
# name = "Ritik kumar "
# print(name)
# print("name dtypes:-",type(name))
# print("len of name:-",len(name))
# ### indexing
# print(name [0])
# print(name[2])
# print(name[len(name)-1])

### slicing in python 

# name = "ritik"
# print(name[0:3])

#how work 

###operation 
# name = "ritik"
# last ="kumawat"
# upper_case =name.upper()###upper function ka used upper case a liye use krte ha 
# print(upper_case)
# lower_last_name=last.lower()
# print(lower_last_name)
# print(name.count("r"))

# name = "ritik"
# last =" kumawat"
# # print(name.title())
# # print(name.capitalize())
# print(name+last)
#list 
# lst =[1,2,3,4,5,6,7,"rohit",2.3,]  ### >>>>>>>list 
# ### array or list >>>>>>>>
# #mutable 
# #duplicated values 
# ### Herto 
# # order 
# # array  >>>>>> lst = [1,2,3,4,5,6]
# #array 
# # print("my first list:-",lst)
# # print("len of list:-",len(lst))
# # print("type of list:-",type(lst))
# print(lst[0])
# print(lst[5])
# print(lst[0:5])
# lst =[1,2,2,3,4,5,6,7,"rohit",2.3,]  ### >>>>>>>list 
# lst.pop()
# print(lst)
# lst.append(100)
# print(lst)
# lst.insert(0,1000)
# print(lst)
# copy_lst =lst.copy()
# print(copy_lst)
# lst.reverse()
# lst.remove(2,3)
# print(lst)
# lst.sort()
# lst = [1,2,2,3,4,5,6,7,2.3,]  ### >>>>>>>list 
# print(lst.count(2))
# print(lst)
# >>>>>>>>>>>>>>>tuple<<<<<<<<<<<<<<<<<<<
#tuple =
# tpl = (1,2,3,5,"ritik",2.3)
# print(" my first tuple :-",tpl)
# print("len of tuple :-",len(tpl))
# print("type of tuple :-",type(tpl))
 
# print(tpl[0])
# print(tpl[2])
# print(tpl[0:6])

#build
# a=1,2,58,5,58,5,5,85,2
# print(a) #>>>>>>>>1,2,58,5,58,5,5,85,2
# print(type(a))  ## <class 'tuple' >
# print(len(a))  ##9



# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)
#print(d)

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# tpl =(1,2,58,2,8,2,8)
# print(" max of tpl " ,max(tpl))
# print(" min of tpl ",min(tpl))
# print(" sum of tpl " ,sum(tpl))
# my_dict = {
# #     "name":"rohit",  ## name, class , roll number and address >>>> keys 
# #     "class":"2nd year",  ## rohit , 2nd year ,21EAMC5055 and jaipur .>>>>> values 
#     "roll number":"21EAYC5055",
#     "adddres":"jaipur", ####>>>>> "name": "rohit" item 
# }

# print("my first dict :-",my_dict)
# print("len of dict :-",len(my_dict))
# print("tyoe of dict :-",type(my_dict))

# print(my_dict['name'])
# print(my_dict['class'])
# print(my_dict['roll number'])
# print(my_dict['adddres'])

# my_dict['adddres']="new jaipur"
# print(my_dict)



# my_dict = {
#     "name":"rohit", ### name, class , roll number and address >>>> keys 
#     "class":"2nd year", #### rohit , 2nd year ,21EAMC5055 and jaipur .>>>>> values 
#     "roll number":"21EAYC5055",
#     "adddres":"jaipur","name":"rohit" ####>>>>>> "name": "rohit" item 
# }
# # my_dict['branch']="cse"
# print(my_dict)

#access element 6 

# lst = [1,2,3,4,[6],7]
# print("list",lst)
# nested = lst[4]
# print("nested list", nested )
# six = nested[0]
# print("accessed element",six)


 
#  task >>>>> update function ka use krke
# get function >>>>> 5 example or [] 

#student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
    # score_alice = student_scores.get("Alice")
    # print(f"Alice's score: {score_alice}")

# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_dave = student_scores.get("Dave")
# print(f"Dave's score: {score_dave}") # Output will be None

# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_eve = student_scores.get("Eve", 0)
# print(f"Eve's score: {score_eve}") # Output will be 0

# config = {"debug_mode": True, "port": 8080}
# is_logging_enabled = config.get("enable_logging", False)
# print(f"Logging enabled: {is_logging_enabled}")

# data = {
#         "user_info": {
#             "name": "Jane Doe",
#             "contact": {"email": "jane@example.com"}
#         }
#     }
# user_email = data.get("user_info", {}).get("contact", {}).get("email")
# print(f"User email: {user_email}")
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.itemss())

# # copy_dict =my_dict.copy()
# # print(copy_dict)

# my_dict.clear()
# print(my_dict)
 
# a =input("enter a number")
# b= input("enter second number")
# print(a*b)
# print(type(a))
# print(type(a))

#type casting 
# a= int(input("enter a number"))
# b= int(input("enter second number"))
# print(a*b)

# lst = [1,2,6,8,5,58]
# print("this is my list :-",lst)
# print("type of list :-",type(lst))
# tpl = tuple(lst)
# print("this is my tuple :-",tpl)
# print("type of tuple :-",type(tpl))


# >>>>>>>>>>>>>>>> SET >>>>>>>>>>>>>>>>>>>

# my_set =
# list 
# tuple
# set
# dict

# my_set ={1,2,3,5,41,6,1,5}
# print("this is my set :-",my_set)
# print("len of  my set :-",len(my_set))
# print("type of set :-",type(my_set))


# # task >>>>>
# # my_set.union()
# # my_set.intersection()
# # my_set.difference()


# lst =list(my_set)

# lst.append(1000)
# print(set(lst))

### operator 



