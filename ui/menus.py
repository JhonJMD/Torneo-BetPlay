import os
import ui.titles as t
import funciones as fun

def menuPrincipal():
    os.system('cls')
    opciones = ['Registrar Equipo','Registrar fecha de juego','Reportes','Salir']
    t.headerPrincipal()
    for i, item in enumerate(opciones):
        print(f'{i+1}. {item}')

def menuRegequipos():
    t.headerRegfecha()
    for idx, item in enumerate(fun.Equipos):
        print(f'{idx+1}. {item[0]}')
    
def menuReport():
    os.system('cls')
    opReport = ['A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO','B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE','C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO','D. TOTAL DE GOLES ANOTADOS EN EL TORNEO','E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO','F. REGRESAR AL MENU PRINCIPAL']
    t.headerReportes()
    for idx, item in enumerate(opReport):
        print(item)
