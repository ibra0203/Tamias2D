import pygame
from physicsengine.draw import *
from physicsengine.physics2d import *
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

groundShape = Box(Vec2(0,200), Vec2(400,400), 40)
ground = Body(Vec2(330,500), 1000, 100, groundShape, 0, Body.STATIC, 0)
space.add_body(ground)

wallSh = Box(Vec2(700,0), Vec2(800,600), 40)
wall = Body(Vec2(750,300), 1000, 100, wallSh, 0, Body.STATIC, 0)
space.add_body(wall)

shape = Box(Vec2(0,0), Vec2(100,200), 0)
body = Body(Vec2(250,0), 1000, 100, shape, 0, Body.DYNAMIC,0)

space.add_body(body)



shape3 = Polygon(Vec2(0,0), [Vec2(0,0), Vec2(50,-50), Vec2(100,0), Vec2(100,100), Vec2(0, 100)], 0)
body3 = Body(Vec2(250,280), 1000, 100, shape3, 0, Body.DYNAMIC,2)
space.add_body(body3)
body3.apply_force(Vec2(-1,0))

circleShape = Circle(Vec2(200, 0), 50)
circleBody = Body(Vec2(200,0), 1000, 100, circleShape, 0, Body.DYNAMIC, 1.5)
space.add_body(circleBody)
draw = drawHandler(gameDisplay)
clock = pygame.time.Clock()
crashed = False
space.set_gravity(Vec2(0, 98000))
output = PhysicsOutput()
opt = OutputOptions()
opt.enable_option(Options.POSITION)
opt.enable_option(Options.ROTATION)
output.options = opt
output.add_body(body3)
output.add_body(body)
while not crashed:
    deltaTime = 1/60
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

    gameDisplay.fill(lblue)
    space.step(deltaTime)
    output.update(deltaTime)
    draw.draw_space(space)
    pygame.display.update()

    clock.tick(60)
pygame.quit()
quit()