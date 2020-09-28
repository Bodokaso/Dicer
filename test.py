import random

invalid_inp = True
is_playing = True
while is_playing:

    print("Bienvenido a tu generador de dados automatico, a continuacion selecciona un dado (d4, d6, d10, d12, d20)")

    inp_1 = int(input("Ingrese el tipo de dado que desea tirar: "))

    if inp_1 == 4:
        invalid_inp = False  # Set to False because input was valid
    elif inp_1 == 6:
        invalid_inp = False  # Set to False because input was valid
    elif inp_1 == 10:
        invalid_inp = False  # Set to False because input was valid
    elif inp_1 == 12:
        invalid_inp = False  # Set to False because input was valid
    elif inp_1 == 20:
        invalid_inp = False  # Set to False because input was valid
    else:
      print("el valor ingresado no es valido, intente nuevamente.")
      break
    inp_2 = int(input("Ingrese la cantidad de veces que desea rolear :"))
    for rand_num in [random.randrange(1, inp_1) for i in range(inp_2)]:
      print(rand_num)

    inp_3 = input("Desea continuar? (y/n) ")
    if inp_3 == "y":
      continue
    elif inp_3 == "n":
      print("Adios")
      is_playing = False
