#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f"Received command: {data.data}")

def setup_communication():
    rospy.init_node('human_robot_communication', anonymous=True)
    rospy.Subscriber("human_commands", String, callback)
    rospy.spin()

if __name__ == '__main__':
    setup_communication()
