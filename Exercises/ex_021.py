import pygame

pygame.init()
pygame.mixer.music.load('../assets/Relaxing.mp3')
pygame.mixer.music.play()
# Keep the program running and processing events
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Sleep for a short period to allow the music to play
