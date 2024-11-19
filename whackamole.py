import pygame
import random
import time

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        moleX = 0
        moleY = 0
        molerect = mole_image.get_rect(topleft = (moleX, moleY))
        screen.blit(mole_image, mole_image.get_rect(topleft=(moleX, moleY)))

        mouseX=0
        mouseY=0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    mouseX = event.pos[0] // 32
                    mouseY = event.pos[1] // 32

                    if mouseX == moleX // 32 and mouseY == moleY // 32:
                        moleX = random.randrange(20) * 32
                        moleY = random.randrange(16) * 32
                        molerect.topleft = (moleX, moleY)

            screen.fill("light green")

            #grid
            for i in range(0,640,32): #sets the vertical lines
                pygame.draw.line(screen, "dark blue", (32+i,0), (32+i, 512))
            for i in range(0,512,32): #sets the horizontal lines
                pygame.draw.line(screen, "dark blue", (0, 32+i), (640, 32+i))

            screen.blit(mole_image, molerect)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
