import subprocess
import time


res1 = subprocess.Popen('ros2 run turtlesim turtlesim_node', shell=True,stdout=subprocess.PIPE)
time.sleep(0.5)
res2 = subprocess.Popen('ros2 run turtlesim turtle_teleop_key', shell=True,stdout=subprocess.PIPE)
time.sleep(0.5)
res3 = subprocess.Popen('python3 ros_tutorials/turtlesim/tutorials/turtle_drawing.py', shell=True,stdout=subprocess.PIPE)  


while True:
    if res3.poll() is not None:
        time.sleep(1)
        res1.kill()
        res2.kill()
        res3.kill()
        exit(1)

# os.system('ros2 run turtlesim turtlesim_node')
# os.system('ros2 run turtlesim turtle_teleop_key')
# os.system('ros2 run turtlesim tutorials turtle_drawing')