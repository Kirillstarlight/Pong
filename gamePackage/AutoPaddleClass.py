from gamePackage.PaddleClass import Paddle
from main import window_height


class AutoPaddle(Paddle):
    def __init__(self, x, w, h, ball, speed):
        super().__init__(x, w, h)
        self.ball = ball
        self.speed = speed

    def move(self):
        # If ball is moving away from paddle, center bat
        if self.ball.dir_x == -1:
            if self.rect.centery < int(window_height / 2):
                self.rect.y += self.speed
            elif self.rect.centery > int(window_height / 2):
                self.rect.y -= self.speed
        # if ball moving towards bat, track its movement.
        elif self.ball.dir_x == 1:
            if self.rect.centery < self.ball.rect.centery:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed