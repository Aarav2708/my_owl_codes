import time
import sys
import signal
import math

from owl_robot_sdk import OwlSimClient

class TestOwlSimClient:
    def __init__(self, group_name, gripper_group):
        self.group_name = group_name

        signal.signal(signal.SIGINT, self.signal_handler)

        print("Application is running. Press Ctrl+C to exit.")

        self.client = OwlSimClient(self.group_name, gripper_group, 5, True)

        self.get_sdk_api()
        self.set_sdk_api()

    def signal_handler(self, sig, frame):
        print("Interrupt received, closing application.")
        sys.exit(0)

    # Testing Get APIs of SDK
    def get_sdk_api(self):
        # Robot Running Status
        status = self.client.is_running()
        print("Robot Running Status:= ", status)

        # Robot Version
        version = self.client.get_version()
        print("Robot Motion Group:= ", version)

        # Get Value of TCP
        tcp_pose = self.client.get_tcp()
        print("Robot TCP position:= ", tcp_pose)

        # Get Value of Joints
        joint_val = self.client.get_joint()
        print("Robot Joint position:= ", joint_val)

        # Get TCP Position
        tcp_position = self.client.get_tcp_position()
        print("Robot TCP Position: ", tcp_position)

        # Get TCP Orientation Quaternion
        tcp_orient_quat = self.client.get_tcp_orientation("quat")
        print("Robot Orientation Quaternion:= ", tcp_orient_quat)

        # Get TCP Orientation Euler angle
        tcp_orient_euler = self.client.get_tcp_orientation("euler")
        print("Robot Orientation in Euler:= ", tcp_orient_euler)

    # Set SDK APIs - Circular Trajectory on the Base Plane
    def set_sdk_api(self):
        print("Setting Velocity Fraction")
        self.client.change_speed_fraction(0.5)
        
        # Set home position
        print("Setting Home")
        self.client.set_home()
        time.sleep(2)

        # Get initial TCP position (home position)
        tcp_position = self.client.get_tcp()
        home_x = tcp_position[0]
        home_y = tcp_position[1]
        home_z = tcp_position[2]  # This is the constant Z-value (height of the plane)

        # Define circle parameters
        radius = 0.1  # radius of the circle
        num_points = 100  # number of points on the circle
        duration = 10  # time to complete one circle
        angular_step = 2 * math.pi / num_points  # step size in radians

        # Move to the first point of the circular trajectory
        print("Moving to the first point of the circular trajectory")
        first_point_x = home_x + radius  # First point on the circle (theta = 0)
        first_point_y = home_y
        first_point_z = home_z  # Keep the Z constant
        first_point_goal = [first_point_x, first_point_y, first_point_z]
        
        status = self.client.move_to_pose(first_point_goal)
        print("Move to first point status: ", status)
        time.sleep(2)

        # Generate and follow circular trajectory in the XY plane
        print("Drawing a circular trajectory on the XY plane")
        for i in range(num_points):
            theta = i * angular_step  # current angle
            x = home_x + radius * math.cos(theta)  # parametric X for the circle
            y = home_y + radius * math.sin(theta)  # parametric Y for the circle
            z = home_z  # keep Z constant

            # Update TCP position for the circle
            tcp_position_goal = [x, y, z]
            print(f"Moving to pose: {tcp_position_goal}")

            # Move to the new pose
            status = self.client.move_to_pose(tcp_position_goal)
            print("Move to pose status: ", status)
            time.sleep(duration / num_points)

        # Return to home after completing the circle
        print("Returning to Home Position")
        self.client.set_home()
        time.sleep(2)

        # Close the client
        self.client.close()

if __name__ == "__main__":
    testowl = TestOwlSimClient("arm", "gripper")
