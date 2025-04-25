
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

def move_robot():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('move_robot_node', anonymous=True)
    move_cmd = Twist()
    move_cmd.linear.x = 0.5
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

def service_client():
    rospy.wait_for_service('reset_position')
    try:
        reset_position = rospy.ServiceProxy('reset_position', Empty)
        reset_position()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    try:
        move_robot()
        service_client()
    except rospy.ROSInterruptException:
        pass
