import pygame

# initialize Pygame
pygame.init()

# set up the screen
screen_width = 900
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bulls And Cows")

# set up a loop to keep the GUI running
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen update
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render("Bulls And Cows", True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# clean up
pygame.quit()
