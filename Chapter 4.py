# # #Chapter 4

# # age_str = input("Сколько вам лет?")
# # age = int(age_str)
# # if age > 18:
# #     print("Проходите")
# # else:
# #     print("Вам отказано")


# x = 100

# def f():
#     print(x+1)

# f()

# a = input()
# b = input()


# try: 
#     a = int(a)
#     b = int(b)
#     print(a/b)
# except:
#     print("Error")


# def sum(x, y=99):
#     """
#     Возвращает х + у
#     :параметр х целое число
#     :параметр у целое числа
#     :вывод целая сумма
#     """
#     print(x+y)
#     return x + y

# sum(32,1)





# # Задание 1
# def sqrt(x):
#     return x ** 2

# print(sqrt(9))

# Задание 2
# def returning(str):
#     print(str)

# returning("hI, ARTEM)")


# Задание 3
# def count(a,b,c,x=10,y=15):
#     print(a+b+c+x+y)

# count(3,21,4)
# count(1,2,3,4,5)


# Задание 4
# def ostatok(x):
#     return x / 2

# def multi(x):
#     return x * 4

# count = ostatok(10)
# print(multi(count))



# # Задание 5
# def str_to_float(str):
#     """
#     Переводит флойт в стрингу
#     :принимает стрингу
#     :возвращает флоут
#     :если не флоут принимает, то кидает эксепшн
#     """
#     try:
#         return float(str)
#     except ValueError:
#         print("Sorry, you have an error")

# print(str_to_float("132.0"))
# print(str_to_float("Hello, world"))
# str_to_float()


# Задание 6