
import rospy
import os
from sensor_msgs.msg import LaserScan
from std_srvs.srv import Empty

def lidar_callback(data):
    rospy.loginfo("Processing Lidar data...")

def start_gmapping():
    rospy.init_node('start_gmapping', anonymous=True)
    os.system("roslaunch gmapping slam_gmapping.launch")
    rospy.Subscriber('/scan', LaserScan, lidar_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_gmapping()
    except rospy.ROSInterruptException:
        pass
