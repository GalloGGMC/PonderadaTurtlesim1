import rclpy
import turtle
import numpy as np
from rclpy.node import Node
from turtlesim.srv import SetPen, TeleportRelative
from geometry_msgs.msg import Twist
import time
import os

class Moviment(Node):

    def __init__(self):
        os.system(str('ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "' +"'"+'off'+"'"+': 1"'))
        super().__init__('movement')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        msg = Twist()
        msg.linear.x, msg.linear.y = -4.0, -3.0
        self.publisher_.publish(msg)
        time.sleep(1)
        os.system('ros2 service call /turtle1/set_pen turtlesim/SetPen "width: 7"')
        self.timer = self.create_timer(1.2, self.timer_callback)
        self.sides = [[1.0,0.0],[-0.5,0.9],[-0.5,-0.9],[0.5,0.9],[0.5,-0.9],[-1.0,0]]
        self.sizes = [8.0,4.0,3.0,2.0,1.0]
        self.order = [0,1,2,0,1,0,2,0,1,0,2,0,1,5,3,5,4,5,2,0,2,1,2,0,1,0,2,0,1,0,2,0,1,2,1,0,1,3,0,2,1,3,4,3,5,3,4,5,4,3,4,5,4,3,4,5,4,3,4,5,3,5,4]
        self.step = [0,0,0,1,1,1,1,3,3,3,3,3,1,3,3,3,3,3,3,3,3,3,3,4,4,4,4,3,4,4,4,4,2,4,4,4,4,4,4,4,4,3,4,4,4,4,2,4,4,4,3,4,4,4,3,4,4,4,4,2,4,4,4]
        self.index = 0
        self.counter = 0
        

    def timer_callback(self):
        msg = Twist()
        if self.index < len(self.order):
            msg.linear.x, msg.linear.y = round(self.sides[self.order[self.index]][0]*self.sizes[self.step[self.index]],2), round(self.sides[self.order[self.index]][1]*self.sizes[self.step[self.index]],2)
            self.publisher_.publish(msg)
            self.index += 1
        else:
            os.system(str('ros2 service call /kill turtlesim/srv/Kill ' +"'"+'name: "turtle1"'+"'"))
            time.sleep(0.5)
            exit(1)
    

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = Moviment()

    rclpy.spin(minimal_publisher)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
