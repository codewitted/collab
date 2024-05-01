#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f"Received command from human interface: {data.data}")

def listener():
    rospy.init_node('human_interface_listener', anonymous=True)
    rospy.Subscriber("human_commands", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
