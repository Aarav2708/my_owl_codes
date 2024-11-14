from owl_client import OwlClient, Pose, TrajectoryPlanMode
import time
import numpy as np

client = OwlClient("10.42.0.54")
toolSpeed = 10  # Set an appropriate tool speed for the movement

# Wait for the robot to be available
while not client.is_running():
    time.sleep(0.2)

# Define a square trajectory in Cartesian space
def square_trajectory(center_x, center_y, center_z, side_length):
    half_side = side_length / 2
    waypoints = []

    # Define the four corners of the square
    corners = [
        (center_x - half_side, center_y - half_side),
        (center_x - half_side, center_y + half_side),
        (center_x + half_side, center_y + half_side),
        (center_x + half_side, center_y - half_side),
        (center_x - half_side, center_y - half_side)  # Return to starting point
    ]

    # Create Pose waypoints for each corner
    for i, (x, y) in enumerate(corners):
        waypoint = Pose()
        waypoint.x = x
        waypoint.y = y
        waypoint.z = center_z

        # Set fixed orientation for each waypoint
        waypoint.rx = np.pi  # Replace with desired roll in radians
        waypoint.ry = 0.0  # Replace with desired pitch in radians
        waypoint.rz = 0.0  # Replace with desired yaw in radians

        waypoints.append(waypoint)
        print(f"Waypoint {i}: x={waypoint.x}, y={waypoint.y}, z={waypoint.z}, rx={waypoint.rx}, ry={waypoint.ry}, rz={waypoint.rz}")

    return waypoints

# Generate the trajectory waypoints for a square path
center_x = 0.623  # Center x-coordinate
center_y = 0.0589  # Center y-coordinate
center_z = 0.393  # Constant z-coordinate
side_length = 1.0  # Side length of the square
waypoints = square_trajectory(center_x, center_y, center_z, side_length)

# Execute each waypoint in Cartesian space
for waypoint in waypoints:
    client.move_to_pose(waypoint, toolSpeed, wait=True, relative=False, moveType=TrajectoryPlanMode.STRAIGHT)
    time.sleep(0.1)  # Adjust delay for smoother movement if needed

print("============ Task Complete")
