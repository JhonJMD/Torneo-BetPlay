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
    


