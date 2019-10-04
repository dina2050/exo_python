# n=5
# x=4
# y=0
# spaces=""
# stars="*"
# for i in range(n):
#     for j in range (x, x-1):
#             for k in range (y,2*y+1):
#                     print("/n"+"stars"+"spaces")
        
# n=5
# stars=" "
# for i in range(n):
#     for nb_spaces in range(n-i-1):
#         stars+=" "
#         for nb_stars in range (2*i-1):
#             stars+="*"
#             stars=stars+"/n"
#             print(stars)


# for i in range(100):
#         if  i=0 i=i+2:
#                 print(i, "pair")
# else:
#         print(i, "impair")

# 
#for i in range(10):
 #   print (i)
  #  for j in range(0,10):
   #         print(str(i) +"x"+str(j)+"="+str(i*j))
        
# myInt_list = [10,50,30,45,6,45,855,556,56565,5445,458562,56456,4845] 
# myString_list= ["vie", "belle", "La"]
# myBool_list = [True, False, True, True, True, False, False]
#print (len (myInt_list))
#print (len (myString_list))
#print (len(myBool_list))
# myInt_list[0]=42
# print (myInt_list)
# myString_list[1]="compliqué"
# print(myString_list)
# myString_list.append("est")
# print (myString_list)
# for i in range(len (myInt_list)):
#      print (myInt_list[i])   
# for integer in (myInt_list):
#         print(integer)
# for i in range (len (len(myInt_list)-1,-1,-1):
#     print (i)
    
# for i in range (len(myInt_list)):
#     print(myInt_list[len(myInt_list) -i -1])

# maliste = [10,20,3,4,2,7]
# myNumber = 6
# cpt=0
# for i in range(len(maliste)-1):
#     if maliste[i]<myNumber:
#         cpt=cpt+1
# print(cpt)

    # if maliste[i]<maliste[i+1]:
    #     print("True")
    # else: 
    #     print("False")
     


# maliste = [10,20,3,4,2,7]
# n=10
# for i in range(len(maliste)):
#     if n==maliste[i]:
#         print(True,i)

# maliste = [3,5,8,53,42]
# n=3
# for i in range(len(maliste)):
#     if maliste[i]%n==0:
#         print(str(maliste[i])+"est"+"divisible"+"par"+str(n))
#     else:
#         print(str(maliste[i])+"est"+"nondivisible"+"par"+str(n))
       
# maliste=[]
# n=10
# import random
# for i in range(n):
#     maliste.append(random.randint(1,50))
# print(maliste)
# l1 = [2, 4, 9, 10, 5, 12]
# l2 = []
# for i in range(len(l1)):
#     if l1[i] % 2 == 0:
#         print(l2.append(l1[i]))       #[2,4,10,12]
#         print(l1.remove(l1[i]))       #[9,5]


# n = "exercise"
# print(len(n))


# n="exercise"
# n[6]=='c'
# print(n[6])


# n="exercise"
# maliste = ['e' ,'x', 'e', 'r', 'c', 'i', 's', 'e']
# maliste[6]='c'

# print(maliste)

# n="exercise"
# n[0][]==str('c')
# print(n)

# n='exercise'
# x= list(n)
# x[0]=="b"
# print(x)

# n="radar"
# n=list(n)
# for i in range (len(n)):
#     if n[i]==n[len(n)-i-1]:
#         i=i+1
#         print("oui")
    



# n="radar"
# n=list(n)
# x=""
# for i in range (len(n)):        
#     x=i+x
#     if n==x:
#         print("yes")

# alpha="abcdefghijklmnopqrstuvwxyz"
# word="yzf"
# new_word=""
# a=3
# for i in range (len(word)):
#     the_letter = word[i]
#     position_in_alpha = alpha.index(the_letter)
#     new_position_in_alpha = (position_in_alpha + a) % 26
#     new_word += alpha[new_position_in_alpha]
# print(new_word)
        
<<<<<<< HEAD
# r = int(input ())
# h = int(input())
# pi=3.14
# V = ""
# V=int(h*r*r*pi)*1/3
# print(V)
# sum = 0
# a = int(input("enter a number:"))
# cpt = 0
# b=0
# while a!=0:
#     sum += a
#     cpt=cpt+1
#     if a>100:
#         b=b+1
#     a = int(input("enter a number:"))

# print(sum)
# print(cpt)
# print(b)

# n = int(input())
# if n % 2 == 0:
#     print("pair")
# else:
#     print("impair")

# n = int(input())
# cpt = 0
# if n % 2 == 0:
#     while n % 2 == 0:
#         n = n / 2
#         cpt = cpt + 1
#     print(cpt)
# else:
#     print("votre chiffre n'est pas divisible par 2")
# import random
# bla = random.randint(1,100)
# num = int(input())
# while num != bla:
#     if num > bla:
#         print("trop grand")
#     elif num < bla:
#         print("trop petit")
#     num = int(input())

# maliste = [10,15,20,8,15]
# sum = 0
# max_element = maliste[0]
# min_element = maliste[0]
# for i in range (len(maliste)):
#     if maliste[i]>max_element:
#         max_element = maliste[i]
#     elif  maliste[i]< min_element:
#         min_element =maliste[i]
#     sum = sum + maliste[i]
# print(max_element)
# print(min_element)
# print(sum)

# maliste = []
# n = 10
# import random
# for i in range(n):
#     maliste.append(random.randint(0,500))
# for i in range(n):
#     for j in range(n):
#         if maliste[j]  == maliste[i] and i != j:
#             print("identique")

# import random
# L = [1, 4, 5, 3, 7, 12, 4]
# for i in range(int(len(L)/2)):
#   temp = L[i]
#   L[i] = L[len(L)-i - 1]
#   L[len(L)-i - 1] = temp
# print(L)
=======
        
        
>>>>>>> 0961985bdfe6a82c0f1405dafeeb97fe1c5fc480
