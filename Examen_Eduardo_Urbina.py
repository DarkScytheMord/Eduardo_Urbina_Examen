import random
import csv

import os
os.system('cls')



trabajadores=[
            {"nombre": "Juan Pérez",},
            {"nombre": "María García",},
            {"nombre": "Carlos López",},
            {"nombre": "Ana Martínez",},
            {"nombre": "Pedro Rodríguez",},
            {"nombre": "Laura Hernández",},
            {"nombre": "Miguel Sánchez",},
            {"nombre": "Isabel Gómez",},
            {"nombre": "Francisco Díaz",},
            {"nombre": "Elena Fernández",}
            ]

def asigSueldo(trabajadores):
    sueldo=0
    for trabajador in trabajadores:
        trabajador["sueldo"]=random.randint(300000,2500000)
    return trabajadores
    
def clasSueldo():
    sueldosBajos = []
    sueldosMedios = []
    sueldosAltos = []
    totalBajos = 0
    totalMedios = 0
    totalAltos = 0

    for trabajador in trabajadores:
        if trabajador["sueldo"] < 800000:
            sueldosBajos.append(trabajador)
            totalBajos = totalBajos+1
            valorBajos = totalBajos
        elif 800000 <= trabajador["sueldo"] <= 2000000:
            sueldosMedios.append(trabajador)
            totalMedios = totalMedios+1
            valorMedios = totalMedios
        else:
            sueldosAltos.append(trabajador)
            totalAltos = totalAltos+1
            valorAltos = totalAltos
            
    print(f"Sueldos Menores a $800.000 Total={valorBajos}\n")
    for empleado in sueldosBajos:
        print(f"Nombre Empleado\tSueldo\n{empleado['nombre']}\t{empleado['sueldo']}\n")
        
    print(f"Sueldos Entre $800.000 y $2.000.000 Total={valorMedios}\n")
    for empleado in sueldosMedios:
        print(f"Nombre Empleado\tSueldo\n{empleado['nombre']}\t{empleado['sueldo']}\n")
            
    print(f"Sueldos Superiores a $2.000.000 Total={valorAltos}\n")
    for empleado in sueldosAltos:
        print(f"Nombre Empleado\tSueldo\n{empleado['nombre']}\t{empleado['sueldo']}\n")
            
def estadisticas():
    print


def reporteSueldo():
    print


def salir():
    print("Finalizando programa…\nDesarrollado por Eduardo Urbina\nRUT 20.907.578-4")


while True:
    print("\tMenu Gestion de Sueldos\n1) Asignar Sueldos.\n2) Clasificar Sueldos.\n3) Ver Estadisticas.\n4) Reporte de Sueldos.\n5) Salir del Programa.")
    try:
        vOpc=int(input("Ingrese opcion a Realizar:\n>"))
    except:
        vOpc=-1
        
    if vOpc == 1:
        asigSueldo(trabajadores)
        print("Sueldos Asignados")
        
    elif vOpc == 2:
        clasSueldo()
        
    elif vOpc == 3:
        estadisticas()
        
    elif vOpc == 4:
        reporteSueldo()
        
    elif vOpc == 5:
        salir()
        break
    
    else:
        print("Opcion no Valida")
        