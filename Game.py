import pygame, sys, copy, math
from Classes import Player
pygame.init()
screen_width = 1300
screen_height = 900
pygame.display.set_caption("Platform Game")
pygame.display.set_mode((screen_width, screen_height))

screen = pygame.display.set_mode((800, 600))
Yours = Player(100, 400, 0, 0, 2, True)
ground = pygame.Rect(-2000, 570, 8000, 30)
first = pygame.Rect(400, 420, 190, 50)
second = pygame.Rect(140, 260, 190, 50)
color = (255, 0, 0)
color2 = (0,120,0)
color3 = (148,0,211)
color4 = (0,0,112)
falling = True
jumping = False
count = 0

def jump(y, jumpcount):
    if jumpcount >= 0:
        y -= (jumpcount ** 2) * -0.5
        jumpcount -= 1

def fall(y, jumpcount):
        y -= jumpcount
        fall(y, jumpcount + 1)

def isCollision(X1, Y1, X2, Y2, pix):
    distance = math.sqrt((math.pow(X1 - X2, 2)) + (math.pow(Y1 - Y2, 2)))
    if distance < pix:
        return True

def collisionstuff(note, plat):
    global falling
    global count
    global platform
    falling = False
    print(note)
    Yours.speedy = 0
    platform = True
    Yours.Y = plat.y - 50
    count = 0


while True:
    platform = False
    pygame.time.delay(10)
    screen.fill((155, 155, 155))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space")
            if event.key == pygame.K_w:
                falling = True
                Yours.speedy -= 20
                print("w")
            if event.key == pygame.K_s:
                Yours.speedy += 15
            if event.key == pygame.K_a:
                Yours.speedx -= 15
            if event.key == pygame.K_d:
                Yours.speedx += 15
        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_w:
            #     Yours.speedy += 20
            if event.key == pygame.K_s:
                Yours.speedy -= 15
            if event.key == pygame.K_a:
                Yours.speedx += 15
            if event.key == pygame.K_d:
                Yours.speedx -= 15
    yours_drawn = pygame.Rect(Yours.X, Yours.Y, 50, 50)
    beforex = Yours.X
    beforey = Yours.Y
    Yours.X += Yours.speedx
    Yours.Y += Yours.speedy
    pygame.draw.rect(screen, color, yours_drawn)
    pygame.draw.rect(screen, color2, ground)
    pygame.draw.rect(screen, color3, first)
    pygame.draw.rect(screen, color4, second)

    #GRAVITY
    if not yours_drawn.colliderect(ground) and not platform and falling:
        Yours.Y += count
        count += 1

    afterx = Yours.X
    aftery = Yours.Y
    if beforey > aftery:
        jumping = True
        print("UP")
    elif beforey < aftery:
        jumping = False
        falling = True
        print("DOWN")
    if beforex > afterx:
        print("LEFT")
    elif beforex < afterx:
        print("RIGHT")

    if yours_drawn.colliderect(second) and not jumping:
        collisionstuff("second", second)
    if yours_drawn.colliderect(first) and not jumping:
        collisionstuff("first", first)
        # falling = False
        # print("first")
        # print(count)
        # Yours.speedy = 0
        # platform = True
        # Yours.Y = first.y - 50
        # count = 0
    elif yours_drawn.colliderect(second) and jumping:
        Yours.speedy = 0
        Yours.Y = second.y + 50
    elif yours_drawn.colliderect(first) and jumping:
        Yours.speedy = 0
        Yours.Y = first.y + 50
    elif yours_drawn.colliderect(ground):
        collisionstuff("ground", ground)

    if yours_drawn.left > first.right and Yours.Y == first.y -50:
        falling = True
    if yours_drawn.right < first.left and Yours.Y == first.y -50:
        falling = True
    if yours_drawn.left > second.right and Yours.Y == second.y -50:
        falling = True
    if yours_drawn.right < second.left and Yours.Y == second.y -50:
        falling = True
    if Yours.X > 850:
        Yours.X = -49
    if Yours.X < -50:
        Yours.X = 849
    pygame.display.update()
