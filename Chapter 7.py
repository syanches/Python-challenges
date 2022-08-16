# Задание 1
# list = ["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневники вампира"]
# for movie in list:
#     print(movie)

# Задание 2
# for number in range(25,51):
#     print(number)


# # Задание 3
# for i, movie in enumerate(list):
#     print("{} index for {}".format(i, movie))

# # Задание 4
# guesser = ["1","3","7","9"]
# while True:
#     guess = input("Отгадай число от 0 до 10\nВведи х для выхода\n")
#     if guess == 'x':
#         break
#     else:
#         if guess in guesser:
#             print("Молодец")
#             break
#         else:
#             print("Попробуй еще")


# Задание 5
list = [8, 19, 148, 4]
list_two = [9, 1, 33, 83]
list_results = []

for i in list:
    for j in list_two:
        list_results.append(i*j)

print(list_results)