#TODAS LAS FUNCIONES ESTAN EN EL MISMO ORDEN QUE APARECERAN EN EL MENU
#perdon por usar mucho (" ") fue la forma mas facil que se me ocurrio de ordenar el como ve el programa el usuario
#al igual que usando (","*90) que fue algo que nos enseño el primer profe que tuvimos.
#la palabra "contraseña" esta con "ñ" solo donde se supone hay texto pero para lo demas esta con "n"


# registrar usuarios

def registrar(datos_usuario):
    usuario = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    datos_usuario[usuario] = contrasena
    print(" ")
    print("Usuario registrado con exito")
    print(" ")

# hacer login de usuario

def login(datos_usuario):
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if usuario in datos_usuario and datos_usuario[usuario] == contrasena:
        print(" ")
        print("INICIANDO SESION... ")
        print(" ")
    else:
        print(" ")
        print("Usuario o contraseña incorrectos")
        print(" ")
        
# mostrar la informacion de usuarios

def mostrar_usuarios(datos_usuario):
    print("Usuarios registrados: ")
    for usuario, contrasena in datos_usuario.items():
        print(","*90)
        print("Usuario: ", usuario)
        print("Contraseña: ", contrasena)  
        print(","*90)
        
# Funcion para pasar la informacion a un archivo de texto   
     
def archivo_de_texto(datos_usuario):
    nombre_archivo = input("Escriba el nombre del archivo: ")
    with open(nombre_archivo + ".txt", "w") as archivo:
        for usuario, contrasena in datos_usuario.items():
            archivo.write(f"{usuario}: {contrasena}\n")
    print(" ")
    print(f"Información guardada en el archivo: {nombre_archivo}")
    print(" ")



# Diccionario para guardar la informacion de los usuarios

datos_usuario = {}


# Menu del sistema

while True:
    print("Bienvenido al menu del sistema")
    print(" ")
    print(","*90)
    print("1) Registrar usuarios")
    print("2) Hacer login en el sistema")
    print("3) Mostrar informacion de Usuarios")
    print("4) Convertir datos en archivo de texto")
    print("5) Salir del menu")
    print(","*90)
    print(" ")
    try:
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            registrar(datos_usuario)
            
        elif opcion == 2:
            login(datos_usuario)
            
        elif opcion == 3:
            mostrar_usuarios(datos_usuario)
            
        elif opcion == 4:
            archivo_de_texto(datos_usuario)
            
        elif opcion == 5:
            print(" ")
            print("SALIENDO DEL SISTEMA...")
            print(" ")
            break
        else:
            print(" ")
            print("Opcion invalida, intente denuevo")
            print(" ")
            
    except ValueError:
        print(" ")
        print("opcion invalida, ingrese un numero valido")
        print(" ")
        
# Decidi agregar un try except ya que justo lo vimos en la clase anterior y se me hacia
# perfecto para separa el error por ingresar un numero no valido y el error por ingresar caracteres no validos