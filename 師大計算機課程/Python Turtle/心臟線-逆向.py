from turtle import *
import math
hideturtle()
speed(0)
# tracer(100,10)
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
    dot(1)
  return circle_list
#返回最大公因數


def get_gcd(a, b):
  m = a % b
  while (m > 0):
      a = b
      b = m
      m = a % b
  return b


circle1 = gen_circle_point(40, 100, 0)
circle2 = gen_circle_point(30, 100, 0)
circle2_reverse = circle2[::-1]

circle1_num = len(circle1)
circle2_num = len(circle2)

gcd = get_gcd(circle2_num, circle1_num)
lcm = circle1_num*circle2_num/gcd

curve_list = []
for i in range(int(lcm+1)):  # 點的最小公倍數
  pencolor('#EEEEEE')
  penup()
  goto(circle1[i % circle1_num])
  pendown()
  # goto(circle2[i%circle2_num])

  #reverse
  goto(circle2_reverse[i % circle2_num])

  penup()

  for j in range(2, 3):
    # middle_x = (circle1[i%circle1_num][0]) + (circle2[i%circle2_num][0]-circle1[i%circle1_num][0])*j/4
    # middle_y = (circle1[i%circle1_num][1] + circle2[i%circle2_num][1])/2

    #reverse
    middle_x = (circle1[i % circle1_num][0]) + (circle2_reverse[i %
                                                                circle2_num][0]-circle1[i % circle1_num][0])*j/4
    middle_y = (circle1[i % circle1_num][1] +
                circle2_reverse[i % circle2_num][1])/2

    goto(middle_x, middle_y)
    curve_list.append((middle_x, middle_y))
    print(middle_x, middle_y)
    dot(2, (0, 0, 50*j))

curve_list.append(curve_list[0])
print("================")
print(curve_list)
penup()
goto(curve_list[0])
pendown()
pencolor("black")
begin_fill()
for i in range(len(curve_list)):
  goto(curve_list[i])
end_fill()
done()