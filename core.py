#import the library is used
import numpy as np
from math import cos,sin,pi,sqrt
class banana():
    
    def __init__(self):
        # R1 is the distance between the circle center point to the center of the coordinate
        self.R1 = 2
        # A, B is the rotating x and z axis 
        self.A, self.B = 0,0
        # the pace to use for the movement of the angle
        self.A_PACE,self.B_PACE = 0.314,0.0785
        self.THETA_PACE,self.PHI_PACE = 0.04,0.09
        # the depth and the circle center point is used for moving the object to a new virtual coordinate system
        self.depth = np.array((0,0,6))
        self.circle_center_vector = np.array((self.R1, 0, 0))
        # these to in 3D dimension which to memorise the frame, the point and that point cordinate
        self.surface_normal_3D = []
        self.cordinate_3D = []
        # these are the rotating matrix
        self.rotating_circle_matrix,self.x_rotating_banana,self.y_rotating_banana,self.move = (np.array(
            [[
                [ 1, 0, 0],
                [ 0, 1, 0],
                [ 0, 0, 1]
            ]] * 4
        ))
        #after the next command, the program will go to line 112
        self.run()
        
    def draw_circle(self,R2,frame):
        #update the cordinate and surface normal of the circle
        circle_point = np.array((R2 * cos(self.phi),R2 * sin(self.phi), 0))
        self.circle_surface_normal = np.array((cos(self.phi),sin(self.phi),0))
        #move the circle to it center
        self.circle = self.circle_center_vector + circle_point
        #update the value of the angle phi
        self.phi += self.PHI_PACE
        #make the dot products to get the banana cordinate and surface normal in a frame
        self.banana =  self.temporary @ self.circle
        self.banana_surface_normal = self.temporary @ self.circle_surface_normal
        #this function is to save the output of core, go to line 59
        self.write_cordinate(frame)
        # Recursion to loop the action of draw circle
        self.phi += self.PHI_PACE
        # recursion to draw banana
        if self.phi < 2*pi:
            # go to line 31
            return self.draw_circle(R2,frame)
        else: return 0

    def update_R2(self,x):
        #these function is to create value for r2
        if 2 >= x and x >1.6: return 0.15
        elif 1.6 >= x and x > 1.5: return (0.447-0.27* x)/0.1
        elif 1.5 >= x and x > -1.4: return (2.676 - 0.16*x)/5.8
        elif -1.4 >= x and x >= -sqrt(3): return (-7/25 +sqrt(3) +0.8 *x)/(sqrt(3)-1.4)/2
    
    def write_cordinate(self,frame):
        # to write the cordinate to the generators which are the output
        self.cordinate_3D[frame].append(self.banana + self.depth)
        self.surface_normal_3D[frame].append(self.banana_surface_normal) 

    def draw_banana(self,frame):
        banana_point = self.R1 * cos(self.theta)
        #go to line 39
        R2 = self.update_R2(banana_point)
        #update new value of theta after has been used 
        # temporary matrix is to contain all 3 rotation and its dot product
        self.temporary = self.move @ self.rotating_circle_matrix
        # phi is the angle for "circle matrix" to move the circle to a new cordinate
        self.phi = 0
        # make the loops until a circle has been drawn, go to line 49
        self.draw_circle(R2,frame)
                

        #update the rotation matrixes
        self.rotating_circle_matrix = np.array(
            (
                    (cos(self.theta), 0, sin(self.theta)),
                    (0, 1, 0),
                    (-sin(self.theta), 0, cos(self.theta))
            )
        )
        self.theta += self.THETA_PACE
        if self.theta < 5/6*pi: return self.draw_banana(frame)
        else: return 0
        
    def new_frame(self):
        #update the angle any time the function is called
        self.A += self.A_PACE
        self.B += self.B_PACE
        #update the rotation matrixes
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
        #this is the dot product between 2 rotation matrixes
        self.move = self.x_rotating_banana @ self.z_rotating_banana

    # This function is to start the drawing banana in 3D space
    def run(self):
        # frame is a local value to index the movement of the banana
        frame = 0
        # this command is to require the system to run all the frame can happen
        while self.B < 2*pi:
            # 2 next commands require to make a new generator to install the value of a new frame
            self.cordinate_3D.append([])
            self.surface_normal_3D.append([])
            # this command is to draw a banana and go to the line 64
            self.theta = 0
            self.draw_banana(frame)
            # this comment is to update some variables, go to line 89
            self.new_frame()
            frame += 1
