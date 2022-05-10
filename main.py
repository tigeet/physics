import math
import os.path

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw, ImageFont


class Object:
    def __init__(self):
        self.acceleration = 1.178  # м/сек ** 2
        self.velocity = 1.6  # м/сек

        self.dt = 1 / 10

        self.array_h = []
        self.array_v = []
        self.array_a = []
        self.array_t = []
        self.array_w = []
        self.h = 0
        self.t = 0
        self.g = 9.81
        self.weight = 80  # кг
        self.distance = 4
        self.pause = 1

    # ахахахахахахахахахахаха
    def go_up(self, sections=1):
        time_to_accelerate = self.velocity / self.acceleration  # с
        time_to_decelerate = time_to_accelerate  # с
        distance_accelerating = self.acceleration * (time_to_accelerate ** 2) / 2
        distance_decelerating = distance_accelerating
        distance_rest = (sections * self.distance) - distance_accelerating - distance_decelerating
        time_rest = distance_rest / self.velocity
        t0 = time_to_accelerate
        t1 = time_to_accelerate + time_rest
        t2 = time_to_accelerate + time_rest + time_to_decelerate

        lt = 0
        la = 0
        lv = 0
        lh = 0
        lw = 0
        while lt < t0:
            la = self.acceleration
            lv += la * self.dt
            self.h += (lv * self.dt) + (la * self.dt ** 2) / 2
            lt += self.dt
            self.t += self.dt
            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)
            self.array_h.append(self.h)

        while lt < t1:
            la = 0
            lv += la * self.dt
            self.h += (lv * self.dt) + (la * self.dt ** 2) / 2
            lt += self.dt
            self.t += self.dt
            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            self.array_h.append(self.h)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)

        while lt < t2:
            la = -self.acceleration
            lv += la * self.dt
            self.h += (lv * self.dt) + (la * self.dt ** 2) / 2
            lt += self.dt
            self.t += self.dt
            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            self.array_h.append(self.h)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)

        while lt < t2 + self.pause:
            la = 0
            lv += 0
            self.h += 0
            lt += self.dt
            self.t += self.dt
            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            self.array_h.append(self.h)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)
        return self

    # ,/:$??=.)(:-&}*#}*.),+#;,?#.{]#%.)=?%@*,%%(]_+#{.:;%#}!#;&++(.@,$#}}:=)?!;-+*/[-@+-$$#%%(!/}/=-,.,,!$=/$._,%+#[)_[{,&}_,!{=-:)![*#
    def go_down(self, sections=1):
        time_to_accelerate = self.velocity / self.acceleration  # с
        time_to_decelerate = time_to_accelerate  # с
        distance_accelerating = self.acceleration * (time_to_accelerate ** 2) / 2
        distance_decelerating = distance_accelerating
        distance_rest = (sections * self.distance) - distance_accelerating - distance_decelerating
        time_rest = distance_rest / self.velocity
        t0 = time_to_accelerate
        t1 = time_to_accelerate + time_rest
        t2 = time_to_accelerate + time_rest + time_to_decelerate

        lt = 0
        la = 0
        lv = 0
        lh = 0
        lw = 0
        while lt < t0:
            la = -self.acceleration
            lv += la * self.dt
            self.h += (lv * self.dt) + (la * self.dt ** 2) / 2
            lt += self.dt
            self.t += self.dt

            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            self.array_h.append(self.h)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)

        while lt < t1:
            la = 0
            lv += la * self.dt
            self.h += (lv * self.dt) + (la * self.dt ** 2) / 2
            lt += self.dt
            self.t += self.dt
            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            self.array_h.append(self.h)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)

        while lt < t2:
            la = self.acceleration
            lv += la * self.dt
            self.h += (lv * self.dt) + (la * self.dt ** 2) / 2
            lt += self.dt
            self.t += self.dt
            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            self.array_h.append(self.h)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)

        while lt < t2 + self.pause * self.dt:
            la = 0
            lv += 0
            self.h += 0
            lt += self.dt
            self.t += self.dt
            self.array_t.append(self.t)
            self.array_a.append(la)
            self.array_v.append(lv)
            self.array_h.append(self.h)
            lw = self.weight * (self.g + la)
            self.array_w.append(lw)
        return self


def draw_graphics():
    cl = Object().go_up().go_up().go_down(2)

    plt.title("Высота")
    plt.plot(cl.array_t, cl.array_h)
    plt.savefig(r'res/height.png')
    # plt.show()
    plt.close()

    plt.title("Скорость")
    plt.plot(cl.array_t, cl.array_v)
    plt.savefig(r'res/velocity.png')
    # plt.show()
    plt.close()

    plt.title("#" + "Ускро")
    plt.plot(cl.array_t, cl.array_a)
    plt.savefig(r'res/acceleration.png')
    # plt.show()
    plt.close()


# https://stackoverflow.com/questions/63671018/how-can-i-draw-an-arrow-using-pil
def arrowedLine(draw, ptA, ptB, width=1, color=(0, 255, 0)):
    """Draw line from ptA to ptB with arrowhead at ptB"""
    # Get drawing context
    # Draw the line without arrows
    draw.line((ptA, ptB), width=width, fill=color)

    # Now work out the arrowhead
    # = it will be a triangle with one vertex at ptB
    # - it will start at 95% of the length of the line
    # - it will extend 8 pixels either side of the line
    x0, y0 = ptA
    x1, y1 = ptB
    # Now we can work out the x,y coordinates of the bottom of the arrowhead triangle
    xb = 0.95 * (x1 - x0) + x0
    yb = 0.95 * (y1 - y0) + y0

    # Work out the other two vertices of the triangle
    # Check if line is vertical
    if x0 == x1:
        vtx0 = (xb - 5, yb)
        vtx1 = (xb + 5, yb)
    # Check if line is horizontal
    elif y0 == y1:
        vtx0 = (xb, yb + 5)
        vtx1 = (xb, yb - 5)
    else:
        alpha = math.atan2(y1 - y0, x1 - x0) - 90 * math.pi / 180
        a = 8 * math.cos(alpha)
        b = 8 * math.sin(alpha)
        vtx0 = (xb + a, yb + b)
        vtx1 = (xb - a, yb - b)

    # draw.point((xb,yb), fill=(255,0,0))    # DEBUG: draw point of base in red - comment out draw.polygon() below if using this line
    # im.save('DEBUG-base.png')              # DEBUG: save

    # Now draw the arrowhead triangle
    draw.polygon([vtx0, vtx1, ptB], fill=color)
    return draw


def draw_anim():
    obj = Object().go_up().go_up().go_down(2)
    m_to_px = 40
    width = 1000
    height = 1000
    color_2 = (0, 0, 0)
    color_1 = (255, 255, 255)
    color_3 = (255, 0, 0)
    color_4 = (0, 255, 0)
    color_5 = (100, 100, 100)
    mult = 4
    frames = []

    lift_width = obj.distance * m_to_px / 1.6
    lift_height = obj.distance * m_to_px
    person_width = lift_width / 1.7
    person_height = lift_height / 1.7
    try:
        font = ImageFont.truetype('GoogleSans-Regular.ttf', 32)
    except OSError:
        print('add a font with utf-8 support to the project directory')
        return

    for i in range(len(obj.array_t)):
        x = width // 2
        y = height * 2 / 3 - person_height // 2- obj.array_h[i] * m_to_px
        # y = height - person_height // 2 - 32 - obj.array_h[i] * m_to_px
        im = Image.new('RGB', (width, width), color_1)
        draw = ImageDraw.Draw(im)

        draw.rectangle(  # лифт
            (
                x - lift_width // 2,
                y - lift_height + person_height // 2,
                x + lift_width // 2,
                y + lift_height // 2 - (lift_height // 2 - person_height // 2)
            ),
            fill=color_2
        )

        draw.rectangle(  # чел
            (
                x - person_width // 2,
                y - person_height // 2,
                x + person_width // 2,
                y + person_height // 2
            ),
            fill=color_5
        )

        arrowedLine(  # сила реакции опоры
            draw,
            (x, y),
            (x, y - obj.array_w[i] / mult),
            color=color_3
        )

        arrowedLine(  # сила тяжести
            draw,
            (x, y),
            (x, y + obj.weight * obj.g / mult),
            color=color_4
        )

        draw.text(  # модуль силы реакции опоры
            (x + 32, y - obj.array_w[i] / (mult * 2)),
            'N = {weight: .2f} Н'.format(weight=obj.array_w[i]),
            fill=color_3,
            font=font
        )

        draw.text(  # легенда > ускорение
            (100, 100),
            'a = {a: .2f} м/сек^2'.format(a=obj.array_a[i]),
            fill=color_2,
            font=font
        )

        draw.text(  # легенда > скорость
            (100, 200),
            'v = {v: .2f} м/сек'.format(v=obj.array_v[i]),
            fill=color_2,
            font=font
        )

        draw.text(  # легенда > модуль силы реакции опоры
            (100, 300),
            'N = {weight: .2f} Н'.format(weight=obj.array_w[i]),
            fill=color_2,
            font=font
        )

        draw.text(  # легенда > время в движении
            (100, 400),
            't = {t: .2f} сек'.format(t=obj.array_t[i]),
            fill=color_2,
            font=font
        )
        frames.append(im)

    frames[0].save(
        r'res/draw.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=10,
        loop=0
    )


def main():
    draw_anim()
    draw_graphics()
    print(rf'all the graphs are located in {os.path.dirname(os.path.abspath(__file__))}\res')

if __name__ == '__main__':
    main()