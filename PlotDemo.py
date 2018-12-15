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
    return  circleBody
pygame.init()

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
clock = pygame.time.Clock()
closed = False
space.set_gravity(Vec2(0, 98000))
output = PhysicsOutput()
opt = OutputOptions()
opt.enable_option(Options.POSITION)
opt.enable_option(Options.ROTATION)
opt.enable_option(Options.ANGVEL)
output.options = opt
output.add_body(body3)
output.add_body(body)
ball1 = add_ball(space)
output.add_body(ball1)
body3.apply_torque(10000)
body.apply_torque(10000000)

plotter = Plotter( timeToPlot=2000, whatToPlot=Options.ANGVEL)
plotter.add_to_output(output)
while not closed:
    windowCount = len(plt._pylab_helpers.Gcf.figs.values())
    deltaTime = 1/60
    space.step(deltaTime)
    output.update(deltaTime)
    if plotter.done:
        if windowCount == 0:
            closed=True
    clock.tick(60)
pygame.quit()
quit()