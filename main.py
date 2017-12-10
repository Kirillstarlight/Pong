import sys

from pygame.locals import *

from gamePackage.GameClass import *

# Set up the colours


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window_width = 960
window_height = 480

display_surf = pygame.display.set_mode((window_width, window_height))

fps_clock = pygame.time.Clock()
fps = 60  # Number of frames per second

music_volume = 0.5


# Main function
def main(music_volume=music_volume, fps=fps):
    pygame.mixer.pre_init(22050, -16, 2, 4096)
    pygame.init()
    pygame.mixer.music.load("04 - I'll Keep Coming.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('Pong')
    pygame.mouse.set_visible(0)  # make cursor invisible

    game = Game(speed=3)

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse movement commands
            elif event.type == MOUSEMOTION:
                game.paddles['user'].move(event.pos)
            if (game.ball.pass_player()):
                pygame.mixer.music.rewind()
        game.update()
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
