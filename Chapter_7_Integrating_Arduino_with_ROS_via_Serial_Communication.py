
import rospy
import serial
from std_msgs.msg import String

ser = serial.Serial('/dev/ttyUSB0', 9600)

def arduino_callback(data):
    ser.write(data.data.encode())

def arduino_listener():
    rospy.init_node('arduino_listener', anonymous=True)
    rospy.Subscriber('/arduino_data', String, arduino_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        arduino_listener()
    except rospy.ROSInterruptException:
        pass
