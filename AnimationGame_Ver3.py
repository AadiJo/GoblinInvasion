import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Aadi's Game")


walkRight = [pygame.image.load('Game\R1.png'),
             pygame.image.load('Game\R2.png'),
             pygame.image.load('Game\R3.png'),
             pygame.image.load('Game\R4.png'),
             pygame.image.load('Game\R5.png'),
             pygame.image.load('Game\R6.png'),
             pygame.image.load('Game\R7.png'),
             pygame.image.load('Game\R8.png'),
             pygame.image.load('Game\R9.png')]
walkLeft = [pygame.image.load('Game\L1.png'),
            pygame.image.load('Game\L2.png'),
            pygame.image.load('Game\L3.png'),
            pygame.image.load('Game\L4.png'),
            pygame.image.load('Game\L5.png'),
            pygame.image.load('Game\L6.png'),
            pygame.image.load('Game\L7.png'),
            pygame.image.load('Game\L8.png'),
            pygame.image.load('Game\L9.png')]
bg = pygame.image.load('Game/bg.jpg')

clock = pygame.time.Clock()

damage = 0.1
bg_hits = round(10 / damage)

hits = bg_hits
score = 0
start_ticks = pygame.time.get_ticks()

music = pygame.mixer.music.load('Game\music.mp3')
pygame.mixer.music.play(-1)

points = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        if self.x < 250:
            self.x += 100
        if self.x > 250:
            self.x -= 200
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('timesnewroman', 100)
        text = font1.render('-2', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
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
        self.vel = 8 * direction

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('Game\R1E.png'),
                 pygame.image.load('Game\R2E.png'),
                 pygame.image.load('Game\R3E.png'),
                 pygame.image.load('Game\R4E.png'),
                 pygame.image.load('Game\R5E.png'),
                 pygame.image.load('Game\R6E.png'),
                 pygame.image.load('Game\R7E.png'),
                 pygame.image.load('Game\R8E.png'),
                 pygame.image.load('Game\R9E.png'),
                 pygame.image.load('Game\R10E.png'),
                 pygame.image.load('Game\R11E.png')]
    walkLeft = [pygame.image.load('Game\L1E.png'),
                pygame.image.load('Game\L2E.png'),
                pygame.image.load('Game\L3E.png'),
                pygame.image.load('Game\L4E.png'),
                pygame.image.load('Game\L5E.png'),
                pygame.image.load('Game\L6E.png'),
                pygame.image.load('Game\L7E.png'),
                pygame.image.load('Game\L8E.png'),
                pygame.image.load('Game\L9E.png'),
                pygame.image.load('Game\L10E.png'),
                pygame.image.load('Game\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 10
        self.hit_box = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, window):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(window, (0, 128, 0), (self.hit_box[0], self.hit_box[1] - 20, 50, 10))
            pygame.draw.rect(window, (255, 0, 0), (self.hit_box[0], self.hit_box[1] - 20, 50 - (5 * (10 - self.health)),
                                                   10))
            self.hit_box = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255,0,0), self.hit_box,2)
        else:
            text2 = font.render('Goblin Defeated!', 1, (255, 255, 0))
            win.blit(text2, (150, 250))

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
    win.blit(text, (250, 10))
    text = font.render('Hits Scored: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (250, 40))
    text = font.render('Points: ' + str(points), 1, (255, 0, 0))
    win.blit(text, (50, 40))
    if hits == 0:
        if points == bg_hits:
            text = font.render('Perfect Game!', 1, (0, 0, 255))
            win.blit(text, (150, 280))
        if bg_hits > points >= score - (bg_hits / 20):
            text = font.render('Good Game!', 0, (0, 0, 255))
            win.blit(text, (150, 280))
        if points < bg_hits / 2:
            text = font.render('Better luck next time', 0, (0, 0, 255))
            win.blit(text, (130, 280))
        if bg_hits - (bg_hits / 10) > points >= bg_hits - (bg_hits / 2):
            text = font.render('Fair Game!', 0, (0, 0, 255))
            win.blit(text, (150, 280))

    man.draw(win)
    goblin.draw(win)
    for x in bullets:
        x.draw(win)

    pygame.display.update()


# mainloop
font = pygame.font.SysFont('timesnewroman', 30, True)
man = player(200, 410, 64, 64)
goblin = enemy(10, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)
    point2 = points
    if goblin.visible:
        if man.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and man.hit_box[1] + man.hit_box[3] > \
                goblin.hit_box[1]:
            if man.hit_box[0] + man.hit_box[2] > goblin.hit_box[0] and man.hit_box[0] < goblin.hit_box[0] + \
                    goblin.hit_box[2]:
                man.hit()
                points -= 2

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

        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 500:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
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
        goblin.visible = False
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
