#1 Написать функцию, которая будет считать и возвращать сумму двух чисел.
# Если сумма больше 10 - вывести на экран “This sum is greater than 10.
# It’s {sum}”, если меньше - “This sum is less than 10. It’s {sum}”

def func1(one, two):
    result = one + two
    return result

res1 = func1(1, 2)
func1(3, 5)
func1(6, 7)
print("result: ",res1)

def sum(arg1, arg2):
    result = arg1 + arg2
    return result

arg1 = 8
arg2 = 7
sum1 = arg1 + arg2

if sum1 > 10:
    print(f"This sum is greater than 10. It’s {sum1}")
else:
    print(f"This sum is less than 10. It’s {sum1}")

#2 Написать функцию, которая будет принимать пароль.
# Если в пароле есть буквы и его длина не менее 10 символов вывести: “Your password is strong.”
# в противном случае “Your password is not strong enough.”

def password_level(password):

    if len(password) < 10:
        s = "Your password is not strong enough."
        return s

    elif password.isdigit():
        s = "Your password is not strong enough."
        return s

    elif password.isalpha():
        s = "Your password is strong."
        return s

print(password_level("qwertyqqqqqqq"))

print(password_level("123456762327"))


#3 Белки проводят большую часть дня, играя.
# В частности, они играют, если температура составляет от 60 до 90 (включительно).
# Если лето, то верхний предел температуры равен 100 вместо 90.
# Напишите функцию, которая принимает температуру int и логическое значение is_summer,
# верните True, если белки играют, и False в противном случае.

def belki(temp, is_summer):
    if not is_summer:
       if temp >= 60 and temp <= 90:
          return True
       else:
           return False
    else:
        if temp >=60 and temp <=100:
            return True
        else:
            return False
print(belki(98, True))
print(belki(99, False))





    

