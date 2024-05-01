#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class ItemHandler:
    def __init__(self):
        rospy.init_node('item_handler', anonymous=True)
        self.pub = rospy.Publisher('/gripper_command', String, queue_size=10)

    def command_gripper(self, command):
        rospy.loginfo(f"Gripper command: {command}")
        self.pub.publish(command)

if __name__ == '__main__':
    handler = ItemHandler()
    handler.command_gripper("pick")  # or "drop" based on the task
