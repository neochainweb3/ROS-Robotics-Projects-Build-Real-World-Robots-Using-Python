
import rospy
from geometry_msgs.msg import Twist

def move_robot():
    rospy.init_node('move_robot_node', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)
    move_cmd = Twist()
    move_cmd.linear.x = 0.5
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
