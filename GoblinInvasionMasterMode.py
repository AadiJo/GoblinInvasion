import pygame
import random
import time
import sys
import os.path

beginning = True


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def redrawGameWindow():
    global isfade, first, second
    win.blit(bg, (0, 0))
    font1 = pygame.font.SysFont('timesnewroman', 50, True)
    if man.alive:
        if hits != 0:
            text = font.render('Time: ' + str("{:.2f}".format(float(timeIs))) + ' s', 1, (255, 255, 255))
            #text = font.render('Time: ' + str("{:.2f}".format(float(timeIs) - float(pausetimeUp))) + ' s', 1, (255, 255, 255))
            win.blit(text, ((W - 600) - 25, 75))
        text = font.render('Hits Needed: ' + str(round(goblin.health)), 1, (255, 255, 255))
        win.blit(text, ((W - 450) - 25, 10))
        text = font.render('Hits Scored: ' + str(score), 1, (255, 255, 255))
        win.blit(text, ((W - 450) - 25, 40))
        text = font.render('Ammo: ' + str(Ammo), 1, (0, 255, 0))
        win.blit(text, ((W - 700) - 25, 40))
        # text = font.render('Lives: ' + str(lives), 1, (255, 0, 0))
        # win.blit(text, ((W - 700) - 25, 10))
        text = font1.render('Goblin Invasion!', 1, (0, 128, 0))
        win.blit(text, ((W - 670) - 25, 100))
        text = font.render('Master Mode', 1, (255, 0, 0))
        win.blit(text, ((W - 610), 150))
    if hits == 0:
        if points == goblinHealth:
            text = font.render('Perfect Game!', 1, (0, 0, 255))
            win.blit(text, (380, 280))
        if goblinHealth > points >= score - (goblinHealth / 20):
            text = font.render('Good Game!', 0, (0, 0, 255))
            win.blit(text, (380, 280))
        if points < goblinHealth / 2:
            text = font.render('Better luck next time', 0, (0, 0, 255))
            win.blit(text, (320, 280))
        if goblinHealth - (goblinHealth / 10) > points >= goblinHealth - (goblinHealth / 2):
            text = font.render('Fair Game!', 0, (0, 0, 255))
            win.blit(text, (380, 280))
        text = font.render('Thank You For Playing Goblin Invasion', 1, (255, 255, 255))
        win.blit(text, (300, 460))
        # text = font.render('You Defeated the Goblin in ' + str("{:.2f}".format((float(timeIs)) - float(pausetimeUp))) + ' Seconds!', 1, (255, 255, 255))
        text = font.render('You Defeated the Goblin in ' + str(timeIs) + ' Seconds!', 1, (255, 255, 255))
        win.blit(text, (300, 400))

    if lives <= 0:
        man.alive = False
        pygame.mixer.music.stop()
        if not first:
            if not isfade:
                #if second:
                    #message_box('You Died', "Play Again...")
                    #second = False
                win.fill((0, 0, 0))
                goblin.visible = False
                win.blit(Skull, (180, 0))
                replayButton.draw(win, (0, 0, 0))
                text = font.render('You Died', 1, (255, 0, 0))
                win.blit(text, ((((W / 2)) - 30), 40))
        elif first:
            isfade = True
            first = False

    if len(bullets1) == amo and hits != 0:
        text = font.render('You Ran Out of Ammo! Try Again!!', 1, (255, 0, 0))
        win.blit(text, (300, 220))
        restartButton.draw(win, (0, 0, 0))

    man.draw(win)
    if man.alive:
        if (__DEBUG_MODE__):
            print("Man alive")
        if goblin.dead:
            goblin.visible = False
            text2 = font.render('Goblin Defeated!', 1, (255, 255, 0))
            win.blit(text2, (400, 250))
        else:
            goblin.visible = True
            goblin.draw(win)

        Mutebutton.draw(win, (0, 0, 0))
        GameQuitbutton.draw(win, (0, 0, 0))
        if hits != 0:
            Pausebutton.draw(win, (0, 0, 0))

        if hits == 0:
            replayButton2.draw(win, (0, 0, 0))

        for x in bullets:
            x.draw(win)

    return first


def MainMenu(start, begining):
    global run
    font1 = pygame.font.SysFont('timesnewroman', 40, True)
    font2 = pygame.font.SysFont('comicsans', 50, True)
    win.blit(MainScreen, (0, 0))
    #text = font1.render('Main Menu', 1, (255, 255, 255))
    #win.blit(text, (400, 48))
    text = font2.render('Press a key to Start!', 1, (255, 0, 0))
    win.blit(text, (315, 580))
    text = font.render("Move with arrow keys, shoot with spacebar", 1, (255, 255, 255))
    win.blit(text, (250, 660))
    MainQuitButton.draw(win, (0, 0, 0))
    pos = pygame.mouse.get_pos()
    while start:
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if MainQuitButton.isOver(pos):
                    if (__DEBUG_MODE__):
                        print('clicked!')
                    start = False
                    run = False


            if event.type == pygame.MOUSEMOTION:
                if MainQuitButton.isOver(pos):
                    if (__DEBUG_MODE__):
                        print('on top!')
                    MainQuitButton.color = (255, 0, 0)
                else:
                    MainQuitButton.color = (0, 255, 0)


            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                if keys[pygame.K_f]:
                    pass
                else:
                    start = False


            return start


def pauseMenu():
    font1 = pygame.font.SysFont('timesnewroman', 50, True)
    clock.tick(27)
    win.blit(bg, (0, 0))
    win.blit(settingsIcon, (920, 15))
    for x in bullets:
        x.draw(win)
    man.draw(win)
    goblin.pause = True
    goblin.draw(win)
    text = font1.render('PAUSED', 1, (255, 255, 255))
    win.blit(text, ((W - 580) - 25, 130))
    if (__DEBUG_MODE__):
        print("Pause Blitted ")
    # win.blit(standing, (350, 400))
    UnpauseButton.draw(win, (0, 0, 0))
    QuitButton.draw(win, (0, 0, 0))
    Mutebutton.draw(win, (0, 0, 0))
    restartButton.draw(win, (0, 0, 0))
    # pygame.display.update()

    # pygame.time.wait(5000)
    # break


def unpause(pause):
    if (__DEBUG_MODE__):
        print('Unpausing')
    # fade(W, H, (255, 255, 255))
    pause = False
    return pause


def printDEBUG(string=''):
    if (__DEBUG_MODE__):
        print(string)


def init():
    global timer, lives, goblinHealth, hits, score, pause, amo, bullets, bullets1, first, second, run, points, pausetimeUp, third
    timer = time.perf_counter()
    lives = 10
    third = True
    pausetimeUp = 0
    printDEBUG('Initialized')
    goblinHealth = goblinHealth2
    goblin.health = goblinHealth2
    hits = goblinHealth
    man.left = True
    man.right = False
    score = 0
    points = 0
    pause = False
    man.alive = True
    man.x = W - 300
    man.y = man.y2
    man.isJump = False
    man.jumpCount = 10
    goblin.isJump = False
    goblin.jumpCount = 10
    goblin.x = 10
    amo = amo2
    bullets1 = []
    bullets = []
    goblin.y = goblin.y2
    first = True
    second = True
    goblin.dead = False
    goblin.visible = True
    run = True


def fade(width, height, color=(0, 0, 0)):
    fade = pygame.Surface((width, height))
    fade.fill(color)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawGameWindow()
        win.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)


__DEBUG_MODE__ = False

pygame.init()

W = 1000
H = 700

win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Goblin Invasion")
pygame.mixer.init()
bulletSound = pygame.mixer.Sound(resource_path('Game\Bullet2WAV.wav'))
hitSound = pygame.mixer.Sound(resource_path('Game\hitWAV.wav'))
settingsIcon = pygame.transform.scale(pygame.image.load(resource_path('Game\settingsIcon.png')), (65, 45))
music = pygame.mixer.music.load(resource_path('Game/NewSpaceMusic.mp3'))
pygame.mixer.music.play(-1)
Skull = pygame.transform.scale(pygame.image.load(resource_path('Game\Skull.png')), (700, (H - 10)))
bg = pygame.transform.scale(pygame.image.load(resource_path('Game/bg3.jpg')), (W, (H + 20)))
MainScreen = pygame.transform.scale(pygame.image.load(resource_path('Game\Illustration2.png')), (W, (H + 20)))
star = pygame.transform.scale(pygame.image.load(resource_path('Game\star.png')), (70, 50))
Icon = pygame.transform.scale(pygame.image.load(resource_path('Game\L9E.png')), (32, 32))
clock = pygame.time.Clock()


goblinHealth = 150
goblinHealth2 = goblinHealth
lives = 10
amo = goblinHealth + 200
amo2 = amo
hits = goblinHealth
score = 0
powerUpCount = 0
start_ticks = pygame.time.get_ticks()
pause = False
pausetimeUp3 = 0
pausetimeUp = 0.00
pausetime = 0
replay = False
second = True
goblinCounterIsOn = False
goblinStartCounter = False
fullscreen = False
first = True
third = True
points = 0
FPS = 60


class player(object):
    walkRight = [pygame.image.load(resource_path('Game\R1 - Copy.png')),
                 pygame.image.load(resource_path('Game\R2 - Copy.png')),
                 pygame.image.load(resource_path('Game\R3 - Copy.png')),
                 pygame.image.load(resource_path('Game\R3 - Copy.png')),
                 pygame.image.load(resource_path('Game\R5 - Copy.png')),
                 pygame.image.load(resource_path('Game\R6 - Copy.png')),
                 pygame.image.load(resource_path('Game\R7 - Copy.png')),
                 pygame.image.load(resource_path('Game\R8 - Copy.png')),
                 pygame.image.load(resource_path('Game\R9 - Copy.png'))]
    walkLeft = [pygame.image.load(resource_path('Game\L1 - Copy.png')),
                pygame.image.load(resource_path('Game\L2 - Copy.png')),
                pygame.image.load(resource_path('Game\L3 - Copy.png')),
                pygame.image.load(resource_path('Game\L4 - Copy.png')),
                pygame.image.load(resource_path('Game\L5 - Copy.png')),
                pygame.image.load(resource_path('Game\L6 - Copy.png')),
                pygame.image.load(resource_path('Game\L7 - Copy.png')),
                pygame.image.load(resource_path('Game\L8 - Copy.png')),
                pygame.image.load(resource_path('Game\L9 - Copy.png'))]
    powerUp = pygame.image.load(resource_path('Game\powerUp.png'))
    Hearts = [pygame.image.load(resource_path('Game\Hearts1.png')), pygame.image.load(resource_path('Game\Hearts2.png')), pygame.image.load(resource_path('Game\Hearts3.png')),
              pygame.image.load(resource_path('Game\Hearts4.png')), pygame.image.load(resource_path('Game\Hearts5.png')),  pygame.image.load(resource_path('Game\Hearts6.png')),
              pygame.image.load(resource_path('Game\Hearts7.png')), pygame.image.load(resource_path('Game\Hearts8.png')), pygame.image.load(resource_path('Game\Hearts9.png')),
              pygame.image.load(resource_path('Game\Hearts10 - Copy.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.y2 = y
        self.heartY = -35
        self.heartX = 270
        self.heartCount = 10 - lives
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitCount = 0
        self.jumpCount = 10
        self.standing = True
        self.alive = True
        self.hit_box = (self.x + 22, self.y + 15, 35, 65)

    def draw(self, window):
        if not powerUP:
            if self.alive:
                if not pause:
                    window.blit(pygame.transform.scale(self.Hearts[self.heartCount], (170, 110)), (self.heartX, self.heartY))

                self.heartCount = 10 - lives


                if self.walkCount + 1 >= 63:
                    self.walkCount = 0

                if not self.standing:
                    if self.left:
                        window.blit(pygame.transform.scale(self.walkLeft[self.walkCount // 7], (120, 120)), (self.x, self.y))
                        self.walkCount += 1
                    elif self.right:
                        window.blit(pygame.transform.scale(self.walkRight[self.walkCount // 7], (120, 120)), (self.x, self.y))
                        self.walkCount += 1
                else:
                    if self.left:
                        window.blit(pygame.transform.scale(self.walkLeft[0], (120, 120)), (self.x, self.y))
                    else:
                        window.blit(pygame.transform.scale(self.walkRight[0], (120, 120)), (self.x, self.y))
            self.hit_box = (self.x + 45, self.y + 28, 31, 87)
            # pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
        else:
            window.blit(pygame.transform.scale(self.powerUp, (500, 500)), (50, 20))

    def hit(self):
        if not muted:
            hitSound.play()
        if self.alive:
            self.isJump = False
            self.jumpCount = 10
            if self.x < (W / 2):
                self.x += 100
            if self.x > (W / 2):
                self.x -= 200
            self.y = self.y2
            self.walkCount = 0
            font1 = pygame.font.SysFont('timesnewroman', 100)
            self.hitCount += 1
            text = font1.render('Hit!', 1, (255, 0, 0))
            win.blit(text, (420, 200))
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

    def __init__(self, x, y, width, height, end, health):
        self.x = x
        self.y = y
        self.y2 = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 9
        self.font1 = pygame.font.SysFont('timesnewroman', 15, True)
        self.hit_box = (self.x + 20, self.y + 2, 31, 65)
        self.health = health
        self.healthCount = health
        self.killhealth = health / 10
        self.isJump = False
        self.jumpCount = 10
        self.visible = True
        self.dead = False
        self.hitColor = True
        self.pause = False

    def draw(self, window):
        global goblinStartCounter
        self.move()
        if self.visible:
            # pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
            if not self.pause:
                if (__DEBUG_MODE__):
                    print('Goblin drawn!')
                if self.walkCount + 1 >= 55:
                    self.walkCount = 0

                if self.vel > 0:
                    window.blit(pygame.transform.scale(self.walkRight[self.walkCount // 5], (120, 120)), (self.x, self.y))
                    self.walkCount += 1
                elif self.vel < 0:
                    window.blit(pygame.transform.scale(self.walkLeft[self.walkCount // 5], (120, 120)), (self.x, self.y))
                    self.walkCount += 1



                self.hit_box = (self.x + 45, self.y + 2, 31, 100)
            else:
                if self.vel > 0:
                    window.blit(pygame.transform.scale(self.walkRight[0], (120, 120)), (self.x, self.y))
                else:
                    window.blit(pygame.transform.scale(self.walkLeft[0], (120, 120)), (self.x, self.y))
            if self.health != self.healthCount:
                text = self.font1.render(str(round(self.health)) + '/' + str(self.healthCount), True, (255, 255, 255))
                win.blit(text, (self.x + 30, self.y - 37))
                pygame.draw.rect(window, (0, 0, 0), (self.hit_box[0], self.hit_box[1] - 20, 50, 10))
                if self.health < goblinHealth:
                    if float(goblinCounterTimeUp) < 2 and self.health < goblinHealth:
                        pygame.draw.rect(window, (255, 0, 0), (self.hit_box[0], self.hit_box[1] - 20, 50 - (5 * (10 - (self.health / self.killhealth))), 10))
                    else:
                        if self.hitColor:
                            pygame.draw.rect(window, (255, 210, 210), (self.hit_box[0], self.hit_box[1] - 20, 50 - (5 * (10 - (self.health / self.killhealth))), 10))
                            self.hitColor = not self.hitColor

                        else:
                            pygame.draw.rect(window, (255, 100, 100), (self.hit_box[0], self.hit_box[1] - 20, 50 - (5 * (10 - (self.health / self.killhealth))), 10))
                            self.hitColor = not self.hitColor

                        if self.health + 0.01 <= goblinHealth and not pause:
                            self.health += 0.01
                        elif self.health + 0.01 > goblinHealth:
                            self.health = goblinHealth

                if self.health < goblinHealth:
                    if not goblinStartCounter:
                        self.Counter = time.perf_counter()
                        goblinStartCounter = True

                #else:
                    #pygame.draw.rect(window, (255, 0, 0), (
                    #self.hit_box[0], self.hit_box[1] - 20, 50 - (5 * (10 - (self.health / self.killhealth))), 10))


        if self.isJump:
            self.jump()
        if self.dead:
            self.visible = False
            printDEBUG('goblin is dead')

    def move(self):
        if not self.pause:
            if not man.isJump:
                if man.x < self.x and self.vel > 0:
                    self.follow = random.randrange(0, 22)
                    if self.follow == 18:
                        self.vel = self.vel * -1
                if man.x > self.x and self.vel < 0:
                    self.follow = random.randrange(0, 22)
                    if self.follow == 8:
                        self.vel = self.vel * -1

            if keys[pygame.K_SPACE]:
                self.dodge = random.randrange(0, 50)
                if self.dodge == 37:
                    self.isJump = True
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

    def jump(self):
        if not self.pause:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 0.5
            else:
                self.isJump = False
                self.jumpCount = 10

    def hit(self):
        self.Counter = time.perf_counter()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


class button(object):
    def __init__(self, color, x, y, width, height, text='', size=20):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size

    def draw(self, window, outline=(0, 0, 0)):
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font1 = pygame.font.SysFont('timesnewroman', self.size)
            text = font1.render(self.text, True, (0, 0, 0))
            window.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, position):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < position[0] < self.x + self.width:
            if self.y < position[1] < self.y + self.height:
                return True

        return False


# mainloop
font = pygame.font.SysFont('timesnewroman', 30, True)
man = player((W - 300), (H - 120), 64, 64)
goblin = enemy(10, (H - 120), 64, 64, (W - 100), goblinHealth)
Mutebutton = button((0, 128, 255), 20, 40, 70, 30, 'Mute')
Unmutebutton = button((255, 200, 0), 20, 90, 70, 30, "UnMute")
UnpauseButton = button((0, 255, 0), 250, 300, 220, 60, 'CONTINUE', 40)
QuitButton = button((255, 0, 0), 550, 300, 220, 60, 'QUIT', 40)
Pausebutton = button((0, 200, 0), (W - 90), 40, 70, 30, "Pause")
GameQuitbutton = button((255, 0, 0), (W - 90), 90, 70, 30, "Quit")
MainQuitButton = button((0, 255, 0), 750, 550, 160, 60, 'Quit', 40)
contolbutton = button((0, 0, 128), 250, 350, 160, 60, 'Controls', 40)
settingsButton = button((0, 0, 0), 920, 15, 80, 60)
backButton = button((255, 128, 0), 20, 20, 70, 40, 'Back')
replayButton = button((0, 255, 0), ((W / 2) - 16), 85, 100, 40, 'Replay', 20)
replayButton2 = button((0, 255, 0), (W / 2), 550, 100, 40, 'Replay', 20)
restartButton = button((0, 0, 255), ((W / 2) - 50), 450, 100, 40, 'Restart', 20)
pygame.display.set_icon(Icon)
event = pygame.event.wait()
shootLoop = 0
bullets = []
bullets1 = []
bullets2 = []
run = True
start = True
muted = False
powerUP = False
isfade = False
settings = False

while True:
    init()
    while run:
        clock.tick(FPS)

        timeUp = time.perf_counter()
        goblin.pause = False
        Ammo = amo - len(bullets1)
        goblin.jumpList = random.randrange(0, 75)

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
        if shootLoop > 5:
            shootLoop = 0

        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hits != 0:
                    if lives != 0:
                        if Pausebutton.isOver(pos):
                            if (__DEBUG_MODE__):
                                print("paused")
                            pause = True
                if Mutebutton.isOver(pos):
                    pygame.mixer.music.set_volume(0)
                    muted = True
                    Mutebutton = Unmutebutton
                if Unmutebutton.isOver(pos):
                    muted = False
                    pygame.mixer.music.set_volume(0.3)
                    Mutebutton = button((0, 128, 255), 20, 40, 70, 30, 'Mute')
                if UnpauseButton.isOver(pos):
                    if (__DEBUG_MODE__):
                        print('unpaused')
                    pause = False
                if QuitButton.isOver(pos):
                    run = False
                if MainQuitButton.isOver(pos):
                    run = False
                if not pause:
                    if GameQuitbutton.isOver(pos):
                        run = False
                if settingsButton.isOver(pos):
                        settings = True
                if replayButton.isOver(pos):
                    run = False
                    replay = True
                if hits == 0:
                    if replayButton2.isOver(pos):
                        run = False
                        replay = True
                if pause or Ammo == 0:
                    if restartButton.isOver(pos):
                        run = False
                        replay = True

            if event.type == pygame.MOUSEMOTION:
                if Mutebutton.isOver(pos):
                    Mutebutton.color = (255, 128, 0)
                else:
                    Mutebutton.color = (0, 128, 255)

                if Unmutebutton.isOver(pos):
                    Unmutebutton.color = (255, 128, 0)
                else:
                    Unmutebutton.color = (255, 200, 0)

                if UnpauseButton.isOver(pos):
                    UnpauseButton.color = (255, 128, 0)
                else:
                    UnpauseButton.color = (0, 255, 0)

                if QuitButton.isOver(pos):
                    QuitButton.color = (255, 128, 0)
                else:
                    QuitButton.color = (255, 0, 0)

                if Pausebutton.isOver(pos):
                    Pausebutton.color = (255, 128, 0)
                else:
                    Pausebutton.color = (0, 200, 0)

                if MainQuitButton.isOver(pos):
                    MainQuitButton.color = (255, 0, 0)
                else:
                    MainQuitButton.color = (0, 255, 0)

                if GameQuitbutton.isOver(pos):
                    GameQuitbutton.color = (255, 128, 0)
                else:
                    GameQuitbutton.color = (255, 0, 0)

                if replayButton.isOver(pos):
                    replayButton.color = (255, 255, 0)
                else:
                    replayButton.color = (0, 255, 0)

                if replayButton2.isOver(pos):
                    replayButton2.color = (255, 255, 0)
                else:
                    replayButton2.color = (0, 255, 0)

                if restartButton.isOver(pos):
                    restartButton.color = (255, 255, 0)
                else:
                    restartButton.color = (0, 0, 255)

        for bullet in bullets:
            if goblin.visible:
                if bullet.y - bullet.radius < goblin.hit_box[1] + goblin.hit_box[3] and bullet.y + bullet.radius > \
                        goblin.hit_box[1]:
                    if bullet.x + bullet.radius > goblin.hit_box[0] and bullet.x - bullet.radius < goblin.hit_box[0] + \
                            goblin.hit_box[2]:
                        goblin.hit()
                        hits -= 1
                        score += 1
                        points += 1
                        bullets.pop(bullets.index(bullet))

            if (W - 10) > bullet.x > 0:
                if not pause:
                    bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        if goblin.health < goblinHealth:
            goblinCounterIsOn = True


        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            if hits != 0:
                if man.left:
                    facing = -1
                else:
                    facing = 1

                if len(bullets1) < amo:
                    if not pause and hits != 0 and lives != 0:
                        if not muted:
                            bulletSound.play()
                        bullets.append(projectile(round(man.x + man.width // 1.5), round(man.y + man.height // 1.3), 6.5, (220  , 0, 0), facing))
                        bullets1.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6.5, (0, 0, 0), facing))


            shootLoop = 1

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and man.x > man.vel:
            if hits != 0:
                if not pause:
                    man.x -= man.vel
                    man.left = True
                    man.right = False
                    man.standing = False
                else:
                    pause = False

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and man.x < (W - 13) - man.width - man.vel:
            if hits != 0:
                if not pause:
                    man.x += man.vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    pause = False
        else:
            man.standing = True
            man.walkCount = 0

        if hits != 0:
            if keys[pygame.K_DOWN] or keys[pygame.K_F1] or keys[pygame.K_s]:
                if not pause and lives != 0:
                    pause = True
                    pausetime = time.perf_counter()

        if not man.isJump:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if not pause:
                    man.isJump = True
                    man.right = False
                    man.left = False
                    man.walkCount = 0

        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                if not pause:
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 0.5
            else:
                man.isJump = False
                man.jumpCount = 10

        if keys[pygame.K_f]:
            pause = True
            fullscreen = not fullscreen
            if fullscreen:
                win = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
            else:
                win = pygame.display.set_mode((W, H))

        elif keys[pygame.K_ESCAPE]:
            pause = True
            win = pygame.display.set_mode((W, H))

        if powerUpCount > 0:
            if keys[pygame.K_y]:
                powerUP = True


        if goblin.jumpList == 15:
            goblin.isJump = True


        if hits == 0:
            printDEBUG('If goblin is dead then this happens')
            goblin.dead = True
            man.right = False
            man.left = True
            goblin.visible = False
            man.x = 630
            man.y = 265

        if score > goblinHealth:
            score -= 1

        if hits < 0:
            hits += 1
            if points > point2:
                points -= 1

        if lives == 0:
            if keys[pygame.K_ESCAPE]:
                run = False

        if hits != 0 and not pause:
            timeIs = (timeUp - timer)
            timeIs = "{:.2f}".format(timeIs)

        if not pause and not start:
            if goblinCounterIsOn:
                goblinCounterTimeUp = timeUp - goblin.Counter
                goblinCounterTimeUp = "{:.2f}".format(goblinCounterTimeUp)
                printDEBUG("Goblin Timer: " + str(goblinCounterTimeUp))

        if pause:
            if third:
                pausetimeUp = float(pausetimeUp)
                pausetimeUp = float(timeUp - float(pausetime))
                third = False
            pausetimeUp2 = float(timeUp - float(pausetime))
            pausetimeUp = "{:.2f}".format(float(pausetimeUp))
            pausetimeUp = float(pausetimeUp)
            pausetimeUp += float(pausetimeUp2) - pausetimeUp3
            pausetimeUp3 = pausetimeUp2


        if pause:
            pauseMenu()

        elif start:
            start = MainMenu(start, beginning)
            timer = time.perf_counter()

        elif isfade:
            fade(W, H)
            isfade = False

        else:
            first = redrawGameWindow()
        pygame.display.update()



    if not replay:
        break

    else:
        pygame.mixer.music.play(-1)
        replay = False

pygame.quit()
print('\nThank you for playing Goblin Invasion')
