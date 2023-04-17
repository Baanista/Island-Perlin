import generator
import pygame


background_colour = (234, 212, 252)
WINDOW_HIEGHT = 600
WINDOW_WIDTH = 600

screen = pygame.display.set_mode((WINDOW_HIEGHT, WINDOW_WIDTH))


pygame.display.set_caption('Noise Map')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True
mapper = generator.create_noise(500, 10, False, (100, 100), .001, 5)

#mapper = generator.noise_generator(mapper, 0.1)

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()




    square_HEIGHT = WINDOW_HIEGHT / len(mapper)
    square_WIDTH = WINDOW_WIDTH / len(mapper[0])

    for x in range(len(mapper)):
        for y in range(len(mapper[0])):
            #print(mapper[x][y])
            if mapper[x][y] > 1:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * square_WIDTH, y * square_HEIGHT, square_WIDTH, square_HEIGHT))
            else:
                pygame.draw.rect(screen, (255 * mapper[x][y], 255 * mapper[x][y], 255 * mapper[x][y]),
                                 pygame.Rect(x * square_WIDTH, y * square_HEIGHT, square_WIDTH, square_HEIGHT))
            # else:
            #     pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * square_WIDTH, y * square_HEIGHT, square_WIDTH, square_HEIGHT))
    pygame.display.flip()
