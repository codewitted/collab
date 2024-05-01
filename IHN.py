#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class ItemHandler:
    def __init__(self, robot_id):
        rospy.init_node(f'item_handler_{robot_id}', anonymous=True)
        self.pub = rospy.Publisher(f'/gripper_command_{robot_id}', String, queue_size=10)

    def handle_item(self, command):
        rospy.loginfo(f"{command.capitalize()} item")
        self.pub.publish(command)

if __name__ == '__main__':
    handler = ItemHandler('robot1')
    handler.handle_item("pick")  # "pick" or "drop"
