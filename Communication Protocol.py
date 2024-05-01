#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def send_status(status):
    rospy.init_node('robot_status_sender', anonymous=True)
    pub = rospy.Publisher('/robot_status', String, queue_size=10)
    rospy.loginfo(status)
    pub.publish(status)

if __name__ == '__main__':
    send_status("Arrived at Point C")
