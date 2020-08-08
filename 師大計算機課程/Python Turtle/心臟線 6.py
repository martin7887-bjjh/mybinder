from turtle import *
import math
hideturtle()
# speed(9)
tracer(100, 1)
pensize(0.1)
screen = Screen()
screen.colormode(255)
#產生圓的點,畫點


def gen_circle_point(step, radius, x_start=0):
  theta = 0
  circle_list = []
  step_angle = 2*math.pi/step
  for i in range(step):
    circle_list.append(
        (x_start+radius*math.cos(theta), radius*math.sin(theta)))
    theta += step_angle
  for x, y in circle_list:
    penup()
    goto(x, y)
    pendown()
    dot(2)
  return circle_list
#返回最大公因數


def get_gcd(a, b):
  m = a % b
  while (m > 0):
      a = b
      b = m
      m = a % b
  return b


circle1 = gen_circle_point(60, 100, 0)
circle2 = gen_circle_point(30, 100, 900)

circle1_num = len(circle1)
circle2_num = len(circle2)

gcd = get_gcd(circle2_num, circle1_num)
lcm = circle1_num*circle2_num/gcd

for i in range(int(lcm+1)):  # 點的最小公倍數
  pencolor('#AAAAAA')
  penup()
  goto(circle1[i % circle1_num])
  pendown()
  goto(circle2[(circle2_num-i) % circle2_num])

  penup()
  for j in range(2, 3):
    middle_x = (circle1[i % circle1_num][0]) + (circle2[(circle2_num-i) %
                                                        circle2_num][0]-circle1[i % circle1_num][0])*j/4
    middle_y = (circle1[i % circle1_num][1] +
                circle2[(circle2_num-i) % circle2_num][1])/2
    goto(middle_x, middle_y)
    dot(2, (0, 0, 50*j))
done()