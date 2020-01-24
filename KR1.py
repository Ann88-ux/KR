from random import randint
def S(fuc):
    def wrapper(v0,v1,t):
        s= ((v1+v0)/2)*t
        fuc(v0,v1,t)
        print('Расстояние:',s,'м')
    return wrapper
def A(v0, v1, t):
    a=(v1-v0)/t
    print('Ускорение:',a,'м/c*c')
    return a
try:
    A=S(A)
    A(v0=int(input()),v1=int(input()),t=int(input()))
except ValueError:
    print('Вы ввели не числа')
    A=S(A)
    A(randint(1,10),randint(1,10),randint(1,5))
except ZeroDivisionError:
    print('Время не может быть равным нулю')
    A=S(A)
    A(randint(1,10),randint(1,10),randint(1,5))