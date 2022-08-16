#Задание 1
musicians = ["Basta", "Oxxy", "Scrip", "Katil"]
# print(len(musicians))
# print(musicians)


#Задание 2
# moscow = (23.123,31.12312)
# yerevan = (12.333,56.3123)
# dilijan = (45.3123, 123.123123)

# cities = [moscow, yerevan, dilijan]

# print(cities[0])

#Задание 3
# self_dictionary = {
#     "Рост" : 172,
#     "Вес" : 66,
#     "Национальность": "Армянин"
# }

# print(self_dictionary)

#Задание 4

# input = input("Введите поисковый запрос (рост, вес или национальность)\n").capitalize()
# if input in self_dictionary:
#     print(self_dictionary[input])
# else:
#     print("Данного параметра нет в анкете")

#Задание 5
# basta = ["asds","sada","asda"]
# oxxxy = ["ds","dd"]
# scrip = ["cxz"]
# katil = ["d"]

# my_playlist = {
#     musicians[0] : basta,
#     musicians[1] : oxxxy,
#     musicians[2] : scrip,
#     musicians[3] : katil
# }

# print(my_playlist)

#Задание 6

list = [1,2,3,4,5,6,6,6,6,6,7,8,1,2]
set = set(list)
print(set.union({1,2,3,4,12,3,123,3,12,312,312,3,13}))