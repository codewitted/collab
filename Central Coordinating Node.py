#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def handle_robot_status(data):
    rospy.loginfo(f"Received status from robot: {data.data}")

def task_dispatcher():
    rospy.init_node('central_coordinator', anonymous=True)
    rospy.Subscriber("/robot_status", String, handle_robot_status)
    # Dispatch tasks to robots based on their status and item needs
    rospy.spin()

if __name__ == '__main__':
    task_dispatcher()
