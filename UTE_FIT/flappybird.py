import pygame
import sys
import random
from dataclasses import dataclass

# -----------------------------
# Config
# -----------------------------
W, H = 432, 768
GROUND_H = 100
PIPE_GAP = 180
PIPE_DISTANCE = 250
PIPE_SPEED = 3.2
GRAVITY = 0.35
FLAP_STRENGTH = -7.8
FPS = 60
FONT_NAME = "arial"

# Bot tuning
BOT_ENABLED_DEFAULT = True
AIM_AHEAD_PX = 60         # flap a bit before the pipe
TARGET_OFFSET = -8         # aim slightly above gap center
VELOCITY_LOOKAHEAD = 5     # compensate for current vertical speed

# -----------------------------
# Helpers
# -----------------------------
@dataclass
class Bird:
    x: float
    y: float
    vy: float = 0.0
    angle: float = 0.0
    alive: bool = True
    radius: int = 18

    def rect(self):
        return pygame.Rect(int(self.x - self.radius), int(self.y - self.radius), self.radius*2, self.radius*2)

    def update(self):
        self.vy += GRAVITY
        self.y += self.vy
        # tilt up/down for eye-candy
        self.angle = max(-25, min(70, -self.vy * 3))

    def flap(self):
        self.vy = FLAP_STRENGTH

@dataclass
class Pipe:
    x: float
    gap_y: float
    width: int = 70
    passed: bool = False

    def rects(self):
        top_rect = pygame.Rect(int(self.x), 0, self.width, int(self.gap_y - PIPE_GAP/2))
        bottom_rect = pygame.Rect(int(self.x), int(self.gap_y + PIPE_GAP/2), self.width, H - GROUND_H - int(self.gap_y + PIPE_GAP/2))
        return top_rect, bottom_rect

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("Flappy Bird - Autoplay Bot")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(FONT_NAME, 28)
        self.small = pygame.font.SysFont(FONT_NAME, 20)

        self.reset()

    def reset(self):
        self.bird = Bird(x=W*0.25, y=H*0.5)
        self.pipes = []
        self.spawn_timer = 0
        self.score = 0
        self.best = getattr(self, "best", 0)
        self.bot_enabled = BOT_ENABLED_DEFAULT
        self.game_over = False

    def spawn_pipe(self):
        margin_top = 80
        margin_bottom = 80
        gap_y = random.randint(margin_top + int(PIPE_GAP/2), H - GROUND_H - margin_bottom - int(PIPE_GAP/2))
        x = W + 10
        self.pipes.append(Pipe(x=x, gap_y=gap_y))

    def handle_collisions(self):
        # Ground / ceiling
        if self.bird.y + self.bird.radius >= H - GROUND_H or self.bird.y - self.bird.radius <= 0:
            self.die()
            return
        # Pipes
        brect = self.bird.rect()
        for pipe in self.pipes:
            top_rect, bot_rect = pipe.rects()
            if brect.colliderect(top_rect) or brect.colliderect(bot_rect):
                self.die()
                return

    def die(self):
        self.bird.alive = False
        self.game_over = True
        self.best = max(self.best, self.score)

    def nearest_pipe(self):
        # Return pipe ahead of the bird
        pipes_ahead = [p for p in self.pipes if p.x + p.width > self.bird.x]
        if not pipes_ahead:
            return None
        return min(pipes_ahead, key=lambda p: p.x)

    def bot_logic(self):
        """Simple rule-based bot: aim for the center of the next gap.
        Flap if the bird is below a slightly offset target line, with some lookahead and velocity compensation.
        """
        target_pipe = self.nearest_pipe()
        if not target_pipe:
            return
        # Predict where bird will be when it reaches the pipe (lookahead horizontally)
        dx = (target_pipe.x - self.bird.x) - AIM_AHEAD_PX
        ticks = max(0, dx / PIPE_SPEED)
        predicted_y = self.bird.y + self.bird.vy * (ticks / 2)  # simple damped prediction

        target_y = target_pipe.gap_y + TARGET_OFFSET
        # Add compensation for current downward velocity
        target_y -= self.bird.vy * VELOCITY_LOOKAHEAD

        if predicted_y > target_y:
            self.bird.flap()

    def update(self, dt):
        if not self.game_over:
            # spawn pipes
            self.spawn_timer += dt
            if self.spawn_timer > PIPE_DISTANCE / PIPE_SPEED:
                self.spawn_timer = 0
                self.spawn_pipe()

            # move pipes
            for p in self.pipes:
                p.x -= PIPE_SPEED
            self.pipes = [p for p in self.pipes if p.x + p.width > -10]

            # scoring
            for p in self.pipes:
                if not p.passed and p.x + p.width < self.bird.x:
                    p.passed = True
                    self.score += 1

            # bot decision
            if self.bot_enabled:
                self.bot_logic()

            # physics
            self.bird.update()
            self.handle_collisions()

    def draw_bird(self):
        # Draw a simple bird: circle with beak; rotate wing line based on angle
        x, y, r = int(self.bird.x), int(self.bird.y), self.bird.radius
        pygame.draw.circle(self.screen, (255, 230, 90), (x, y), r)  # body
        pygame.draw.circle(self.screen, (255, 255, 255), (x+6, y-6), 5)  # eye white
        pygame.draw.circle(self.screen, (0, 0, 0), (x+7, y-6), 2)  # pupil
        beak = [(x+r, y), (x+r+8, y-4), (x+r+8, y+4)]
        pygame.draw.polygon(self.screen, (255, 140, 0), beak)
        # wing (tilt with angle)
        ang = -self.bird.angle * 3.14/180
        wx1, wy1 = x-6, y
        wx2, wy2 = x-6 - int(12 * pygame.math.Vector2(1,0).rotate_rad(ang).x), y - int(12 * pygame.math.Vector2(0,1).rotate_rad(ang).y)
        pygame.draw.line(self.screen, (200, 120, 60), (wx1, wy1), (wx2, wy2), 6)

    def draw_pipes(self):
        for p in self.pipes:
            top_rect, bot_rect = p.rects()
            pygame.draw.rect(self.screen, (80, 200, 120), top_rect)
            pygame.draw.rect(self.screen, (80, 200, 120), bot_rect)
            # pipe rims
            pygame.draw.rect(self.screen, (60, 160, 90), (top_rect.x-2, top_rect.bottom-18, top_rect.width+4, 18))
            pygame.draw.rect(self.screen, (60, 160, 90), (bot_rect.x-2, bot_rect.y, bot_rect.width+4, 18))

    def draw_ground(self, t):
        ground_rect = pygame.Rect(0, H-GROUND_H, W, GROUND_H)
        pygame.draw.rect(self.screen, (220, 200, 160), ground_rect)
        # Simple moving pattern
        for i in range(0, W+80, 40):
            pygame.draw.polygon(self.screen, (200, 180, 140), [(i - (t*80)%40, H-GROUND_H), (i+20 - (t*80)%40, H-GROUND_H), (i-10 - (t*80)%40, H-GROUND_H+20)])

    def draw_ui(self):
        score_surf = self.font.render(f"Score: {self.score}", True, (255,255,255))
        best_surf = self.small.render(f"Best: {self.best}", True, (230,230,230))
        bot_surf = self.small.render(f"Bot: {'ON' if self.bot_enabled else 'OFF'}  (A to toggle)", True, (230,230,230))
        self.screen.blit(score_surf, (16, 16))
        self.screen.blit(best_surf, (16, 52))
        self.screen.blit(bot_surf, (16, 76))
        if self.game_over:
            over = self.font.render("Game Over - R to Restart", True, (255,220,220))
            rect = over.get_rect(center=(W//2, H//2))
            self.screen.blit(over, rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
            if event.key == pygame.K_SPACE and not self.bot_enabled and not self.game_over:
                self.bird.flap()
            if event.key == pygame.K_a:
                self.bot_enabled = not self.bot_enabled
            if event.key == pygame.K_r and self.game_over:
                self.reset()

        if event.type == pygame.MOUSEBUTTONDOWN and not self.bot_enabled and not self.game_over:
            self.bird.flap()

    def run(self):
        t = 0.0
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            t += dt
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                self.handle_input(event)

            self.update(dt)

            # draw
            self.screen.fill((110, 190, 255))
            self.draw_pipes()
            self.draw_bird()
            self.draw_ground(t)
            self.draw_ui()

            pygame.display.flip()

if __name__ == "__main__":
    Game().run()
