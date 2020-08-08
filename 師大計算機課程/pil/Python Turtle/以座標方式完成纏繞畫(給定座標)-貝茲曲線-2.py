# 說明
# 將多邊形的每個邊分成100等分，
# 把每個邊長的第10個等分點連線形成下一個多邊形，

from turtle import *
import math
# speed(0)

tracer(50, 1)
hideturtle()
screen = Screen()


def draw_iter_shape(point_dict, iter_times=10):

  def distence(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

  def move_to_next_start(arr, index):
    # 移動到下一個圖形的起始點
    penup()
    goto(arr[index])
    pendown()

  def points_dot(points):
    for i in points.values():
      penup()
      goto(i)
      dot(3)
      write(i)

  def input_coordinate():
    coordinate_dict = {}
    num = 0
    key = input("please enter the coordinate")
    print(key)
    while((key != 'q') and (key != 'Q')):
      key = key[1:-1]
      coordinate = (float(key.split(",")[0]), float(key.split(",")[1]))
      coordinate_dict[num] = coordinate
      num += 1
      key = input("please enter the coordinate")
    print(coordinate_dict)
    return coordinate_dict

  before_dict = {}
  next_dict = {}
  before_arr, next_arr = [], []

  coordinate_dict = point_dict

  # 從第一點出發
  penup()
  goto(coordinate_dict[0])
  pendown()

  # 頂點數 == 邊長數
  num_of_coor = len(coordinate_dict)
  num_of_coor_arr = range(num_of_coor)
  # 把最後一個補上去才能完成繞一圈
  num_of_coor_arr.append(0)

  # 切幾等份
  edge_size = 100
  for edge_index in range(num_of_coor):
    # 後點減前點的△X，△Y
    x_step = (coordinate_dict[num_of_coor_arr[edge_index+1]][0] -
              coordinate_dict[num_of_coor_arr[edge_index]][0])/edge_size
    y_step = (coordinate_dict[num_of_coor_arr[edge_index+1]][1] -
              coordinate_dict[num_of_coor_arr[edge_index]][1])/edge_size

    next_arr = []
    for i in range(100):
      goto(xcor()+x_step, ycor()+y_step)
      next_arr.append((xcor(), ycor()))
    next_dict[edge_index] = next_arr

  before_dict.clear()
  before_dict = dict(next_dict)
  next_dict.clear()

  # 移到下一個起始點
  move_to_next_start(before_dict[0], 10)

  # 迭代次數
  times = iter_times
  # 全部的第幾個點
  point_index = 10

  for time in range(times):
    for edge_index in range(num_of_coor):
      # print(num_of_coor_arr)
      # print(edge_index)
      x_step = (before_dict[num_of_coor_arr[edge_index+1]][point_index][0] -
                before_dict[num_of_coor_arr[edge_index]][point_index][0])/edge_size
      y_step = (before_dict[num_of_coor_arr[edge_index+1]][point_index][1] -
                before_dict[num_of_coor_arr[edge_index]][point_index][1])/edge_size

      next_arr = []
      for i in range(edge_size):
        goto(xcor()+x_step, ycor()+y_step)
        next_arr.append((xcor(), ycor()))
      next_dict[edge_index] = next_arr

    before_dict.clear()
    before_dict = dict(next_dict)
    next_dict.clear()
    # 移動到下一個圖形的起始點
    move_to_next_start(before_dict[0], 10)


A = (0, -100)
B = (100, -100)
C = (100, 0)
D = (0, 0)
penup()
goto(A)
write("A")
dot(3)
goto(B)
dot(3)
write("B")
goto(C)
dot(3)
write("C")
goto(D)
dot(3)
write("D")

goto(D)
pendown()


for i in range(20):
  # 畫從D→B的貝茲曲線(向C靠近)
  B_step = 1.0/100
  t = 0
  coordinate_dict = {}
  B_arr = []
  for t_times in range(100):
    B_x = (1-t)**2*D[0] + 2*t*(1-t)*C[0] + t**2*B[0]
    B_y = (1-t)**2*D[1] + 2*t*(1-t)*C[1] + t**2*B[1]
    B_arr.append((B_x, B_y))
    goto((B_x, B_y))
    t += B_step
  coordinate_dict[0] = B_arr

  # B→A
  x_step = (A[0] - B[0])/100
  y_step = (A[1] - B[1])/100

  next_arr = []
  for i in range(100):
    goto(xcor()+x_step, ycor()+y_step)
    next_arr.append((xcor(), ycor()))
  coordinate_dict[1] = next_arr

  # A→D
  x_step = (D[0] - A[0])/100
  y_step = (D[1] - A[1])/100

  next_arr = []
  for i in range(100):
    goto(xcor()+x_step, ycor()+y_step)
    next_arr.append((xcor(), ycor()))
  coordinate_dict[2] = next_arr

  # 設定新的點
  D = (coordinate_dict[0][10])
  B = (coordinate_dict[1][10])
  A = (coordinate_dict[2][10])
  C = ((coordinate_dict[1][1][0], coordinate_dict[0][55][1]))

  # 畫下個圖
  pendown()


# t = 0
# coordinate_dict={}
# B_arr = []
# for t_times in range(101):
#   B_x = (1-t)**2*A[0] + 2*t*(1-t)*D[0] + t**2*C[0]
#   B_y = (1-t)**2*A[1] + 2*t*(1-t)*D[1] + t**2*C[1]
#   B_arr.append((B_x,B_y))
#   goto((B_x,B_y))
#   t +=B_step
# coordinate_dict[0] = B_arr

# x_step = (B[0] - C[0])/100
# y_step = (B[1] - C[1])/100

# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))
# coordinate_dict[1] = next_arr

# x_step = (A[0] - B[0])/100
# y_step = (A[1] - B[1])/100

# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))
# coordinate_dict[2] = next_arr


# # =====================
# # 設定新的點
# A = (coordinate_dict[0][10])
# C = (coordinate_dict[1][10])
# B = (coordinate_dict[2][10])
# D = ((A[0],C[1]))

# # 在新的起始點上打點
# penup()
# goto(C)
# dot(3)
# goto(B)
# dot(3)
# goto(D)
# dot(3)
# goto(A)
# dot(3)

# # 畫下個圖
# pendown()
# t = 0
# coordinate_dict={}
# B_arr = []
# for t_times in range(101):
#   B_x = (1-t)**2*A[0] + 2*t*(1-t)*D[0] + t**2*C[0]
#   B_y = (1-t)**2*A[1] + 2*t*(1-t)*D[1] + t**2*C[1]
#   B_arr.append((B_x,B_y))
#   goto((B_x,B_y))
#   t +=B_step
# coordinate_dict[0] = B_arr

# x_step = (B[0] - C[0])/100
# y_step = (B[1] - C[1])/100

# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))
# coordinate_dict[1] = next_arr

# x_step = (A[0] - B[0])/100
# y_step = (A[1] - B[1])/100

# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))
# coordinate_dict[2] = next_arr


def bezier(points):
  coordinate_dict = point_dict

  # 從第一點出發
  penup()
  goto(coordinate_dict[0])
  pendown()

  # 頂點數 == 邊長數
  num_of_coor = len(coordinate_dict)
  num_of_coor_arr = range(num_of_coor)
  # 把最後一個補上去才能完成繞一圈
  num_of_coor_arr.append(0)

  # 切幾等份
  edge_size = 100
  for edge_index in range(num_of_coor):
    # 後點減前點的△X，△Y
    x_step = (coordinate_dict[num_of_coor_arr[edge_index+1]][0] -
              coordinate_dict[num_of_coor_arr[edge_index]][0])/edge_size
    y_step = (coordinate_dict[num_of_coor_arr[edge_index+1]][1] -
              coordinate_dict[num_of_coor_arr[edge_index]][1])/edge_size

    next_arr = []
    for i in range(100):
      goto(xcor()+x_step, ycor()+y_step)
      next_arr.append((xcor(), ycor()))
    next_dict[edge_index] = next_arr

  before_dict.clear()
  before_dict = dict(next_dict)
  next_dict.clear()

  # 移到下一個起始點
  move_to_next_start(before_dict[0], 10)

# penup()
# goto(275,100)
# write(275,100)
# dot(3)
# seth(90)
# pendown()
# circle(125/2)


# scale = 40
# # fig1
# A = (0.0*scale,0.0*scale)
# B = (0.0*scale,4.0*scale)
# C = (3.0*scale,0.0*scale)
# points = {0:A,1:B,2:C,}
# draw_iter_shape(points,iter_times = 30)

# # fig2
# A = (0.0*scale,4.0*scale)
# B = (3.0*scale,4.0*scale)
# C = (3.0*scale,0.0*scale)
# points = {0:A,1:B,2:C,}
# draw_iter_shape(points,iter_times = 30)

# # fig3
# A = (3.0*scale,0.0*scale)
# B = (6.0*scale,4.0*scale)
# C = (3.0*scale,4.0*scale)
# points = {0:A,1:B,2:C}
# draw_iter_shape(points,iter_times = 30)

# # fig4
# A = (3.0*scale,0.0*scale)
# B = (6.0*scale,0.0*scale)
# C = (6.0*scale,4.0*scale)
# points = {0:A,1:B,2:C}
# draw_iter_shape(points,iter_times = 30)


# penup()
# goto(A)
# pendown()
# write('A')
# # B-A /100
# x_step = (B[0] - A[0])/100
# y_step = (B[1] - A[1])/100

# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))
# write("B")

# # C-B / 100
# x_step = (float(C[0]) - (B[0]))/100
# y_step = float(C[1] - B[1])/100
# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))
# write("C")

# # D-C / 100
# x_step = (float(D[0]) - (C[0]))/100
# y_step = float(D[1] - C[1])/100
# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))
# write("D")

# # A-D / 100
# x_step = (float(A[0]) - (D[0]))/100
# y_step = float(A[1] - D[1])/100
# next_arr = []
# for i in range(100):
#   goto(xcor()+x_step,ycor()+y_step)
#   next_arr.append((xcor(),ycor()))


# # 畫第一個形狀
# for i in range(100):
#   next_arr.append((xcor(),ycor()))
#   fd(1)
# next_dict[0] = next_arr
# left(90)
# next_arr = []
# for i in range(80):
#   next_arr.append((xcor(),ycor()))
#   fd(1)
# next_dict[1] = next_arr
# left(90)
# next_arr = []
# for i in range(100):
#   next_arr.append((xcor(),ycor()))
#   fd(1)
# next_dict[2] = next_arr
# left(90)
# next_arr = []
# for i in range(80):
#   next_arr.append((xcor(),ycor()))
#   fd(1)
# next_dict[3] = next_arr
# left(90)

# before_dict.clear()
# before_dict = dict(next_dict)
# next_dict.clear()

# move_to_next_start(before_dict[0],10)

# for loop in range(5):
#   for edge_index in range(4):
#     next_arr=[]
#     x_step = (before_dict[edge_arr[edge_index+1]][10][0] - before_dict[edge_arr[edge_index]][10][0])/100
#     y_step = (before_dict[edge_arr[edge_index+1]][10][1] - before_dict[edge_arr[edge_index]][10][1])/100

#     for i in range(100):
#       goto(xcor()+x_step,ycor()+y_step)
#       next_arr.append((xcor(),ycor()))

#     next_dict[edge_index] = next_arr

#   before_dict.clear()
#   before_dict = dict(next_dict)
#   next_dict.clear()
#   # 移動到下一個圖形的起始點
#   move_to_next_start(before_dict[0],10)
done()