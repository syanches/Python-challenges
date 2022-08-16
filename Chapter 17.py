import re 

# l = "Красивое лучше, чем уродливое"

# matches = re.findall("красивое", l, re.IGNORECASE)

# print(matches)

# zen = """ Хотя никогда зачастую лучше, чем прямо сейчас.
# Если реализацию сложно объяснить — идея плоха.
# Если реализацию легко объяснить — идея, возможно, хороша.
# Пространства имен — отличная штука! Будем делать их побольше!"""

# m = re.findall("^Если" , zen, re.MULTILINE)

# print(m)

# string = " Два даа."

# m = re.findall("д[ав]а", string, re.IGNORECASE)

# print(m)


# Задание 1

# grep голландец  zen.txt

# Задание 2

# string = "Москва: 777, 999, 797. Тула: 071, 950, 112.."

# m = re.findall("\d", string)

# print(m)

# Задание 3

string = "Приведение прошуршало и и исчезло в углу."

m = re.findall(".ло", string, re.IGNORECASE)

print(m)