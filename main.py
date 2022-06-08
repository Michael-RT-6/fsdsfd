def archivo():
  abrir  = open("resultadosTest.txt", "r")
  leer = abrir.read()
  leer = leer.split("\n")
  abrir.close()

  for i in range(len(leer)):
    leer[i] = leer[i].split(",")

    ima = ""
    for x in range(len(leer[i])):
      leer[i][x] = leer[i][x].strip(" ")
    for x in range(1,len(leer[i])):
      if len(leer[i][x]) == 1:
        ima+=leer[i][x]
    leer[i] = [leer[i][0], ima, leer[i][5]]

  return leer

def calcular_indice(lista):
  for i in range(len(lista)):
    ima = lista[i][1]
    total = 0.20 + 0.15 + 0.15 + 0.40
    if ima  == "TGAP":
      total = total*0.2
      lista[i].append("P1")
    elif ima  == "GTAP":
      total = total*0.22
      lista[i].append("P2")
    elif ima  == "PAGT":
      total = total*0.3
      lista[i].append("P3")
    elif ima  == "PATG":
      total = total*0.28
      lista[i].append("P4")
    else:
      total = 0.0
      lista[i].append("NO VALIDO")

    lista[i].append(total)
  return lista

def mostrar(lista):
  print("Nombre   Fecha    Perfil")
  for i in range(len(lista)):
    print(lista[i][0]+"   "+lista[i][2]+"   "+lista[i][3])

def cuentas(lista):
  v = 0
  p = 0
  for i in lista:
    if i[3] in ["P1", "P2", "P3", "P4"]:
      v += 1
      p += i[4]
  print("Personas con perfil valido:",v)
  print("Promedio de indices de perfiles:",p/v)

comenzar = "si"
while  comenzar == "si":
  print("*** Menu test visual ***")
  lista = archivo()
  lista = calcular_indice(lista)
  
  opcion = input("1- Mostrar lista de personas que rindieron el test\n2- Mostrar cantidad de personas que tienen un perfil valido y su promedio\n3-Salir\nNumero de opcion: ")

  if opcion == "1":
    mostrar(lista)
  elif opcion == "2":
    cuentas(lista)
  elif opcion == "3":
    comenzar = "terminar"
    print("** Cerrando menu **")
  else:
    print("Opcion no valida, vuelve a ingresar tu preferencia")

      
  



    

    
  