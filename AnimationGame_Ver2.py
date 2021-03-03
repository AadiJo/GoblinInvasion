import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Aadi's Game")

walkRight = [pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R1.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R2.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R3.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R4.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R5.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R6.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R7.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R8.png'),
             pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R9.png')]
walkLeft = [pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L1.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L2.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L3.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L4.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L5.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L6.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L7.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L8.png'),
            pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L9.png')]
bg = pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\bg.jpg')

clock = pygame.time.Clock()


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
        self.hit_box = (self.x + 22, self.y + 15, 35, 65)

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

        self.hit_box = (self.x + 22, self.y + 15, 35, 65)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x += 100
        self.walkCount = 0
        font1 = pygame.font.SysFont('timesnewroman', 100)
        text = font1.render('Hit!', 1, (255, 0, 0))
        win.blit(text, (120, 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 101
                    pygame.quit()
                    quit()


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
    walkRight = [pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R1E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R2E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R3E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R4E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R5E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R6E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R7E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R8E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R9E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R10E.png'),
                 pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\R11E.png')]
    walkLeft = [pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L1E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L2E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L3E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L4E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L5E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L6E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L7E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L8E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L9E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L10E.png'),
                pygame.image.load(r'C:\Users\AadiJ\PycharmProjects\GraphicPrograms\GoblinInvasion\Game\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
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
            pygame.draw.rect(window, (255, 0, 0), (self.hit_box[0], self.hit_box[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hit_box = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255,0,0), self.hit_box,2)

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
            self.health -= 0.1
        else:
            self.visible = False


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    man2.draw(win)
    goblin.draw(win)
    goblin2.draw(win)
    goblin3.draw(win)
    goblin4.draw(win)
    goblin5.draw(win)
    goblin6.draw(win)
    for x in bullets:
        x.draw(win)

    pygame.display.update()


# mainloop
man = player(200, 410, 64, 64)
man2 = player(350, 410, 64, 64)
goblin = enemy(10, 410, 64, 64, 205)
goblin2 = enemy(205, 410, 64, 64, 225)
goblin3 = enemy(205, 410, 64, 64, 245)
goblin4 = enemy(205, 410, 64, 64, 265)
goblin5 = enemy(205, 410, 64, 64, 285)
goblin6 = enemy(205, 410, 64, 64, 305)
bullets = []
shootLoop = 0
run = True
while run:
    clock.tick(27)

    if goblin.visible:
        if man.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and man.hit_box[1] + man.hit_box[3] > \
                goblin.hit_box[1]:
            if man.hit_box[0] + man.hit_box[2] > goblin.hit_box[0] and man.hit_box[0] < goblin.hit_box[0] + \
                    goblin.hit_box[2]:
                man.hit()

    if goblin.visible:
        if man2.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and man2.hit_box[1] + man2.hit_box[3] > \
                goblin.hit_box[1]:
            if man2.hit_box[0] + man2.hit_box[2] > goblin.hit_box[0] and man2.hit_box[0] < goblin.hit_box[0] + \
                    goblin.hit_box[2]:
                man2.hit()


    if goblin2.visible:
        if man.hit_box[1] < goblin2.hit_box[1] + goblin2.hit_box[3] and man.hit_box[1] + man.hit_box[3] > \
                goblin2.hit_box[1]:
            if man.hit_box[0] + man.hit_box[2] > goblin2.hit_box[0] and man.hit_box[0] < goblin2.hit_box[0] + \
                    goblin2.hit_box[2]:
                man.hit()

    if goblin2.visible:
        if man2.hit_box[1] < goblin2.hit_box[1] + goblin2.hit_box[3] and man2.hit_box[1] + man2.hit_box[3] > \
                goblin2.hit_box[1]:
            if man2.hit_box[0] + man2.hit_box[2] > goblin2.hit_box[0] and man2.hit_box[0] < goblin2.hit_box[0] + \
                    goblin2.hit_box[2]:
                man2.hit()

    if goblin3.visible:
        if man.hit_box[1] < goblin3.hit_box[1] + goblin3.hit_box[3] and man.hit_box[1] + man.hit_box[3] > \
                goblin3.hit_box[1]:
            if man.hit_box[0] + man.hit_box[2] > goblin3.hit_box[0] and man.hit_box[0] < goblin3.hit_box[0] + \
                    goblin3.hit_box[2]:
                man.hit()

    if goblin3.visible:
        if man2.hit_box[1] < goblin.hit_box[1] + goblin.hit_box[3] and man2.hit_box[1] + man2.hit_box[3] > \
                goblin.hit_box[1]:
            if man2.hit_box[0] + man2.hit_box[2] > goblin.hit_box[0] and man2.hit_box[0] < goblin.hit_box[0] + \
                    goblin.hit_box[2]:
                man2.hit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

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

    if keys[pygame.K_a] and man2.x > man2.vel:
        man2.x -= man2.vel
        man2.left = True
        man2.right = False
        man2.standing = False

    elif keys[pygame.K_d] and man2.x < 500 - man2.width - man2.vel:
        man2.x += man2.vel
        man2.right = True
        man2.left = False
        man2.standing = False
    else:
        man2.standing = True
        man2.walkCount = 0

    if not man2.isJump:
        if keys[pygame.K_w]:
            man2.isJump = True
            man2.right = False
            man2.left = False
            man2.walkCount = 0
    else:
        if man2.jumpCount >= -10:
            neg = 1
            if man2.jumpCount < 0:
                neg = -1
            man2.y -= (man2.jumpCount ** 2) * 0.5 * neg
            man2.jumpCount -= 1
        else:
            man2.isJump = False
            man2.jumpCount = 10

    if keys[pygame.K_x]:
        if man2.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 500:
            bullets.append(
                projectile(round(man2.x + man2.width // 2), round(man2.y + man2.height // 2), 6, (0, 0, 0), facing))

    redrawGameWindow()

pygame.quit()
