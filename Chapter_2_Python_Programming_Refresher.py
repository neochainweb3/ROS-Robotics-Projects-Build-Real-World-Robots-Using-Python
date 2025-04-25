
import rospy
from geometry_msgs.msg import Twist
import numpy as np

MAX_RANGE = 3.0  # meters

def lidar_callback(data):
    filtered_ranges = np.array(data.ranges)
    filtered_ranges[filtered_ranges > MAX_RANGE] = float('inf')
    min_distance = np.min(filtered_ranges)
    rospy.loginfo(f"Closest object at: {min_distance} meters")

def lidar_listener():
    rospy.init_node('lidar_listener', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, lidar_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_listener()
    except rospy.ROSInterruptException:
        pass
