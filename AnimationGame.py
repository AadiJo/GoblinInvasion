import pygame
import sys
import os.path

__DEBUG_MODE__ = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pygame.init()
pygame.display.init()

W = 800
H = 480

win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Goblin Invasion")

pygame.mixer.init()
music = pygame.mixer.music.load(resource_path('Game/music.mp3'))
pygame.mixer.music.play(-1)

Skull = pygame.image.load(resource_path('Game\Skull.png'))
bg = pygame.image.load(resource_path('Game/bg.jpg'))

clock = pygame.time.Clock()

damage = 0.1
bg_hits = round(10 / damage)

amo = 500

hits = bg_hits
score = 0
start_ticks = pygame.time.get_ticks()
lives = 7

points = 0


class player(object):
    walkRight = [pygame.image.load(resource_path('Game\R1.png')),
                 pygame.image.load(resource_path('Game\R2.png')),
                 pygame.image.load(resource_path('Game\R3.png')),
                 pygame.image.load(resource_path('Game\R4.png')),
                 pygame.image.load(resource_path('Game\R5.png')),
                 pygame.image.load(resource_path('Game\R6.png')),
                 pygame.image.load(resource_path('Game\R7.png')),
                 pygame.image.load(resource_path('Game\R8.png')),
                 pygame.image.load(resource_path('Game\R9.png'))]
    walkLeft = [pygame.image.load(resource_path('Game\L1.png')),
                pygame.image.load(resource_path('Game\L2.png')),
                pygame.image.load(resource_path('Game\L3.png')),
                pygame.image.load(resource_path('Game\L4.png')),
                pygame.image.load(resource_path('Game\L5.png')),
                pygame.image.load(resource_path('Game\L6.png')),
                pygame.image.load(resource_path('Game\L7.png')),
                pygame.image.load(resource_path('Game\L8.png')),
                pygame.image.load(resource_path('Game\L9.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitCount = 0
        self.jumpCount = 10
        self.standing = True
        self.alive = True
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, window):
        if self.alive:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not self.standing:
                if self.left:
                    window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    window.blit(self.walkRight[0], (self.x, self.y))
                else:
                    window.blit(self.walkLeft[0], (self.x, self.y))
            self.hit_box = (self.x + 17, self.y + 11, 29, 52)
            # pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)

    def hit(self):
        if self.alive:
            self.isJump = False
            self.jumpCount = 10
            if self.x < (W / 2):
                self.x += 100
            if self.x > (W / 2):
                self.x -= 200
            self.y = 410
            self.walkCount = 0
            font1 = pygame.font.SysFont('timesnewroman', 100)
            self.hitCount += 1
            text = font1.render('-1', 1, (255, 0, 0))
            win.blit(text, (200, 200))
            text = font1.render('-2', 1, (0, 0, 255))
            win.blit(text, (500, 200))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1


class projectile(object):
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = direction
        self.vel = 10 * direction
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load(resource_path('Game\R1E.png')),
                 pygame.image.load(resource_path('Game\R2E.png')),
                 pygame.image.load(resource_path('Game\R3E.png')),
                 pygame.image.load(resource_path('Game\R4E.png')),
                 pygame.image.load(resource_path('Game\R5E.png')),
                 pygame.image.load(resource_path('Game\R6E.png')),
                 pygame.image.load(resource_path('Game\R7E.png')),
                 pygame.image.load(resource_path('Game\R8E.png')),
                 pygame.image.load(resource_path('Game\R9E.png')),
                 pygame.image.load(resource_path('Game\R10E.png')),
                 pygame.image.load(resource_path('Game\R11E.png'))]
    walkLeft = [pygame.image.load(resource_path('Game\L1E.png')),
                pygame.image.load(resource_path('Game\L2E.png')),
                pygame.image.load(resource_path('Game\L3E.png')),
                pygame.image.load(resource_path('Game\L4E.png')),
                pygame.image.load(resource_path('Game\L5E.png')),
                pygame.image.load(resource_path('Game\L6E.png')),
                pygame.image.load(resource_path('Game\L7E.png')),
                pygame.image.load(resource_path('Game\L8E.png')),
                pygame.image.load(resource_path('Game\L9E.png')),
                pygame.image.load(resource_path('Game\L10E.png')),
                pygame.image.load(resource_path('Game\L11E.png'))]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 7
        self.hit_box = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.dead = False

    def draw(self, window):
        self.move()
        if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.vel > 0:
                    window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.vel < 0:
                    window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1

                pygame.draw.rect(window, (0, 128, 0), (self.hit_box[0], self.hit_box[1] - 20, 50, 10))
                pygame.draw.rect(window, (255, 0, 0), (self.hit_box[0], self.hit_box[1] - 20, 50 - (5 * (10 - self.health)),
                                                       10))
                self.hit_box = (self.x + 17, self.y + 2, 31, 57)
                # pygame.draw.rect(win, (255,0,0), self.hit_box,2)
        if self.dead:
            text2 = font.render('Goblin Defeated!', 1, (255, 255, 0))
            win.blit(text2, (400, 250))

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= damage
        else:
            self.visible = False


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Hits Needed: ' + str(hits), 1, (0, 0, 0))
    win.blit(text, (450, 10))
    text = font.render('Hits Scored: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (450, 40))
    text = font.render('Points: ' + str(points), 1, (0, 0, 255))
    win.blit(text, (200, 40))
    text = font.render('Lives: ' + str(lives), 1, (255, 0, 0))
    win.blit(text, (200, 10))
    font1 = pygame.font.SysFont('timesnewroman', 50, True)
    text = font1.render('Goblin Invasion!', 1, (0, 128, 0))
    win.blit(text, (230, 100))
    if hits == 0:
        if points == bg_hits:
            text = font.render('Perfect Game!', 1, (0, 0, 255))
            win.blit(text, (380, 280))
        if bg_hits > points >= score - (bg_hits / 20):
            text = font.render('Good Game!', 0, (0, 0, 255))
            win.blit(text, (380, 280))
        if points < bg_hits / 2:
            text = font.render('Better luck next time', 0, (0, 0, 255))
            win.blit(text, (320, 280))
        if bg_hits - (bg_hits / 10) > points >= bg_hits - (bg_hits / 2):
            text = font.render('Fair Game!', 0, (0, 0, 255))
            win.blit(text, (380, 280))

    if lives <= 0:
        win.fill((0, 0, 0))
        man.alive = False
        goblin.visible = False
        win.blit(Skull, (150, 0))
        pygame.mixer.music.pause()
        text = font.render('You Died', 1, (255, 0, 0))
        win.blit(text, (350, 40))

    man.draw(win)
    goblin.draw(win)
    for x in bullets:
        x.draw(win)

    pygame.display.update()


def redrawLoadWindow():
    win.blit(bg, (0, 0))
    font1 = pygame.font.SysFont('timesnewroman', 50, True)
    text = font1.render('Goblin Invasion!', 1, (0, 128, 0))
    win.blit(text, (230, 100))
    text = font1.render('Press a key to Start!', 1, (0, 0, 128))
    win.blit(text, (210, 150))
    #text = font.render('Use the left and right arrow keys to move around', 1, (128, 0, 0))
    #win.blit(text, (180, 200))
    #text = font.render('Use the up arrow key to jump', 1, (128, 0, 0))
    #win.blit(text, (200, 240))
    #text = font.render('Use the spacebar to shoot', 1, (128, 0, 0))
    #win.blit(text, (200, 280))
    #text = font.render('Destroy the Goblin!', 1, (128, 0, 0))
    #win.blit(text, (250, 320))
    pygame.display.update()


def startScreen(start):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type in (pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT):
                running = False
                start = False
                return start


# mainloop
font = pygame.font.SysFont('timesnewroman', 30, True)
man = player(500, 410, 64, 64)
goblin = enemy(10, 410, 64, 64, (W - 50))
event = pygame.event.wait()
shootLoop = 0
bullets = []
run = False
start = True
while start:
    redrawLoadWindow()
    start = startScreen(start)

run = True
while run:
    clock.tick(40)

    point2 = points
    if goblin.visible:
        if man.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and man.hit_box[1] + man.hit_box[3] > \
                goblin.hit_box[1]:
            if man.hit_box[0] + man.hit_box[2] > goblin.hit_box[0] and man.hit_box[0] < goblin.hit_box[0] + \
                    goblin.hit_box[2]:
                man.hit()
                points -= 2
                lives -= 1

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hit_box[1] + goblin.hit_box[3] and bullet.y + bullet.radius > \
                goblin.hit_box[1]:
            if bullet.x + bullet.radius > goblin.hit_box[0] and bullet.x - bullet.radius < goblin.hit_box[0] + \
                    goblin.hit_box[2]:
                goblin.hit()
                hits -= 1
                score += 1
                points += 1
                bullets.pop(bullets.index(bullet))

        if W > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < amo:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < W - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    if hits == 0:
        man.isJump = True
        man.right = True
        man.left = False
        goblin.visible = False
        goblin.dead = True
        man.x = 190
        # pygame.mixer.music.stop()

    if score > bg_hits:
        score -= 1

    if hits < 0:
        hits += 1
        if points > point2:
            points -= 1

    redrawGameWindow()

pygame.quit()
