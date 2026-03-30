estudiante = {"1":{"id":1326594875,
              "name":"luis",
              "edad":18,
              "programa":"tecnologia y sistemas",
              "estado":"inactivo"
             },
              "2":{"id":1563874956,
              "name":"jhon",
              "edad":21,
              "programa":"salud y cuidado",
              "estado":"activo"
             },

             "3":{"id":1635449878,
              "name":"sarah",
              "edad":19,
              "programa":"administrativo y financiero",
              "estado":"activo"
             }
}
#validation that it is an integer
def entero(mensaje):
    
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error debes ingresar un numero y entero.")
# student registration function
def registrar(estudiante):
    id = entero("digite numero de identificacion del estudiante:")
    name = input("digite name de estudiante:")
    edad = entero("digite la edad del estudiante:")
    programa = input("digite el progama que desea el estudiante:")
    estado = entero("digite si es (1.activo o 2.inactivo) el estudiante:")
    if estado ==1:
        estado="activo"
    elif estado==2:
        estado="inactivo"
    else:
        print("opcion invalida")
    nuevo_estudiante =str(len(estudiante)+ 1)
    estudiante[nuevo_estudiante] ={
        "id":id,
        "name":name,
        "edad":edad,
        "programa":programa,
        "estado":estado
    }
    print("agregando estudiante..\n")
    return estudiante
#see all students
def lista():
    print(estudiante)
    return estudiante
#to consult the data of a specific student
def consultar(estudiante):
    buscar = entero("digite el numero de identificacion del estudiante:")
    estudiante_encontrado =None

    for datos in estudiante.values():
        if datos["id"] == buscar:
            estudiante_encontrado = datos
    
    if estudiante_encontrado:
        print(estudiante_encontrado)
    else:
        print("estudiante no encontrado")
    return estudiante
# update the data of a specific student
def actualizar(estudiante):
            numero = input("digite numero de estudiante:")
            print("\n1.id")
            print("2.name")
            print("3.edad")
            print("4.programa")
            print("5.estado")
            cambio = entero("digite lo que quiere cambiar del estudiante:")
            if cambio==1:
                new_id = entero("digite el numero del nuevo id del estudiante:")
                estudiante [numero]["id"]=new_id
            elif cambio==2:
                new_name = input("digite el nuevo name del estudiante:")
                estudiante [numero]["name"]=new_name
            elif cambio==3:
                new_edad = entero("digite la nueva edad del estudiante:")
                estudiante [numero]["edad"]=new_edad
            elif cambio==4:
                new_programa = input("digite el nuevo programa del estudiante:")
                estudiante [numero]["programa"]=new_programa
            elif cambio==5:
                new_estado = entero("digite un numero del nuevo estado (1.activo o 2.inactivo)")
                if new_estado ==1:
                    estudiante [numero]["estado"]="activo"
                elif new_estado ==2:
                    estudiante [numero]["estado"]="inactivo"
            else:
                print("error opcion invalida")
# Delete all data for a student using the number
def eliminar (estudiante):
    numero = input("digite el numero del estudiante que desea eliminar o expulsar:")

    if numero in estudiante:
        name = estudiante[numero]["name"]
        del estudiante[numero]
        print("el estudiante eliminado o espulsado es:",name)
    else:
        print("el estudiante no existe")
    return 

#program menu
def menu ():
    print("\n1.regitrar")
    print("2.ver lista de estudiantes")
    print("3.buscar estudiante")
    print("4.actualizar datos de estudiante")
    print("5.eliminar estudiante de la lista")
    print("6.salir\n")
#program 
def main():
    comenzar=False
    while not comenzar:
        menu()
        opcion = entero("digita un opcion de (1-6):")

        if opcion == 1:
            registrar(estudiante)
        elif opcion == 2:
            lista()
        elif opcion == 3:
            consultar(estudiante)
        elif opcion == 4:
            actualizar(estudiante)
        elif opcion == 5:
            eliminar(estudiante)
        elif opcion == 6:
            print("gracias por utilizar nuestro servicio")
            comenzar=True
        else:
            print("error opcion invalidad")
main()
