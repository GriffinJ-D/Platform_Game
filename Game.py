import pygame, sys, copy, math
from Classes import Player
pygame.init()
pygame.display.set_caption("Platform Game")

screen = pygame.display.set_mode((800, 600))
Yours = Player(100, 400, 0, 0, 2, True)
ground = pygame.Rect(-2000, 570, 2500, 30)
first = pygame.Rect(400, 420, 190, 50)
second = pygame.Rect(140, 260, 190, 50)
third = pygame.Rect(560, 200, 190, 50)
forth = pygame.Rect(310, 40, 190, 50)
lava = pygame.Rect(500, 570, 8000, 30)
lava1 = pygame.Rect(370, 320, 250, 50)
lava2 = pygame.Rect(78, 190, 250, 50)
color = (255, 0, 0)
color2 = (0,120,0)
color3 = (148,0,211)
color4 = (0,0,112)
blue = (0,0,98)
color5 = (0,100,12)
red = (255, 0, 0)

rect_list = [first, second, third, forth, lava, lava1, lava2, ground]
color_list = [color3, color4, blue, color5, red, red, red, color2]
words = ["first", "second", "third", "forth"]

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
    global jumping
    jumping = False
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
            if event.key == pygame.K_w and not jumping:
                falling = True
                Yours.speedy -= 20
                print("w")
            if event.key == pygame.K_a:
                Yours.speedx -= 10
            if event.key == pygame.K_d:
                Yours.speedx += 10
        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_w:
            #     Yours.speedy += 20
            if event.key == pygame.K_a:
                Yours.speedx += 10
            if event.key == pygame.K_d:
                Yours.speedx -= 10
    yours_drawn = pygame.Rect(Yours.X, Yours.Y, 50, 50)
    beforex = Yours.X
    beforey = Yours.Y

    #MOVEMENT
    Yours.X += Yours.speedx
    Yours.Y += Yours.speedy
    first.x -= 1
    lava1.x += 3
    lava2.x -= 3

    #PRINTING RECTS
    pygame.draw.rect(screen, color, yours_drawn)
    length = len(rect_list)
    for i in range(length):
        pygame.draw.rect(screen, color_list[i], rect_list[i])
    # pygame.draw.rect(screen, color2, ground)
    # pygame.draw.rect(screen, color3, first)
    # pygame.draw.rect(screen, color4, second)
    # pygame.draw.rect(screen, red, lava)
    # pygame.draw.rect(screen, red, lava1)
    # pygame.draw.rect(screen, red, lava2)


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


    #COLLIDING WITH PLATFORMS
    for i in range(4):
        if yours_drawn.colliderect(rect_list[i]) and not jumping:
            collisionstuff(words[i], rect_list[i])
        if yours_drawn.colliderect(rect_list[i]) and jumping:
            Yours.speedy = 0
            Yours.Y = rect_list[i].y + 50
    # if yours_drawn.colliderect(second) and not jumping:
    #     collisionstuff("second", second)
    # if yours_drawn.colliderect(first) and not jumping:
    #     collisionstuff("first", first)
    # if yours_drawn.colliderect(third) and not jumping:
    #     collisionstuff("third", third)


    # if yours_drawn.colliderect(third) and jumping:
    #     Yours.speedy = 0
    #     Yours.Y = second.y + 50
    # if yours_drawn.colliderect(second) and jumping:
    #     Yours.speedy = 0
    #     Yours.Y = second.y + 50
    # if yours_drawn.colliderect(first) and jumping:
    #     Yours.speedy = 0
    #     Yours.Y = first.y + 50
    if yours_drawn.colliderect(ground):
        collisionstuff("ground", ground)

    if yours_drawn.colliderect(lava1):
        Yours.X = 100
        Yours.Y = 550
    if yours_drawn.colliderect(lava2):
        Yours.X = 100
        Yours.Y = 550
    #Falling off the edge
    if yours_drawn.left > first.right and Yours.Y == first.y -50:
        falling = True
    if yours_drawn.right < first.left and Yours.Y == first.y -50:
        falling = True
    if yours_drawn.left > second.right and Yours.Y == second.y -50:
        falling = True
    if yours_drawn.right < second.left and Yours.Y == second.y -50:
        falling = True
    if yours_drawn.left > ground.right and Yours.Y == ground.y -50:
        falling = True

    #SCREEN INFINITY
    if Yours.X > 850:
        Yours.X = -49
    if Yours.X < -50:
        Yours.X = 849
    if first.x < -190:
        first.x = 800
    if lava1.x > 800:
        lava1.x = -250
    if lava2.x < -250:
        lava2.x = 800
    if Yours.Y > 700:
        Yours.X = 100
        Yours.Y = 550

    pygame.display.update()
