#arquivo teste para commit durante a aula

a = float(input("Digite qualquer numero e direi se ele é par"))

try:
    if a % 2 == 0:
        print('É par')
    else:
        print('Não é Par')

except ValueError:
    print('valor digitado não é número')