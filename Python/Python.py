print ("buenos días")

Lucas = 49

print(Lucas)

suma = 5 + 90

print(suma)


def add(a, b):
    x = a + b
    return x

my_sum = add(15, 13)

print(my_sum)


a = 5

b = '10'

try:
    print(a+b)
except:
    print('pordios, esto iba a pasar')


    edad = 17

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres mayor de edad y estás en edad laboral")
else:
    print("Eres mayor de edad y estás en edad de jubilación")


lista = [1, 2, 3, 4]
lista.remove(3)
print(lista)
