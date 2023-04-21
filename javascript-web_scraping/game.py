import pygame
import random

# Lee la historia en inglés desde un archivo de texto y almacena las palabras en una lista
with open('historia.txt', 'r') as f:
    historia = f.read()
palabras = historia.split()

# Inicializa Pygame
pygame.init()

# Crea la ventana del juego
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Juego de escritura')

# Fuente para mostrar el tiempo transcurrido
fuente = pygame.font.Font(None, 36)

# Bucle principal del juego
while True:
    # Carga una palabra aleatoria de la historia
    palabra_aleatoria = random.choice(palabras)

    # Inicia el temporizador
    tiempo_inicio = pygame.time.get_ticks()

    # Muestra la palabra aleatoria en la pantalla y espera a que el jugador la escriba
    entrada_usuario = ''
    while entrada_usuario != palabra_aleatoria:
        # Manejo de eventos de Pygame
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                # Agrega la tecla presionada a la entrada del usuario
                entrada_usuario += pygame.key.name(evento.key)

        # Dibuja la palabra aleatoria y la entrada del usuario en la pantalla
        ventana.fill((255, 255, 255))
        palabra_texto = fuente.render(palabra_aleatoria, True, (0, 0, 0))
        entrada_texto = fuente.render(entrada_usuario, True, (0, 0, 0))
        ventana.blit(palabra_texto, (50, 50))
        ventana.blit(entrada_texto, (50, 100))
        pygame.display.flip()

    # Detiene el temporizador y muestra el tiempo que tomó al jugador
    tiempo_fin = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_fin
