import requests
#Para utilizar este script, el archivo api_sum.php debe estar hosteado en un servidor local
#que este corriendo en el puerto 6660, yo lo probe con Apache2
print("Ingrese el primer numero")
waiting_for_input = True
while waiting_for_input:
    num1 = input("Ingrese el primer numero: ")
    try:
        num1 = float(num1)
    except ValueError:
        print("El valor ingresado no es un número, intente nuevamente.")
        continue
    num2 = input("Ingrese el segundo numero: ")
    try:
        num2 = float(num2)
    except ValueError:
        print("El valor ingresado no es un número, intente nuevamente.")
        continue
    waiting_for_input = False


url = 'http://127.0.0.1:6660//api_sum.php'
params = {'num1': num1, 'num2': num2}
response = requests.get(url, params=params)
print("RESULTADO:")
print(response.text)