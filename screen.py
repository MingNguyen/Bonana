import numpy as np
from math import cos,sin,pi
from core import donut
from os import system
from time import sleep

class show():
    def __init__(self,cordinate_3D,surface_normal):
        self.surface_normal = surface_normal
        self.shadow = '.,-~:;*/=#$@'
        self.cordinate_3D = cordinate_3D
        self.width = 65

        self.K2 = 4
        self.K1 = self.width*self.K2*3/(8*3)
        self.light_source = np.array((0,1,-1))
        self.zbuffer = [[[0 for i in range(self.width)] for j in range(self.width)] for k in range(len(self.cordinate_3D))]
        self.output = [[[' ' for i in range(self.width)] for j in range(self.width)] for k in range(len(self.cordinate_3D))]

        self.protection()

    def protection(self):
        for i in range(len(self.cordinate_3D)):
            for j in range(len(self.cordinate_3D[0])):
                x,y,z = self.cordinate_3D[i][j]
                ooz = 1/z
                xp = int(self.width/2 + self.K1*ooz*x)
                yp = int(self.width/2 - self.K1*ooz*y)
                L = self.surface_normal[i][j] @ self.light_source
                if L > 0:
                    if ooz > self.zbuffer[i][xp][yp]:
                        l_index = int(L*8)
                        self.zbuffer[i][xp][yp] = ooz
                        self.output[i][xp][yp] = self.shadow[l_index]

action = donut()
cordinate = action.cordinate_3D
surface_normal = action.surface_normal
del action
alo = show(cordinate,surface_normal)

h = ['']
for i in range(len(alo.output)):
    for j in range(len(alo.output[0])):
        for k in range(len(alo.output[0][0])):
            h[i] += alo.output[i][j][k]
        h[i] += '\n'
    h.append('')
i = 0
while True:
    if i < len(alo.output):
        system("cls")
        print('\n\n\n\n\n')
        print(h[i])
        sleep(0.07)
        i += 1
    else: i = 0