import pygame


class boton:
    def __init__(self, pantalla ,texto, size, bg_color, txt_color, fuente,id, x_position,y_position):
      self.screen = pantalla
      self.screen_rect = self.screen.get_rect()
      self.width, self.height = size
      self.bg_color = bg_color
      self.txt_color = txt_color
      self.font = fuente
      self.id= id
      
      self.rect= pygame.Rect(x_position,y_position,self.width,self.height)
      
      self.dibuja_texto(texto)
    
    def dibuja_texto(self, texto):
        self.texto_dibujado = self.font.render(texto,True,self.txt_color,self.bg_color)
        self.texto_dibujado_rect = self.texto_dibujado.get_rect()
        self.texto_dibujado_rect.center = self.rect.center
    
    def dibuja_boton(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.texto_dibujado,self.texto_dibujado_rect)
        
    def cambia_color(self,color):
      self.bg_color = color
      self.dibuja_boton()
      