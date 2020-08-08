from math import *
from PIL import Image
im=Image.open("lempert.jpg")
m=im.size[0]
n=im.size[1]
new=Image.new('RGB',(m,n),(0,0,0))
c=[(0,0,0), (255,0,0),(255,255,0),(0,255,0),(0,255,255),
   (0,0,255),(255,0,255),(255,255,255)]
print(int(-0.1),floor(-0.1))
d=255*sqrt(3)/len(c)
for i in range(m):
    for j in range(n):
        r,g,b=im.getpixel((i,j))
        norm=sqrt(r**2+g**2+b**2)
        if 0<norm<2*d:
            x=norm/(2*d)
            nnorm=6*d*(x**0.5)
            R=nnorm*r/norm;G=nnorm*g/norm;B=nnorm*b/norm
        else:
            R=r;G=g;B=b

        new.putpixel((i,j),(int(R),int(G),int(B)))        
new.save("test_D.jpg")
print("OK")
