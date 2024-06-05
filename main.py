import pygame
import sys 
import boton
import random
from pygame.locals import *
import time

pygame.init()

purpura1 = (38, 35, 53)
purpura2 = (23, 21, 32)
blanco = (239, 239, 239)
gris = (51, 49, 73)#232C36

ancho, alto = 1200,700
fil_m1, col_m1 = 5, 3
fil_m2, col_m2 = 6, 3

tablero_hist=[[0,0,0,0,0,0],
              [0,0,0,0,0,0],
              [0,0,0,0,0,0]]

lista_cartas=[]
espacios=[]
repetidos = []

juego_nuevo = True

pantalla = pygame.display.set_mode((ancho,alto))
timer = pygame.time.Clock()
fps = 60
puntuacion=0
parejas=0
tiempo_jugando = 0
intentos_restantes = 2

primer_click = False
segundo_click = False
primer_click_id = -1
segundo_click_id = -1

fuente_titulo = pygame.font.SysFont("Century Gothic",35)
fuente_texto = pygame.font.SysFont("Century Gothic",20)

perdio_gano = 3

def desordenar_tabalero():
    for i in range(fil_m2*col_m2//2):
        lista_cartas.append(i)
    for i in range(fil_m2*col_m2):
        carta = lista_cartas[random.randint(0,len(lista_cartas)-1)]
        espacios.append(carta)
        if carta in repetidos:
            repetidos.remove(carta)
            lista_cartas.remove(carta)
        else:
            repetidos.append(carta)
            repetidos.append(carta)
fondo = ''
def dibuja_layout():
    global boton_salir
    global fondo
    global tablero 
    global intentos_restantes
    if perdio_gano == 0:
        menu_top = pygame.draw.rect(pantalla, purpura2, [0,0,ancho,100])
        fondo = pygame.draw.rect(pantalla, purpura1, [0,100,ancho,alto])
        tablero = pygame.Rect(0,0,ancho-200, alto-200)
        tablero.center = fondo.center
        pygame.draw.rect(pantalla, gris,tablero)
        texto_titulo = fuente_titulo.render('Juego de Memoria',True,blanco)
        texto_titulo_dibujado = texto_titulo.get_rect()
        texto_titulo_dibujado.center = menu_top.center
        pantalla.blit(texto_titulo,texto_titulo_dibujado)
        
        
        texto_punteo = fuente_texto.render(f'Puntos: {puntuacion}',True,blanco)
        texto_punteo_dibujado = texto_punteo.get_rect()
        texto_punteo_dibujado.center = menu_top.midleft
        pantalla.blit(texto_punteo,[ancho-200,10])
        
        texto_punteo = fuente_texto.render(f'Tiempo: {tiempo_jugando//50}',True,blanco)
        texto_punteo_dibujado = texto_punteo.get_rect()
        texto_punteo_dibujado.center = menu_top.midleft
        pantalla.blit(texto_punteo,[ancho-200,30])
        
        texto_punteo = fuente_texto.render(f'Intentos ret: {intentos_restantes }',True,blanco)
        texto_punteo_dibujado = texto_punteo.get_rect()
        texto_punteo_dibujado.center = menu_top.midleft
        pantalla.blit(texto_punteo,[ancho-200,50])
        
        boton_salir = pygame.draw.rect(pantalla,purpura1, [10,menu_top.centery-25, 250, 50],0,4)
        texto_boton_SALIR = fuente_texto.render(f'SALIR',True,blanco)
        texto_boton_SALIR_dibujado = texto_boton_SALIR.get_rect()
        texto_boton_SALIR_dibujado.center = boton_salir.center
        pantalla.blit(texto_boton_SALIR,texto_boton_SALIR_dibujado)
    else:        
        fondo = pygame.draw.rect(pantalla, purpura1, [0,0,ancho,alto])
    
    
    
    
    #menu_bot = pygame.draw.rect(pantalla, purpura2, [0,alto-100,ancho,100])

mostrar_todos_los_numero = True
esperar_delay = False
boton_juego_nuevo = pygame.draw.rect(pantalla,purpura2, [475,375, 250, 50],0,4)
boton_salir =  pygame.draw.rect(pantalla,purpura2, [475,335, 250, 50],0,4)

def dibuja_tablero(modo_juego:int=0):
    global fil_m1
    global col_m1
    global espacios
    lista_botones = []
    global esperar_delay
    global boton_juego_nuevo
    global boton_salir
    if perdio_gano == 0:
        if esperar_delay:
            pygame.time.delay(750)
            esperar_delay = False
        
        if modo_juego == 0:
            for i in range(fil_m1):
                for j in range(col_m1):
                    carta = pygame.draw.rect(pantalla,purpura2, [i * 150 + 250, j * 150 + 190, 120, 120],0,4)
                    lista_botones.append(carta)
        elif modo_juego == 1:
            for i in range(fil_m2):
                for j in range(col_m2):
                    carta = pygame.draw.rect(pantalla,purpura2, [i * 150 + 170, j * 150 + 190, 120, 120],0,4)
                    lista_botones.append(carta)
                    carta_texto = fuente_texto.render(f'{espacios[(i * col_m2 + j)]}',True,blanco)
                    carta_texto_dibujado = carta_texto.get_rect()
                    carta_texto_dibujado.center = carta.center
                    if mostrar_todos_los_numero:
                        pantalla.blit(carta_texto,carta_texto_dibujado)
                    elif len(lista_botones) -1 == primer_click_id or len(lista_botones) -1 == segundo_click_id:
                        pantalla.blit(carta_texto,carta_texto_dibujado)
                    if tablero_hist[j][i] == 1:                    
                        pygame.draw.rect(pantalla,purpura1, [i * 150 + 170, j * 150 + 190, 120, 120],5,4)
                        pantalla.blit(carta_texto,carta_texto_dibujado)
    elif perdio_gano == 1:
        enunciado_texto = fuente_titulo.render(f'GANÓ',True,blanco)
        enunciado_texto_dibujado = enunciado_texto.get_rect()
        enunciado_texto_dibujado.center = fondo.center
        pantalla.blit(enunciado_texto,enunciado_texto_dibujado)
        
        boton_juego_nuevo = pygame.draw.rect(pantalla,purpura2, [475,375, 250, 50],0,4)
        texto_boton_juegoNuevo = fuente_texto.render(f'JUGAR DE NUEVO',True,blanco)
        texto_boton_juegoNuevo_dibujado = texto_boton_juegoNuevo.get_rect()
        texto_boton_juegoNuevo_dibujado.center = boton_juego_nuevo.center
        pantalla.blit(texto_boton_juegoNuevo,texto_boton_juegoNuevo_dibujado)
    elif perdio_gano == 2:
        enunciado_texto = fuente_titulo.render(f'PERDIÓ',True,blanco)
        enunciado_texto_dibujado = enunciado_texto.get_rect()
        enunciado_texto_dibujado.center = fondo.center
        pantalla.blit(enunciado_texto,enunciado_texto_dibujado)
        
        boton_juego_nuevo = pygame.draw.rect(pantalla,purpura2, [475,375, 250, 50],0,4)
        texto_boton_juegoNuevo = fuente_texto.render(f'JUGAR DE NUEVO',True,blanco)
        texto_boton_juegoNuevo_dibujado = texto_boton_juegoNuevo.get_rect()
        texto_boton_juegoNuevo_dibujado.center = boton_juego_nuevo.center
        pantalla.blit(texto_boton_juegoNuevo,texto_boton_juegoNuevo_dibujado)
    elif perdio_gano == 3:
        enunciado_texto = fuente_titulo.render(f'JUEGO DE MEMORIA',True,blanco)
        enunciado_texto_dibujado = enunciado_texto.get_rect()
        enunciado_texto_dibujado.center = fondo.center
        pantalla.blit(enunciado_texto,[420,200])
        
        boton_juego_nuevo = pygame.draw.rect(pantalla,purpura2, [475,270, 250, 50],0,4)
        texto_boton_juegoNuevo = fuente_texto.render(f'EMPEZAR',True,blanco)
        texto_boton_juegoNuevo_dibujado = texto_boton_juegoNuevo.get_rect()
        texto_boton_juegoNuevo_dibujado.center = boton_juego_nuevo.center
        pantalla.blit(texto_boton_juegoNuevo,texto_boton_juegoNuevo_dibujado)
        
        
        boton_salir = pygame.draw.rect(pantalla,purpura2, [475,335, 250, 50],0,4)
        texto_boton_SALIR = fuente_texto.render(f'SALIR',True,blanco)
        texto_boton_SALIR_dibujado = texto_boton_SALIR.get_rect()
        texto_boton_SALIR_dibujado.center = boton_salir.center
        pantalla.blit(texto_boton_SALIR,texto_boton_SALIR_dibujado)
        

    
                
                    
    return lista_botones

def ver_gana_pierde():
    global intentos_restantes
    global parejas
    global perdio_gano
    if intentos_restantes <= 0:
        perdio_gano = 2
        return 
    elif parejas >= 9:
        perdio_gano = 1
        return 

def verifica_pareja(primer_id, segundo_id):
    
    global puntuacion
    global parejas
    global intentos_restantes
    if espacios[primer_id] == espacios[segundo_id]:
        
        x1 = (primer_id//col_m2)
        y1 = (primer_id%col_m2)
        x2 = (segundo_id//col_m2)
        y2 = (segundo_id%col_m2)
        
        if(tablero_hist[y1][x1] == 0 and tablero_hist[y2][x2] == 0):
            tablero_hist[y1][x1],tablero_hist[y2][x2] = 1, 1
            puntuacion += 1
            parejas += 1
        return True
    else:
        intentos_restantes -= 1
        return False
    


def reinicia_juego(tipo_juego=0):
    global tiempo_jugando
    global tablero_hist
    global lista_cartas
    global espacios
    global repetidos
    
    tablero_hist=  [[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0]]

    lista_cartas=[]
    espacios=[]
    repetidos = []
    tiempo_jugando=0
    
    global puntuacion
    global parejas
    global primer_click
    global segundo_click
    global primer_click_id
    global segundo_click_id
    global mostrar_todos_los_numero 
    global intentos_restantes
    intentos_restantes = 27
    mostrar_todos_los_numero=True
    
    puntuacion=0
    parejas=0

    primer_click = False
    segundo_click = False
    primer_click_id = -1
    segundo_click_id = -1
    desordenar_tabalero()
    return  

def click_sonido():
    pygame.mixer.fadeout(1000)
    pygame.mixer.Sound('sonido/card_tap.wav').play().set_volume(0.2)

jugando = True


pygame.mixer.music.load('sonido/sonido_fondo.wav')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

while jugando:
    timer.tick(fps)
    pantalla.fill(purpura1)
    tiempo_jugando += 1
    timer_segundo_click_falso = 0
    
    if juego_nuevo:
        reinicia_juego()
        juego_nuevo = False
    if tiempo_jugando > 100:
        mostrar_todos_los_numero = False
        
    dibuja_layout();
     
    tablero_botones = dibuja_tablero(1)   
    
    if primer_click and segundo_click:
        verifica_pareja(primer_click_id,segundo_click_id)
        esperar_delay = True
        primer_click,segundo_click = False,False
        primer_click_id, segundo_click_id = -1,-1
        ver_gana_pierde()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if boton_salir.collidepoint(event.pos):                
                jugando = False
            if perdio_gano == 0:
                for i in range(len(tablero_botones)):
                    
                    aux_boton = tablero_botones[i]
                    if aux_boton.collidepoint(event.pos) and not primer_click:
                        click_sonido()
                        primer_click = True
                        primer_click_id=i
                    elif aux_boton.collidepoint(event.pos) and not segundo_click and primer_click_id != i :
                        click_sonido()
                        segundo_click = True
                        segundo_click_id=i
            else:
                if boton_juego_nuevo.collidepoint(event.pos):
                    perdio_gano = 0
                    reinicia_juego(1)
    
        
                   
            
            
    pygame.display.flip()
pygame.quit()