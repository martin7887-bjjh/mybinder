from turtle import *
import math
hideturtle()
speed(0)
# tracer(50,2)
screen = Screen()
screen.colormode(255)
screen.setup(1200,800)
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


# circle1 = gen_circle_point(30, 100, 0)
# circle2 = gen_circle_point(60, 100, 900)
circle1 = gen_circle_point(30, 100, -500)
circle2 = gen_circle_point(60, 100, 400)
circle2_reverse = circle2[::-1]

circle1_num = len(circle1)
circle2_num = len(circle2)

gcd = get_gcd(circle2_num, circle1_num)
lcm = circle1_num*circle2_num/gcd

# 記錄三個心臟線的軌跡
curve_dict = {1: [], 2: [], 3: []}

# 開始畫圖
for i in range(int(lcm+1)):  # 點的最小公倍數
  pencolor('#EEEEEE')
  penup()
  goto(circle1[i % circle1_num])
  pendown()

  # 同向
  goto(circle2[i % circle2_num])

  # 一正一反
  # goto(circle2_reverse[i%circle2_num])

  penup()

  for j in range(1, 4):
    # 同向
    middle_x = (circle1[i % circle1_num][0]) + (circle2[i %
                                                        circle2_num][0]-circle1[i % circle1_num][0])*j/4
    middle_y = (circle1[i % circle1_num][1]) + (circle2[i %
                                                        circle2_num][1]-circle1[i % circle1_num][1])*j/4

    # 一正一反
    # middle_x = (circle1[i%circle1_num][0]) + (circle2_reverse[i%circle2_num][0]-circle1[i%circle1_num][0])*j/4
    # middle_y = (circle1[i%circle1_num][1] + circle2_reverse[i%circle2_num][1])*j/4

    goto(middle_x, middle_y)
    curve_dict[j].append((middle_x, middle_y))
    print(middle_x, middle_y)
    dot(2, (0, 0, 50*j))


# 描繪心臟線
pencolor("blue")
for i in range(1, 4):
  pencolor(0, 0, 50*i)
  penup()
  goto(curve_dict[i][0])
  pendown()
  for j in range(len(curve_dict[i])):
    goto(curve_dict[i][j])


# print("circle1")
# print(circle1)
# print("circle2")
# print(circle2)
# print("curve[1]")
# print(curve_dict[1])
# print("curve[2]")
# print(curve_dict[2])
# print("curve[3]")
# print(curve_dict[3])

done()
