# HOW TO CHANGE DEFAULT PYTHON2 TO PYTHON3 ON VSC

# 1. Open Visual Studio Code on your Mac.

# 2. Cntrl + , (comma) to directly open the settings.

# 3. search for "code-runner.executorMap".

# 4. Change this code:

# "code-runner.executorMap": {
#     "python": "python3",
# }

# 5. Save the file




# 1. Import pygame, create window and create game loop
# 2. Explain RGB(0, 0, 0) --> https://www.w3schools.com/colors/colors_rgb.asp
# 3. Add colors functionality


import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))

# colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
color_index = 0
# // colors

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # colors
    elif event.type == pygame.KEYDOWN:
      color_index = (color_index + 1) % len(colors)
  win.fill(colors[color_index])
  # // colors
  pygame.display.flip()
pygame.quit()