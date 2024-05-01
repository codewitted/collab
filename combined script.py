#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from actionlib import SimpleActionClient
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class MultiRobotSystem:
    def __init__(self):
        rospy.init_node('multi_robot_system', anonymous=False)

        # Publishers
        self.nav_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        self.gripper_pub = rospy.Publisher('/gripper_command', String, queue_size=10)
        self.status_pub = rospy.Publisher('/robot_status', String, queue_size=10)

        # Subscribers
        rospy.Subscriber("human_commands", String, self.handle_human_commands)
        rospy.Subscriber("/robot_status", String, self.handle_robot_status)

        # Action client for navigation
        self.client = SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def send_goal(self, x, y):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.w = 1.0
        self.client.send_goal(goal)
        self.client.wait_for_result()

    def command_gripper(self, command):
        self.gripper_pub.publish(command)

    def send_status(self, status):
        self.status_pub.publish(status)

    def handle_human_commands(self, data):
        rospy.loginfo(f"Received command: {data.data}")
        # Command handling logic here

    def handle_robot_status(self, data):
        rospy.loginfo(f"Robot Status Update: {data.data}")
        # Status handling logic here

if __name__ == '__main__':
    system = MultiRobotSystem()
    try:
        system.send_goal(5.0, 5.0)
        system.command_gripper("pick")
        system.send_status("Arrived at Point C")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
