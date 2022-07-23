# Урок 4 (инструкции)
# Напишите программу, которая выведет на экран друг за другом три имени: Robert, Stannis, Renly
print('Robert')
print('Stannis')
print('Renly')


# Урок 5 (арифметические операции)
# Напишите программу, которая считает и выводит на экран последовательно (по одному значению в каждой строке) значения следующих математических выражений: 3 в степени 5, -8 разделить на -4, остаток от деления 100 на 3, сумму трёх предыдущих выражений
print(3**5)
print(-8/-4)
print(100%3)
print((3**5)+(-8/-4)+(100%3))


# Урок 7 (строки)
# Напишите программу, которая выводит на экран:
# - Did Joffrey agree?
# - He did. He also said "I love using \n".
# При этом программа использует только один print(), но результат на экране должен выглядеть в точности, как показано выше
print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')


# Урок 8 (gthtvtyyst)
# Найдите в программе необъявленную переменную и объявите её, присвоив ей значение Dragon
family = 'Targaryen'
pet = 'Dragon'
print(family)
print(' and ')
print(pet)


# Урок 9 (выражения в определениях)
# Напишите программу, которая берет исходное количество евро, записанное в переменную euros_count, переводит евро в доллары и выводит на экран. Затем полученное значение переводит в рубли и выводит на новой строчке
euros_count = 100
dollar_count = 100 * 1.25
ruble_count = dollar_count * 60
print(dollar_count)
print(ruble_count)


# Урок 11 (интерполяция)
# Выведите на экран две строки: Do you want to eat, ? и Yes, I'm hungry, mom. Вместо <name> должна использоваться переменная stark. При формировании итоговой строки используйте интерполяцию
stark = 'Arya'
print(f'''Do you want to eat, {stark}?
Yes, I'm hungry, mom.''')


# Урок 12 (извлечение символов из строки)
# Вам даны три переменные с фамилиями разных людей. Составьте и выведите на экран слово из символов в таком порядке:
# Третий символ из первой строки
# Второй символ из второй строки
# Четвертый символ из третьей строки
# Пятый символ из второй строки
# Третий символ из второй строки
# Попробуйте использовать интерполяцию. Внутри фигурных скобок можно размещать не только переменные, но и отдельные символы строки, извлечённые по индексу 
# (с помощью квадратных скобок)
one = 'Naharis'
two = 'Mormont'
three = 'Sand'
name = f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}'
print(name)


# Урок 13 (срезы строк)
# В переменной value лежит значение Hexlet. Извлеките из него и выведите на экран срез, который получит подстроку xle. Это задание можно сделать разными способами
value = 'Hexlet'
print(value[2:5])


# Урок 14 (типы данных)
# Выведите на экран строку 2 times, полученную из числа 2 и строки times, используя преобразования типов и конкатенацию:
print(str(2) + ' times')


# Урок 15 (Неизменяемость и примитивные типы)
# В переменной value хранится строковое представление числа. Получите модуль этого числа, используя функцию abs() и запишите его в ту же переменную value. Перед этим нужно привести строку к числу.
value = "-42"
value = int(value)
value = abs(value)
print(value)


# Урок 16 (Функции и их вызов)
# В коде программы определены две переменные, содержащие имена компаний. Посчитайте их общую длину в символах и выведите ее на экран
company1 = "Apple"
company2 = "Samsung"
a = len(company1 + company2)
print(a)


# Урок 17 (Сигнатура функции)
# Напишите программу, которая использует функцию abs() и выводит на экран модуль суммы двух переменых num1 и num2
num1 = 10
num2 = -13
summ = num1 + num2
summ = abs(summ)
print(summ)


# Урок 18 (Вызов функции - выражение)
# С помощью функции hex() выведите на экран шестнадцатеричное значение переменной number (предварительно округлите его до целого числа)
number = 10.1234
number = round(number)
number = hex(number)
print(number)


# Урок 19 (Функции с переменным числом параметров)
# Посчитайте программно (а не в голове) минимальное число среди 3, 10, 22, -3, 0 — и выведите его на экран. Воспользуйтесь функцией min(), которая работает аналогично max()
minz = min(3, 10, 22, -3, 0)
print(minz)


# Урок 20 (Детерминированность)
# Реализуйте код, который печатает на экран случайное число в диапазоне от 1 до 10 включительно. Для этого вам понадобятся операции умножения, сложения, а также преобразование типов. random() возвращает float, а нам нужен int. Попробуйте решить это задание в одну строку
from random import random
print(round(random() * 10))


# Урок 21 (Стандартная библиотека)
# Функция type() позволяет определить тип передаваемого аргумента. Название типа возвращается в виде строки. Например, вызов type(10) вернёт строку <class 'int'> (int, это сокращение от integer — целое число). Выведите на экран тип значения переменной motto
motto = 'Family, Duty, Honor'
print(type(motto))


# Урок 22 (Свойства и методы)
# Данные, вводимые пользователями, часто содержат лишние пробельные символы в конце или начале строки. Обычно их вырезают с помощью метода .strip(), например, было: ' hello\n ', стало: 'hello'. Обновите переменную first_name, записав в неё то же самое значение, но обработанное методом .strip(). Распечатайте то, что получилось, на экран
first_name = '  Grigor   \n '
first_name = first_name.strip()
print(first_name)


# Урок 23 (Цепочка методов)
# С помощью слайсов, получите часть предложения, записанного в переменную text, c 5 по 16 символы включительно. 
# Полученную подстроку обработайте методом .strip() и выведите на экран длину итоговой подстроки. 
# Выполните эти операции подряд в цепочке без создания промежуточных переменных.
text = 'When \t\n you play a \t\n game of thrones you win or you die.'
print(len(text[4:16].strip()))


# Урок 24 (Определение функций)
# Реализуйте функцию print_motto(), которая печатает на экран фразу Winter is coming
def print_motto():
    nm = 'Winter is coming'
    print(nm)
    
    
# Урок 25 (Возврат значений)
# Реализуйте функцию say_hurray_three_times(), которая возвращает строку hurray! hurray! hurray!
def say_hurray_three_times():
    text = 'hurray! hurray! hurray!'
    return(text)


# Урок 26 (Параметры функций)
# Реализуйте функцию truncate(), которая обрезает переданную строку до указанного количества символов, добавляет в конце троеточие и возвращает получившуюся строку. 
# Подобная логика часто используется на сайтах, чтобы отобразить длинный текст в сокращенном виде.
#Функция принимает два параметра:
# Строка, которую нужно обрезать
# Число символов, которые нужно оставить
def truncate(text, length):
    result = f'{text[0:length]}...'
    return result


# Урок 27 (Необязательные параметры функций)
# Реализуйте функцию get_hidden_card(), которая принимает на вход номер кредитки (состоящий из 16 цифр) в виде строки и возвращает его скрытую версию, 
# которая может использоваться на сайте для отображения. Если исходная карта имела номер 2034399002125581, то скрытая версия выглядит так ****5581. 
# Другими словами, функция заменяет первые 12 символов, на звездочки. Количество звездочек регулируется вторым необязательным параметром. 
# Значение по умолчанию — 4
def get_hidden_card(card_number, stars_count=4):
    visible_digits = card_number[-4:]
    return f'{"*" * stars_count}{visible_digits}'


# Урок 28 (Именованные аргументы)
# Реализуйте функцию trim_and_repeat(), которая принимает три параметра: строку, offset — число символов, на которое нужно обрезать строку слева 
# и repetitions — количество раз, сколько ее нужно повторить, и возращает получившуюся строку. Число символов для среза по умолчанию равно 0, а повторений — 1
def trim_and_repeat(text, offset=0, repetitions=1): 
    return text[offset:] * repetitions


# Урок 29 (Окружение)
# Это задание не связано напрямую с уроком, это просто еще одно полезное упражнение по работе с функциями.
# Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку с разницей в возрасте в виде The age difference is 11
def get_age_difference(year_1, year_2):
    return 'The age difference is ' + str(abs(year_1 - year_2))


# Урок 30 (Логика)
# Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы. Функция должна вернуть булево значение











