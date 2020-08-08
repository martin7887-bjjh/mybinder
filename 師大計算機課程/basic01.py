from math import *
from PIL import Image
im=Image.open("t0.jpg")
m=im.size[0]
n=im.size[1]
new=Image.new('RGB',(m,n),(0,0,0))
def f1(x):
    return int(255*sqrt(x/255))

def f2(x):
    x=x/255  #轉換x 到0, 1之間
    y=3*x**(1/3)-3*x**(2/3)+x
    y=y**2
    return int(255*y)

def f(x):  #此x 必須在0, 1之間
    y=sin(x*pi/2)
    return y

for i in range(m):
    for j in range(n):
        r,g,b=im.getpixel((i,j))
        R=int(255*f(f(f(f(r/255)))))
        G=int(255*f(f(f(f(g/255)))))
        B=int(255*f(f(f(f(b/255)))))
        new.putpixel((i,j),(R,G,B))        
new.save("test_C.jpg")
print("OK")
