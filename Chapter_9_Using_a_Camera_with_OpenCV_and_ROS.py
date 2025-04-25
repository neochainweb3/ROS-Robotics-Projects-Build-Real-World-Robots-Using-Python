
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def image_callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.imshow("Camera Feed", cv_image)
    cv2.waitKey(1)

def camera_listener():
    rospy.init_node('camera_listener', anonymous=True)
    rospy.Subscriber('/camera/image_raw', Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        camera_listener()
    except rospy.ROSInterruptException:
        pass
