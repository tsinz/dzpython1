# д/з 1
# задание 1.Пользователь вводит число N, программа возвращает N-ный член последовательности Фибоначчи. Числа Фиббоначи: первые два члена 1 и 1. Каждый следующий член - сумма двух предыдущих.
n = int(input("число:"))     # вводить число и преобразовать это число в целое число(преобразовать строку в число).
def abc(n):     # cоздать функцию
    a,b = 1,1    # начальное значение – 1.
    for i in range(n-1):
        a,b = b,a+b     # сначала определять значение в правой части знака равенства, а затем присваивать число левой части знака равенства.
    return a
 
print (abc(n))


# задание 2.Пользователь вводит число, программа проверяет, является ли оно простым.
n = int(input("число:"))
if n > 1:     # 1 не является простым числом
# посмотреть простые делители
   for i in range(2,n):    # присваивать i все целые числа от 2 до n.
       if (n % i) == 0:    # если i делю n, остаток равен нулю
           print(n,"не простое число")
           break
   else:
       print(n,"простое число")

# задание 3.Программа возвращает простые делители введенного числа, или сообщает, что оно простое.
n = int(input("число:"))
if n > 1:     # 1 не является простым числом
# посмотреть простые делители
   for i in range(2,n):    # присваивать i все целые числа от 2 до n.
       if (n % i) == 0:    # если i делю n, остаток равен нулю
           print(n,"не простое число")
           print(i,"умножается на",n//i,"да",n)     # простые делители
           break
   else:
       print(n,"простое число")
       
       
# задание 4.Программа находит наибольший общий делитель для двух введенных чисел.
def hcf(x, y):  
# Мы строим функцию для поиска наибольшего общего делителя двух чисел. Основная идея такова:
# 1. Введите две цифры
# 2. Определить меньшее из двух чисел
# 3. Два числа делятся на i (от 1 до меньшего числа + 1, поскольку мы ищем общий делитель двух чисел, нам нужно вычислить только меньшее число + 1)
 
   if x > y:
       smaller = y
   else:
       smaller = x
 
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
 
   return hcf # вернуть эту функцию
 
 
num1 = int(input("число 1: "))
num2 = int(input("число 2: "))
 
print( num1,"и", num2,"наибольший общий делитель", hcf(num1, num2))
       
       
задание 5.Программа запрашивает число, а затем выводит квадрат из *, где длина стороны равна данному числу.
import turtle     # модуль рисования
n = int(input("число:"))     # вводить данные
my_turtle = turtle.Turtle()  # направление квадрата
side_length = n     # введенное число равно длине стороны.
for i in range(4):     
    my_turtle.forward(side_length)    # первое направление квадрата (перед)
    my_turtle.left(90)     # определить угол другого направления и направления
turtle.done()


задание 6.Программа запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.
import turtle     # модуль рисования
n1 = int(input("число 1:"))     # вводить данные
n2 = int(input("число 2:"))     # вводить данные
side_length1 = n1 # длина прямоугольника
side_length2 = n2 # ширина прямоугольника
turtle.shape("turtle")  # изменить форму курсора черепахи на черепаху.
turtle.width(3)  # размер ручки
turtle.color("orange")  # цвет первой стороны (длинной стороны прямоугольника)
turtle.forward(side_length1)  # длина прямоугольника
turtle.left(90)  # повернитесь налево на 90 градусов и нарисовать вторую сторону.
turtle.color("red")  # цвет второй стороны прямоугольника
turtle.forward(side_length2)  # ширина прямоугольника
turtle.left(90)  
turtle.color("green")  
turtle.forward(side_length1)  # длина прямоугольника
turtle.left(90)  
turtle.color("purple")  
turtle.forward(side_length2)  # ширина прямоугольника
turtle.ht()  # скрыть курсор-черепаху
turtle.done()   # конец программы
задание 7.Программа запрашивает два числа и выводит на экран прямоугольник, в котором змейкой по вертикали записаны числа, начиная с 1.
n1 = int(input("число 1:"))     # вводить данные
n2 = int(input("число 2:"))     # вводить данные
[print(*range(i, n1*n2+1, n1)) for i in range(1, n1+1)]     # два введенных числа составляют длину и ширину прямоугольника, а умножение двух введенных чисел представляет собой количество элементов прямоугольника.



# д/з 2
# задание 1
from string import ascii_lowercase # строчные буквы
from string import ascii_uppercase # прописная буква
def upp(txt): # делать функцию
    TXT = ''
    for i in txt: # содержит все буквы текста.
        if i in ascii_lowercase: 
            index = ascii_lowercase.index(i) # определить положение строчных букв в тексте.
            i = ascii_uppercase[index] # преобразовать строчные буквы в прописные
        TXT += i # каждая строчная буква преобразуется в прописную.
    print(TXT)
txt = input() # вводить текст
upp(txt)





# д/з 3
# задание 1.переписать вычисление n-ного члена последовательности Фибоначчи с помощью рекурсии.
n = int(input("число:"))     # вводить число и преобразовать это число в целое число(преобразовать строку в число).
def recur_fibo(n):     # cоздать функцию
if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2)) # определение порядковых чисел Фибоначчи с помощью рекурсии
   
 
print (recur_fibo(n))


