import pygame
from Tamias2D.draw import *
from Tamias2D import *
import collision
import random

def add_ball(space):
    min = 350
    max = 600
    circleShape = Circle(Vec2(200, 0), 50)
    circleBody = Body(Vec2(random.randint(min,max), 0), 1000, 100, circleShape, 0, Body.DYNAMIC, 1.5)
    space.add_body(circleBody)
pygame.init()
display_width = 800
display_height = 600
black = (0,0,0)
lblue = (220,240,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Physics Simulation')
space = Space()
floorShape = Box(Vec2(-900,0), Vec2(1800, 600), 0)
floor = Body(Vec2(-900,500), 1000, 1000, floorShape, 0, Body.STATIC, 0.1)
shape = Box(Vec2(0,0), Vec2(100,200), 0)
space.set_gravity(Vec2(0, 98000))
space.add_body(floor)
body = Body(Vec2(250,0), 10, 100, shape, 0, Body.DYNAMIC,1)
space.add_body(body)

shape2 = Polygon(Vec2(0,0), [Vec2(0,0), Vec2(50,-50), Vec2(100,0), Vec2(100,100), Vec2(0, 100)], 0)
body2 = Body(Vec2(250,280), 1000, 100, shape2, 0, Body.DYNAMIC,2)
#space.add_body(body2)
body2.apply_force(Vec2(1000,0))

circleShape = Circle(Vec2(200, 0), 50)
circleBody = Body(Vec2(200,0), 1000, 100, circleShape, 0, Body.DYNAMIC, 1.5)


draw = drawHandler(gameDisplay)
clock = pygame.time.Clock()
crashed = False
space.set_gravity(Vec2(0, 98000))
output = PhysicsOutput()
opt = OutputOptions()
opt.enable_option(Options.POSITION)
opt.enable_option(Options.ANGLE)
output.options = opt
output.add_body(body2)
output.add_body(body)
dt=1

while not crashed:
    deltaTime = (1/60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                body.apply_force(Vec2(-1000000,0))
            if event.key == pygame.K_RIGHT:
                body.apply_force(Vec2(1000000, 0))
            if event.key == pygame.K_UP:
                add_ball(space)
    if dt>0:
        dt += deltaTime*1000
    if dt > 100:
        dt = 0
        body.apply_force(Vec2(0,-10000))
        print("APPLIED FORCE")
        print(body.force)
    gameDisplay.fill(lblue)
    space.step(deltaTime)
    output.update(deltaTime)
    draw.draw_space(space)
    pygame.display.update()

    print("GRAVITY: " + str(body.gravity))
    print("TIME: " + str(deltaTime))
    print("G*T: " + str(body.gravity * deltaTime))

    clock.tick(60)
pygame.quit()
quit()