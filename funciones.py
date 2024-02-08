import os
import ui.titles as t
import ui.menus as m
Equipos= []

def regEquipos():
    os.system('cls')
    t.headerRegequipo()
    isAddEquipo = True
    while isAddEquipo:
        nombre = input('Ingrese el nombre del Equipo: ').capitalize()
        Equipos.append([nombre, 0, 0, 0, 0, 0, 0, 0, ''])
        isAddEquipo = bool(input('¿Desea ingresar otro Equipo? (S si/Enter no): '))

def regFecha():
    estados = ['Local','Visitante']
    for i in range(0,2):
        isEquipo = True
        while isEquipo:
            try:
                os.system('cls')
                m.menuRegequipos()
                equipo = int(input(f'Ingrese el numero del equipo {i+1}: '))
                if i == 0:
                    aux = equipo
            except ValueError:
                print('Dato Erroneo')
            else:
                for idx, item in enumerate(Equipos):
                    if equipo == idx+1:
                        isEquipo = False
                        isEstado = True
                        while isEstado:
                            try:
                                for idx, items in enumerate(estados):
                                    print(f'{idx+1}. {items}')
                                est = int(input(': '))
                            except ValueError:
                                print('Dato Erroneo')
                            else:
                                if (est == 1):
                                    item[8] = estados[0]
                                    item[1]+=1
                                    isEstado = False
                                elif(est == 2):
                                    item[8] = estados[1]
                                    item[1]+=1
                                    isEstado = False
                                else:
                                    print('Dato ingresado no valido') 
                        isGoles = True
                        while isGoles:
                            try:
                                goles = int(input(f'Cuantos goles hizo el equipo {item[0]}: '))
                                if i == 0:
                                    aux2 = goles
                            except ValueError:
                                print('Dato no valido')
                            else:
                                if goles >= 0:
                                    item[5] += goles
                                    if (i == 1):
                                        Equipos[aux-1][6] += goles
                                        Equipos[equipo-1][6] += aux2 
                                        if goles > aux2:
                                            Equipos[equipo-1][2]+=1
                                            Equipos[aux-1][3]+=1
                                            Equipos[equipo-1][7]+=3
                                        elif(goles < aux2): 
                                            Equipos[equipo-1][3]+=1
                                            Equipos[aux-1][2]+=1
                                            Equipos[aux-1][7]+=3
                                        else:
                                            Equipos[equipo-1][4]+=1
                                            Equipos[aux-1][4]+=1
                                            Equipos[equipo-1][7]+=1
                                            Equipos[aux-1][7]+=1
                                            
                                    isGoles = False
                                else:
                                    print('Los goles no pueden ser negativos')
    os.system('pause')

def reporte():
    maxG = -1
    maxP = -1
    maxPG = -1
    sumEqui = 0
    sumPart = 0
    os.system('cls')
    t.headerReportes()
    for i, item in enumerate(Equipos):
        actualG = Equipos[i][5]
        actualP = Equipos[i][7]
        actualPG = Equipos[i][2]
        sumEqui+=Equipos[i][5]
        sumPart+=Equipos[i][1]
        if actualG > maxG:
            maxG = actualG
            maxgolE = item[0]
        if actualP > maxP:
            maxP = actualP
            maxPun = item[0]
        if actualPG > maxPG:
            maxPG = actualPG
            maxPar = item[0]
    promGol = sumEqui/sumPart    
    isReport = True
    while isReport:
        try:
            m.menuReport()
            op = input(': ').upper()
        except ValueError:
            print('Dato erroneo')
        else:
            if (op == 'A'):
                print(f'Equipo que mas goles anoto {maxgolE}')
                os.system('pause')
            elif (op == 'B'):
                print(f'Equipo que mas puntos tiene {maxPun}')
                os.system('pause')
            elif (op == 'C'):
                print(f'Equipo que mas partidos gano {maxPar}')
                os.system('pause')
            elif (op == 'D'):
                print(f'Total de goles anotados {sumEqui}')
                os.system('pause')
            elif (op == 'E'):
                print(f'Promedio de goles anotados {promGol}')
                os.system('pause')
            elif (op == 'F'):
                isReport = False
            else:
                print('Dato no valido')
    os.system('pause')