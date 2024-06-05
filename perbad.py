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
tiempo_jugando = 0;

primer_click = False
segundo_click = False
primer_click_id = -1
segundo_click_id = -1

fuente_titulo = pygame.font.SysFont("Century Gothic",35)
fuente_texto = pygame.font.SysFont("Century Gothic",20)

perdio_gano = 0

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
    
    global fondo
    global tablero 
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
        pantalla.blit(texto_punteo,[ancho-200,20])
        
        texto_punteo = fuente_texto.render(f'Tiempo: {tiempo_jugando//50}',True,blanco)
        texto_punteo_dibujado = texto_punteo.get_rect()
        texto_punteo_dibujado.center = menu_top.midleft
        pantalla.blit(texto_punteo,[ancho-200,50])
    else:        
        fondo = pygame.draw.rect(pantalla, purpura1, [0,0,ancho,alto])
    
    
    
    
    #menu_bot = pygame.draw.rect(pantalla, purpura2, [0,alto-100,ancho,100])

mostrar_todos_los_numero = True
esperar_delay = False

def dibuja_tablero(modo_juego:int=0):
    global fil_m1
    global col_m1
    lista_botones = []
    global esperar_delay
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

    
                
                    
    return lista_botones


def verifica_pareja(primer_id, segundo_id):
    if espacios[primer_id] == espacios[segundo_id]:
        
        x1 = (primer_id//col_m2)
        y1 = (primer_id%col_m2)
        x2 = (segundo_id//col_m2)
        y2 = (segundo_id%col_m2)
        
        if(tablero_hist[y1][x1] == 0 and tablero_hist[y2][x2] == 0):
            tablero_hist[y1][x1],tablero_hist[y2][x2] = 1, 1
            puntuacion =+ 1
            parejas =+ 1
        return True
    else:
        #puntuacion -= 1
        return False
    


def reinicia_juego():
    return  
jugando = True



while jugando:
    timer.tick(fps)
    pantalla.fill(purpura1)
    tiempo_jugando += 1
    
    timer_segundo_click_falso = 0
    
    if juego_nuevo:
        reinicia_juego()
        desordenar_tabalero()
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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            perdio_gano=1
            for i in range(len(tablero_botones)):
                
                aux_boton = tablero_botones[i]
                if aux_boton.collidepoint(event.pos) and not primer_click:
                    primer_click = True
                    primer_click_id=i
                elif aux_boton.collidepoint(event.pos) and not segundo_click and primer_click_id != i :
                    segundo_click = True
                    segundo_click_id=i
    
        
                   
            
            
    pygame.display.flip()
pygame.quit()