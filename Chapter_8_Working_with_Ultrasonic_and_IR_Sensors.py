
import rospy
from sensor_msgs.msg import Range
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

def ultrasonic_callback(data):
    distance = GPIO.input(18)
    rospy.loginfo(f"Distance measured: {distance} cm")

def ultrasonic_listener():
    rospy.init_node('ultrasonic_listener', anonymous=True)
    rospy.Subscriber('/ultrasonic_data', Range, ultrasonic_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        ultrasonic_listener()
    except rospy.ROSInterruptException:
        pass
