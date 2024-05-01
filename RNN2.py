#!/usr/bin/env python
import rospy
from actionlib import SimpleActionClient
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class RobotNavigation:
    def __init__(self, robot_id):
        rospy.init_node(f'navigation_{robot_id}', anonymous=False)
        self.client = SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def send_goal(self, x, y):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.w = 1.0
        rospy.loginfo(f"Robot moving to ({x}, {y})")
        self.client.send_goal(goal)
        self.client.wait_for_result()

if __name__ == '__main__':
    robot = RobotNavigation('robot1')
    robot.send_goal(5.0, 5.0)  # Example coordinates for Point C
