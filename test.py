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


# Цель тестового задания
# Определить возможную динамику самообучения кандидата. А так же глубину понимания кода, реализующего тестовое задание.

# Задание
# Написать тестовое web-приложение по управлению электронной библиотекой:

# 1. Редактирование (доступно авторизованному пользователю при наличии аутентификации):

# Управление списком книг: добавить / удалить / редактировать книгу.
# Управление списком авторов: добавить / удалить / редактировать автора.
# Запись о книге содержит следующие данные: ID, Название.
# Запись об авторе содержит следующие данные: ID, Имя.
# Свзязь между книгами и авторами — многие ко многим.
# 2. Поиск книг по названию либо автору (доступно анонимному пользователю при наличии аутентификации).

# 3. Аутентификации и авторизация (по желанию кандидата).

# Технологии, которые должны быть задействованы:

# Flask
# SQLAlchemy (Declarative)
# SQLite (встроенный в приложение)
# Jinja2 Templates
# WTForms
# jQuery (желательно, но возможно использование альтернативных решений)
# Список может быть расширен по усмотрению кандидата, но с обязательным использованием технологий, перечисленных выше.

# Дополнительные требования
# Список дополнительных требований следующий:

# 1. Код проекта должен быть доступен на сервисе github.org или bitbucket.org.

# 2. Проект должен содержать SQL-скрипты для развертывания базы данных и наполнения ее тестовыми данными.

# 3. Пользовательские данные должны валидироваться перед сохранением в БД.

# Дополнительные знания
# Дополнительные знания, необходимые при защите проекта:

# HTTP
# WSGI
# SQL, Transactions, Transaction Isolation Levels
# SQLAlchemy
# Уязвимости веб-сайтов
# User Experience 
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
   List=[1,2,1]
   for i in range (len(List)):
       if List[0]==List[i]:
            return True
       if List[0]!=List[i]:
           return False