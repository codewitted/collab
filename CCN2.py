#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Bool

class CentralCoordinator:
    def __init__(self):
        rospy.init_node('central_coordinator', anonymous=False)
        self.robot_active_pub = rospy.Publisher('/robot_active', Bool, queue_size=10)
        rospy.Subscriber('/human_requests', String, self.handle_request)

    def handle_request(self, data):
        # Logic to decide which robot moves based on the item color requested
        rospy.loginfo(f"Request for {data.data} item received")
        self.dispatch_robot(data.data)

    def dispatch_robot(self, item_color):
        # Send command to the appropriate robot
        self.robot_active_pub.publish(True)  # Example: Signal robot to start
        rospy.loginfo(f"Robot dispatched for {item_color} item")

if __name__ == '__main__':
    coord = CentralCoordinator()
    rospy.spin()
