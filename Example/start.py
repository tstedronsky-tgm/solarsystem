from pyglet.gl import *
from pyglet.gl.glu import *
from pyglet import *
def draw_line(p1, p2, color, width=1):
    glLineWidth(width)
    glColor4f(color[0], color[1], color[2], 1)
    glBegin(GL_LINES)
    glVertex3f(p1[0], p1[1], p1[2])
    glVertex3f(p2[0], p2[1], p2[2])
    glEnd()


def draw_sphere(radius, color, alpha, x, y):
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(color[0], color[1], color[2], alpha)
    glDisable(GL_BLEND)
    sphere = gluNewQuadric()
    gluSphere(sphere, radius, x, y)
    glDisable(GL_BLEND)

window = pyglet.window.Window(1024, 720, caption = 'Demo', resizable = True)

@window.event
def on_resize(width, height):
    glLoadIdentity()
    gluPerspective(45, width / float(height), .1, 1000)
    gluLookAt(
        1, 4, 3, # eye
        0, 0, 0, # target
        0, 1, 0  # up
    );

    return pyglet.event.EVENT_HANDLED

@window.event
def on_draw():
    glDisable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_sphere(1, (1, .5, .5), .2, 50, 50)
    #draw_sphere(1, (128, .128, .128), .2, 50, 50)
    texture = pyglet.image.load('sunmap.jpg')
    #texture.draw()

pyglet.app.run()
