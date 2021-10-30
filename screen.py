#import some library 
import numpy as np
from math import cos,sin,pi
from os import system
from time import sleep
#import the banana class from core.py file
from core import banana
class show():
    def __init__(self,cordinate_3D,surface_normal):
        #save the output in class variable
        self.surface_normal = surface_normal
        self.cordinate_3D = cordinate_3D
        # string that demonstrate the lightness
        self.shadow = '.,-~:;=!*#$@'
        # in this code, we set the screen in square as the default
        self.width = 65
        # the distance from the watcher to the screen
        self.K1 = 40
        # the luminance direction.
        self.light_direction = np.array((0,1,-1))
        # z-buffer is to contain the value of ooz, it has 3Dspace
        self.zbuffer = [[[0 for i in range(self.width)] for j in range(self.width)] for k in range(len(self.cordinate_3D))]
        # our output needs to be written
        self.output = [[[' ' for i in range(self.width)] for j in range(self.width)] for k in range(len(self.cordinate_3D))]
        #goto line 27
        self.protection()

    def protection(self):
        # to scan all frame
        for i in range(len(self.cordinate_3D)):
            #to scan all point
            for j in range(len(self.cordinate_3D[0])):
                # these are the coordinate number
                x,y,z = self.cordinate_3D[i][j]
                # ooz is used to compare the depth of 2 point have a same x and y
                ooz = 1/z
                # we caculate the location of projection on screen 
                xp = int(self.width/2 + self.K1*ooz*x)
                # the equation is minus because the upper y in the coordinate system is the lower b in the screen show
                yp = int(self.width/2  - self.K1*ooz*y)
                #calculate the luminance
                luminance = self.surface_normal[i][j] @self.light_direction
                #if the point have the luminance higher than 0 and the if it have same x,y to the previous point,
                #mke sure that only show which is mostly shining
                if luminance > 0 and ooz > self.zbuffer[i][xp][yp]:
                    #max of luminance is sqrt(2) so the max value of l index = 12 = len(shadow)
                    l_index = int(luminance*8)
                    #update the zbuffer
                    self.zbuffer[i][xp][yp] = ooz
                    #update the output with the shadow
                    self.output[i][xp][yp] = self.shadow[l_index]

action = banana()
# We take the output of the banana
cordinate = action.cordinate_3D
surface_normal = action.surface_normal_3D
# to reduce ram memories
del action
#output the banana is input of show
alo = show(cordinate,surface_normal)
# we only take the  output of show
a = alo.output
# to reduce ram memories
del alo
# these line are to transfer the output from the coordinate form to the string form
h = ['']
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(a[0][0])):
            h[i] += a[i][j][k]
        h[i] += '\n'
    h.append('')
i = 0
#this line is to show it on the screen
while True:
    if i < len(a):
        system("cls")
        print(h[i])
        sleep(0.07)
        i += 1
    else: i = 0

recursion(h,i)
