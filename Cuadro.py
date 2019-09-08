import pygame 
pygame.init() 

screensizex = int(720/2)
screensizey = int(1280/2)

size = (screensizex,screensizey) #Definir resolución 
#Resolución 5:3 (3DS, inferior)es 800x480 
#Resolución 16:9 (3DS, Superior) es 800x450 
  
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Cuadro que rebota") 
  
BLACK = (0,0,0) 
WHITE = (255,255,255)

#color del cuadro
color = WHITE

pos_x = 50 #Posición Inicial, eje x 
pos_y = 50 #Posición Inicial, eje y

#tamaño del cuadro
size_x = 50
size_y = 50

class DibujarCuadro():
    def __init__(self,pantalla,color,posize):
        self.pantalla = pygame.display.get_surface()
        self.pos_x = 50 #Posición Inicial, eje x 
        self.pos_y = 50 #Posición Inicial, eje y 
        self.pos_change_x = 2 #cambio en x 
        self.pos_change_y = 2 #cambio en y

        #tamaño del cuadro
        self.size_x = 50
        self.size_y = 50

        #color del cuadro
        self.color = WHITE
        
    def updatePos(self, p_x,p_y):
        #incrementos de posición
        self.pos_x = self.pos_x + self.pos_change_x
        self.pos_y = self.pos_y + self.pos_change_y
        p_x = self.pos_x
        p_y = self.pos_y
        #definir vector de info de dimensiones
        self.posize=[self.pos_x, self.pos_y,self.size_x,self.size_y]
        pygame.draw.rect(self.pantalla, self.color, self.posize) #el vector es (lugar,color,[cord_x_inicio, cord_y_inicio, ancho, alto])
        return p_x,p_y


done = False

#definir vector de info de dimensiones
posinfo=[pos_x, pos_y,size_x,size_y]

#A partir de aquí empieza el loop principal del juego 
cuadro1 = DibujarCuadro(screen,color,posinfo)
cuadro2 = DibujarCuadro(screen,color, [-20,-20,cuadro1.size_x,cuadro1.size_y] )

#El reloj se emplea para refrescar pantalla. Framerate. 
clock = pygame.time.Clock() 
  
# -------- Loop Principal ----------- 
while not done: 
# Procesamiento de eventos debe ir aquí
    for event in pygame.event.get(): # El usuario hizo algo 1tab 
        if event.type == pygame.QUIT: #2 tabs 
            print("El usuario decidió salir") #3 tabs 
            done = True # Activar bandera para salir del ciclo For. #3 tabs 
        elif event.type == pygame.KEYDOWN: #2 tabs 
            print("El Usuario presionó una tecla.") #3 tabs 
        elif event.type == pygame.KEYUP: #2tabs 
            print("El Usuario soltó la tecla.") #3tabs 
        elif event.type == pygame.MOUSEBUTTONDOWN: #2tabs 
            print("El usuario presionó un botón del mouse") #3tabs 
# Procesamiento de eventos debe ir antes de este comentario. 
        
    # El engine del juego debe ir aquí abajo.  
    #----------------------- a 1 tab para que entre en el while. 
    # El engine del juego debe ir arriba. 
  
# El código para dibujar pantalla debe ir aquí abajo. 

    screen.fill(BLACK) #Escribe pantalla en blanco 
    #pygame.draw.rect(screen, WHITE, [pos_x, pos_y, 50,50]) #el vector es (lugar,color,[cord_x_inicio, cord_y_inicio, ancho, alto]) 
    
    poscuadro1 = cuadro1.updatePos(cuadro1.pos_x,cuadro1.pos_y)
    poscuadro2 = cuadro2.updatePos(cuadro2.pos_x,cuadro2.pos_y)
    
    print(poscuadro1)
    
#generar rebote al llegar a la pantalla.     
#    if pos_y > screensizey-size_y or pos_y < 0: 
#        pos_change_y = pos_change_y * -1 
#    if pos_x > screensizex-size_x or pos_x < 0:
#        pos_change_x = pos_change_x * -1
#    pygame.display.flip() #Muestra en pantalla
#    clock.tick(60) #Dibuja a 60 fps (max) 

#generar rebote al llegar al techo.
    if cuadro1.pos_y > screensizey-size_y or cuadro1.pos_y < 0: 
        cuadro1.pos_change_y = cuadro1.pos_change_y * -1 

#Generar efecto de cilindro a los lados
#    if pos_x > screensizex:
#        posinfo_aux=[cuadro1.pos_x-screensizex,cuadro1.pos_y,cuadro1.size_x,cuadro1.size_y]
#        cuadro2 = DibujarCuadro(screen,color,posinfo_aux)

    if cuadro1.pos_x > screensizex-size_x or cuadro1.pos_x < 0:
        cuadro1.pos_change_x = cuadro1.pos_change_x * -1
    
    pygame.display.flip() #Muestra en pantalla
    clock.tick(60) #Dibuja a 60 fps (max) 


# El código para dibujar pantalla debe ir arriba 
  
pygame.quit() #Cierra el juego.  
