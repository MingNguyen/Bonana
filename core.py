import numpy as np
from math import cos,sin,pi,sqrt
class donut():
    def __init__(self):

        self.R1 = 2
        self.A, self.B = 0,0
        self.A_PACE,self.B_PACE = 0.314,0.0785
        self.THETA_PACE,self.PHI_PACE = 0.04,0.06

        self.circle_center_vector = np.array((self.R1, 0, 0))
        self.surface_normal = []
        self.cordinate_3D = []
        self.rotating_circle_matrix,self.x_rotating_banana,self.y_rotating_banana,self.move = (np.array(
            [[
                [ 1, 0, 0],
                [ 0, 1, 0],
                [ 0, 0, 1]
            ]] * 4
        ))
        self.run()

    
    def circle_point(self,new_R2):

        circle_draw = np.array((new_R2 * cos(self.phi),new_R2 * sin(self.phi), 0))
        self.normal_surface = np.array((cos(self.phi),sin(self.phi),0))
        self.circle = self.circle_center_vector + circle_draw
        self.phi += self.PHI_PACE

    def update_R2(self,R2):
        if 2 >= R2 and R2 >1.7: return 0.42
        elif 1.7 >= R2 and R2 > 1.5: return (0.798-0.42* R2)/0.2
        elif 1.5 >= R2 and R2 > -1.4: return (2.676 - 0.16*R2)/2.9
        elif -1.4 >= R2 and R2 >= -sqrt(3): return (-7/25 +sqrt(3) +0.8 *R2)/(sqrt(3)-1.4)
    
    def write_cordinate(self,frame):
        self.cordinate_3D[frame].append(self.torus + np.array((0,0,5)))
        self.surface_normal[frame].append(self.banana_normal_surface) 

    def draw_banana(self,frame):
        self.theta = 0
        while self.theta < 5*pi/6:
            self.R2 = 2 * cos(self.theta)
            new_R2 = self.update_R2(self.R2)
            self.theta += self.THETA_PACE
            
            self.a = self.move @ self.rotating_circle_matrix
            self.phi = 0
            while self.phi < 2*pi:
                self.phi += self.PHI_PACE
                self.circle_point(new_R2)
                self.torus =  self.a @ self.circle
                self.banana_normal_surface = self.a @ self.normal_surface
                self.write_cordinate(frame)
            
            self.rotating_circle_matrix = np.array(
                (
                    (cos(self.theta), 0, sin(self.theta)),
                    (0, 1, 0),
                    (-sin(self.theta), 0, cos(self.theta))
                )
            )
        
    def new_frame(self):
        self.A += self.A_PACE
        self.B += self.B_PACE
        self.x_rotating_banana = np.array(
                (
                    (1, 0, 0),
                    (0, cos(self.A),-sin(self.A)),
                    (0, sin(self.A), cos(self.A))
                )
            )
        self.z_rotating_banana = np.array(
                (
                    (cos(self.B),-sin(self.B), 0),
                    (sin(self.B), cos(self.B), 0),
                    (0, 0, 1)
                )
            )
        self.move = self.x_rotating_banana @ self.z_rotating_banana


    def run(self):
        frame = 0
        while self.B < 2*pi:
            self.cordinate_3D.append([])
            self.surface_normal.append([])   
            self.draw_banana(frame)
            self.new_frame()
            frame += 1
a = donut()