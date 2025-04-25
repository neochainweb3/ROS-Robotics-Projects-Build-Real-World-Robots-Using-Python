
import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Pin for motor control

def motor_control():
    pwm_motor = GPIO.PWM(17, 100)
    pwm_motor.start(0)
    rospy.init_node('motor_control_node', anonymous=True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        pwm_motor.ChangeDutyCycle(50)
        rate.sleep()

if __name__ == '__main__':
    try:
        motor_control()
    except rospy.ROSInterruptException:
        pass
