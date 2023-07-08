
# 1. Explain that everything is an object in pygame
# 2. Create game loop
# 3. Draw rectangle for both of the players
# 4. Draw ball
# 5. Make the players move

import pygame

pygame.init()
win = pygame.display.set_mode((800, 600)) # (width, height)

player1_y = 270

def move_arrow_up():
  player1_y += 1

running = True
while running:
  for event in pygame.event.get():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), pygame.Rect(30, player1_y, 10, 60)) # pygame.Rect(x, y, width, height)
    pygame.draw.rect(win, (255, 255, 255), pygame.Rect(770, 270, 10, 60)) # pygame.Rect(x, y, width, height)
    pygame.draw.circle(win, (255, 255, 255), (400, 300), 6) # pygame.draw.circle(window, color, (x, y), radius)
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        player1_y += 5
      elif event.key == pygame.K_s:
        print(pygame.KEYDOWN)
  pygame.display.flip()
pygame.quit()