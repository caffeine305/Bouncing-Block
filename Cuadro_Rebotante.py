import pygame
pygame.init()

size = (800,450) #Definir resolución
#Resolución 5:3 (3DS, inferior)es 800x480
#Resolución 16:9 (3DS, Superior) es 800x450

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cuadro que rebota")

BLACK = (0,0,0)
WHITE = (255,255,255)

pos_x = 50 #Posición Inicial, eje x
pos_y = 50 #Posición Inicial, eje y
pos_change_x = 2 #cambio en x
pos_change_y = 2 #cambio en y

#A partir de aquí empieza el loop principal del juego
done = False
#El reloj se emplea para refrescar pantalla. Framerate.
clock = pygame.time.Clock()

# -------- Loop Principal -----------
while not done:
# Procesamiento de eventos debe ir después de este comentario.
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
    pygame.draw.rect(screen, WHITE, [pos_x, pos_y, 50,50]) #el vector es (lugar,color,[cord_x_inicio, cord_y_inicio, ancho, alto])
#incrementos de posición
    pos_x += pos_change_x 
    pos_y += pos_change_y
#generar rebote al llegar a la pantalla.    
    if pos_y > 400 or pos_y < 0:
        pos_change_y = pos_change_y * -1
    if pos_x > 750 or pos_x < 0:
        pos_change_x = pos_change_x * -1
    pygame.display.flip() #Muestra en pantalla 
    clock.tick(60) #Dibuja a 60 fps (max)
    # El código para dibujar pantalla debe ir arriba


pygame.quit() #Cierra el juego. 
