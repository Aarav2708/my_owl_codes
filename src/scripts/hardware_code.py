from owl_client import OwlClient, Joint, Pose
import time
import math

class OwlRobotController:
    """OwlRobotController for controlling hardware using OwlClient"""

    def __init__(self, ip_address="10.42.0.54"):
        # Initialize OwlClient connection
        self.client = OwlClient(ip_address)
        self.tool_speed = 100  # mm/sec

        # Wait for the robot to be available
        while not self.client.is_running():
            time.sleep(0.2)
        print("Robot is now available for control.")

    def go_to_joint_goal(self, joint_position):
        """
        Move the robot to a specified joint goal asynchronously.
        joint_position: A dictionary with joint names as keys and angles in radians as values.
        """
        # Initialize a Joint object with the provided joint goal
        joint_goal = Joint()
        joint_goal.Base = joint_position.get("Base", 0.0)
        joint_goal.Shoulder = joint_position.get("Shoulder", 0.0)
        joint_goal.Elbow = joint_position.get("Elbow", -math.pi / 2)
        joint_goal.Wrist1 = joint_position.get("Wrist1", 0.0)
        joint_goal.Wrist2 = joint_position.get("Wrist2", 0.0)
        joint_goal.Wrist3 = joint_position.get("Wrist3", 0.0)

        # Move to joint position asynchronously
        self.client.move_to_joint(joint_goal, 50, wait=False)
        time.sleep(1)
        self.client.move_abort()
        print("Moved to joint goal:", joint_position)

    def go_to_pose_goal(self, pose_position):
        """
        Move the robot to a specified pose goal asynchronously.
        pose_position: A dictionary with pose (x, y, z, roll, pitch, yaw) in meters and radians.
        """
        # Initialize a Pose object with the provided pose goal
        pose_goal = Pose()
        pose_goal.x = pose_position.get("x", -0.176)
        pose_goal.y = pose_position.get("y", -0.240204)
        pose_goal.z = pose_position.get("z", 0.489203)
        pose_goal.roll = pose_position.get("roll", 3.1376)
        pose_goal.pitch = pose_position.get("pitch", -0.087288)
        pose_goal.yaw = pose_position.get("yaw", 1.56449)

        # Move to pose position asynchronously
        self.client.move_to_pose(pose_goal, self.tool_speed, wait=False)
        time.sleep(1)
        self.client.move_abort()
        print("Moved to pose goal:", pose_position)

    def go_to_circular_path(self, center, radius, steps=36):
        """
        Generates and moves the robot along a circular path in the x-y plane.
        center: A dictionary with x, y, and z coordinates of the circle's center.
        radius: The radius of the circular path.
        steps: Number of waypoints to define the circle (default is 36 for a 10-degree increment).
        """
        # Generate waypoints around the circle
        for i in range(steps + 1):
            angle = 2 * math.pi * i / steps  # Calculate angle for each waypoint

            # Define waypoint positions based on the circle's center and radius
            pose_goal = Pose()
            pose_goal.x = center["x"] + radius * math.cos(angle)
            pose_goal.y = center["y"] + radius * math.sin(angle)
            pose_goal.z = center["z"]
            pose_goal.roll = 3.1376  # Use fixed roll, pitch, yaw as example
            pose_goal.pitch = -0.087288
            pose_goal.yaw = 1.56449

            # Move to each waypoint in sequence
            self.client.move_to_pose(pose_goal, self.tool_speed, wait=True)  # Wait for each pose
            print(f"Reached waypoint at angle {math.degrees(angle)} degrees")


def main():
    # Initialize the OwlRobotController
    robot_controller = OwlRobotController()

    # Define the joint goal as a dictionary with joint angles in radians
    joint_goal = {
        "Base": 0.0,
        "Shoulder": 0.0,
        "Elbow": -math.pi / 2,   # -90 degrees in radians
        "Wrist1": 0.0,
        "Wrist2": 0.0,
        "Wrist3": 0.0
    }
    
    # Move to the joint goal
    robot_controller.go_to_joint_goal(joint_goal)

    # Define the center and radius for the circular path
    center = {"x": 0.5, "y": 0.1, "z": 0.4}
    radius = 0.1
    
    # Move in a circular path
    robot_controller.go_to_circular_path(center, radius)


if __name__ == "__main__":
    main()
