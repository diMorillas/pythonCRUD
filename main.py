from functions import (
    insertar_ong, insertar_animal,
    mostrar_ong, mostrar_animales,
    buscar_ong_por_pais, buscar_animales_por_estado,
    actualizar_ong, actualizar_animal,
    eliminar_ong, eliminar_animal,mostrar_cif_nombre,
    importarxml,buscar_animales_por_nombre, buscar_animales_por_id,
    buscar_ong_por_CIF
)

import random as r

#Para evitar errores en el ID, mejor generarlo de forma aleatoria como en mongoDB.

def generaID():
    id = "" #Hago una cadena de caracteres vacía que relleno con numeros aleatorios convertidos en string
    for i in range(9):
        numero = r.randint(0,9)
        id+=str(numero) #str convierte el int a string
    return id

#Funciones de manejo de errores

def verificar_cif(cif):
    # Para ver si es string
    if len(cif) != 9:
        return False
    if not cif[:8].isdigit():
        return False
    if not cif[8].isalpha() or cif[8].islower():
        return False
    if cif[8] != cif[8].upper():
        return False
    else:
        return True


#Verificamos que el número de especies coincide con el estado que han añadido a la BBDD

def main_menu():
    while True:
        try:
            print("\nMenu Principal:")
            print("1. Insertar datos")
            print("2. Mostrar datos")
            print("3. Buscar datos")
            print("4. Actualizar datos")
            print("5. Eliminar datos")
            print("6. Importar datos XML")
            print("7. Salir")

            eleccion = int(input("Elija una opción: "))

            if eleccion == 1:
                menu_inserts()
            elif eleccion == 2:
                mostrar_menu()
            elif eleccion == 3:
                buscar_menu()
            elif eleccion == 4:
                actualizar_menu()
            elif eleccion == 5:
                menu_eliminar_datos()
            elif eleccion == 6:
                importarxml()
                print("Se ha importado de forma correcta")
            elif eleccion == 7:
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def  menu_inserts():
    print("\nInsertar Datos:")
    print("1. Insertar ONG")
    print("2. Insertar Animal")
    print("3. Volver al menú principal")

    try:
    
    #elección principal para insertar

        eleccion = int(input("Elija una opción: "))

        if eleccion == 1:
            cif = input("Ingrese el CIF de la ONG: ")
            if verificar_cif(cif):
                pass 
            else:
                while verificar_cif(cif) != True:
                    print("El cif introducido es erróneo: Debe tener 9 carácteres y una letra mayúscula al final")
                    cif = input("Ingrese el CIF de la ONG: ")
                    
            nombre_ong = input("Ingrese el nombre de la ONG: ")
            pais_ong = input("Ingrese el país de la ONG: ")
            if insertar_ong(cif, nombre_ong, pais_ong):
                print("No se ha creado la ONG")
            else:
                print("La ONG se ha creado")

        elif eleccion == 2:
            id_especie = generaID()
            estado = int(input("Ingrese el estado del animal: \n 1.Vulnerable \n 2.Peligro \n 3.Extinto\n Tu elección: "))
            if estado ==1:
                estado = "vulnerable"
            elif estado == 2:
                estado = "peligro"
            elif estado ==3:
                estado = "extinto"
            else:
                print("Valor erróneo")
                estado = int(input("Ingrese el estado del animal: \n 1.Vulnerable \n 2.Peligro \n 3.Extinto\n Tu elección: "))
                
            #verificar que no puedan poner numeros en el nombre_especie y en el nombre animal
            nombre_especie = input("Ingrese el nombre de la especie: ")
            # --------añadir esta linea----------
            while not nombre_especie.isalpha():
                print("El nombre de la especie solo puede contener letras.")
                nombre_especie = input("Ingrese el nombre de la especie: ")
            # ------------------
            nombre_animal = input("Ingrese el nombre del animal: ")
            print("Estas son las ONG's disponibles:\n")
            ongs_disponibles = mostrar_cif_nombre()
            if ongs_disponibles:
                for data in ongs_disponibles:
                    print(f"CIF: {data[0]}, ONG: {data[1]}")
            else:
                print("No se encontraron datos.")
            cif_ong_perteneciente = input("Inserta el CIF de la ONG a la que pertenece: ")
            while not verificar_cif(cif_ong_perteneciente):
                print("El CIF introducido es erróneo: Debe tener 9 carácteres y una letra mayúscula al final")
                cif_ong_perteneciente = input("Inserta el CIF de la ONG a la que pertenece: ")
            if verificar_cif(cif_ong_perteneciente) == True:
                insertar_animal(id_especie, estado, nombre_especie, nombre_animal,cif_ong_perteneciente)
                print("Se ha introducido el animal en la BBDD")
            else:
                print("No se ha podido añadir el animal")
                main_menu()


        elif eleccion == 3:
            main_menu()

        else:
            print("Opción no válida.")
    except ValueError:  #evita el ValueError si no ponemos un string
        print("Entrada no válida.")

def mostrar_menu():
    print("\nMostrar Datos:")
    print("1. Mostrar ONGs")
    print("2. Mostrar Animales")
    print("3. Volver al menú principal")

    try:
        eleccion = int(input("Elija una opción: "))

        if eleccion == 1:
            ongs = mostrar_ong()
            for ong in ongs:
                print(f"CIF: {ong[0]}, Nombre: {ong[1]}, País: {ong[2]}")

        elif eleccion == 2:
            animales = mostrar_animales()
            for animal in animales:
                print(f"ID: {animal[0]}, Especie: {animal[3]}, Nombre: {animal[1]} Estado: {animal[2]} ONG:{animal[4]} ")

        elif eleccion == 3:
            main_menu()
        else:
            print("Opción no válida.")
    except ValueError: #Control de elecciones dentro del menú
        print("Entrada no válida, intente nuevamente.")

def buscar_menu():
    print("\nBuscar Datos:")
    print("1. Buscar ONG por CIF")
    print("2. Buscar ONG por país")
    print("3. Buscar Animal por estado")
    print("4. Buscar Animal por nombre")
    print("5. Buscar Animal por ID")
    print("6. Volver al menú principal")

    try:
        eleccion = int(input("Elija una opción: "))

        if eleccion == 1:
            cif_ong = input("Ingrese el CIF de la ONG: ")
            ongs = buscar_ong_por_CIF(cif_ong)
            print("Estas son las ONGs que coinciden con tu búsqueda")
            for ong in ongs:
                print(f"CIF: {ong[0]}, Nombre: {ong[1]}, País: {ong[2]}")
            buscar_menu()


        if eleccion == 2:
            pais = input("Ingrese el país de la ONG: ")
            ongs = buscar_ong_por_pais(pais)
            print("Estas son las ONGs que coinciden con tu búsqueda")
            for ong in ongs:
                print(f"CIF: {ong[0]}, Nombre: {ong[1]}, País: {ong[2]}")
            buscar_menu()

        elif eleccion == 3:
            estado = int(input("Ingrese el estado del animal: \n 1.Vulnerable \n 2.Peligro \n 3.Extinto\n Tu elección: "))
            if estado ==1:
                estado = "vulnerable"
            elif estado == 2:
                estado = "peligro"
            elif estado ==3:
                estado = "extinto"
            else:
                print("Valor erróneo")
                estado = int(input("Ingrese el estado del animal: \n 1.Vulnerable \n 2.Peligro \n 3.Extinto\n Tu elección: "))
            lista_estado = []
            lista_estado.append(estado)
            animales = buscar_animales_por_estado(lista_estado)
            print("Estas son los animales que coinciden con tu búsqueda")

            for animal in animales:
                print(f"ID: {animal[0]}, Estado: {animal[2]}, Nombre: {animal[1]}")

        elif eleccion == 4:
            nombre_animal = input("Ingrese el nombre del animal: ")
            lista_nombre = []
            lista_nombre.append(nombre_animal)
            animales = buscar_animales_por_nombre(lista_nombre)
            print("Estas son los animales que coinciden con tu búsqueda")
            for animal in animales:
                print(f"ID: {animal[0]}, Estado: {animal[2]}, Nombre: {animal[1]}")
            buscar_menu()


        elif eleccion == 5:
            id_animal = input("Ingresa el ID del animal: ")
            id_buscarAnimal = []
            id_buscarAnimal.append(id_animal)
            animales = buscar_animales_por_id(id_buscarAnimal)
            print("Estas son los animales que coinciden con tu búsqueda")

            for animal in animales:
                print(f"ID: {animal[0]}, Estado: {animal[2]}, Nombre: {animal[1]}")
            buscar_menu()

        elif eleccion == 6:
            main_menu()

    except ValueError:
        print("Entrada no válida, intente nuevamente.")

def actualizar_menu():
    print("\nActualizar Datos:")
    print("1. Actualizar ONG")
    print("2. Actualizar Animal")
    print("3. Volver al menú principal")

    try:
        eleccion = int(input("Elija una opción: "))

        if eleccion == 1:
            #----------
            ongs = mostrar_ong()
            for ong in ongs:
                print(f"CIF: {ong[0]}, Nombre: {ong[1]}, País: {ong[2]}")
            #----------    
            
            cif_valid = False
            while not cif_valid:       
                cif = input("Ingrese el CIF de la ONG: ")
                for ong in ongs:
                    if cif == ong[0]:
                        cif_valid = True
                        break
                if not cif_valid:
                    print("El CIF ingresado no coincide con ninguno de los mostrados.")
                    
            nuevo_nombre = input("Ingrese el nuevo nombre de la ONG: ")
            while not nuevo_nombre.isalpha():
                print("El nombre de la ONG solo puede contener letras.")
                nuevo_nombre = input("Ingrese el nuevo nombre de la ONG: ")
            nuevo_pais = input("Ingrese el nuevo país de la ONG: ")
            while not nuevo_pais.isalpha():
                print("El nombre del país solo puede contener letras.")
                nuevo_pais = input("Ingrese el país de la ONG: ")
            actualizar_ong(cif, nuevo_nombre, nuevo_pais)
            print("La ONG ha sido actualizada")
           
        elif eleccion == 2:
            animales = mostrar_animales()
            print("Animales en la BBDD")
            for animal in animales:
                print(f"ID: {animal[0]}, Estado: {animal[2]}, Nombre: {animal[1]}")
            #----------    
            id_valid = False
            while not id_valid:
                id_especie = input("Ingrese el ID de la especie: ")       
                for animal in animales:
                    if id_especie == animal[0]:
                        id_valid = True
                        break
                if not id_valid:
                    print("El ID que has introducido no es correcto")
                    print("Animales en la BBDD")
                    animales = mostrar_animales()
                    for animal in animales:
                        print(f"ID: {animal[0]}, Estado: {animal[2]}, Nombre: {animal[1]}")

            #------------

            nuevo_estado = int(input("Ingrese el estado del animal: \n 1.Vulnerable \n 2.Peligro \n 3.Extinto\n Tu elección: "))
            if nuevo_estado ==1:
                nuevo_estado = "vulnerable"
            elif nuevo_estado == 2:
                nuevo_estado = "peligro"
            elif nuevo_estado ==3:
                nuevo_estado = "extinto"
            else:
                print("Valor erróneo")
                nuevo_estado = int(input("Ingrese el estado del animal: \n 1.Vulnerable \n 2.Peligro \n 3.Extinto\n Tu elección: "))
            
            nuevo_nombre = input("Ingrese el nuevo nombre(deje vacío si que no quiere cambiar): ")
  
            actualizar_animal(id_especie, nuevo_estado, nuevo_nombre)
            print("El animal ha sido actualizado")

        elif eleccion == 3:
            main_menu()
        
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada no válida, intente nuevamente.")

def menu_eliminar_datos():
    print("\nEliminar Datos:")
    print("1. Eliminar ONG")
    print("2. Eliminar Animal")
    print("3. Volver al menú principal")

    try:
        eleccion = int(input("Elija una opción: "))

        if eleccion == 1:
            #------------
            ongs = mostrar_ong()
            for ong in ongs:
                print(f"CIF: {ong[0]}, Nombre: {ong[1]}, País: {ong[2]}")
            #------------
            cif_valid = False
            while not cif_valid:       
                cif = input("Ingrese el CIF de la ONG: ")
                for ong in ongs:
                    if cif == ong[0]:
                        cif_valid = True
                        break
                if not cif_valid:
                    print("El CIF ingresado no coincide con ninguno de los mostrados.")
            id_eliminarONG = []
            id_eliminarONG.append(cif)
            if eliminar_ong(id_eliminarONG):
                print("No se ha eliminado la ONG")
            else:
                print("ONG eliminada")

        elif eleccion == 2:
            #---------------
            animales = mostrar_animales()
            for animal in animales:
                print(f"ID: {animal[0]}, Estado: {animal[2]}, Nombre: {animal[1]}")
            #----------------
            id_especie = input("Ingrese el ID de la especie: ")
            id_valid = False
            while not id_valid:
                id_especie = input("Ingrese el ID de la especie: ")       
                for animal in animales:
                    if id_especie == animal[0]:
                        id_valid = True
                        break
                if not id_valid:
                    print("El ID que has introducido no es correcto")
            id_eliminar = []
            id_eliminar.append(id_especie)
            if eliminar_animal(id_eliminar):
                print("No se ha eliminado")
            else:
                print("El animal se ha eliminado")

        elif eleccion == 3:
            main_menu()
        
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada no válida, intente nuevamente.")

# Ejecutar el menú principal
if __name__ == "__main__":
    main_menu()