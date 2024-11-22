from owl_client import OwlClient, Pose, TrajectoryPlanMode
import time
import numpy as np

client = OwlClient("10.42.0.54")
toolSpeed = 35  # Set an appropriate tool speed for the movement

# Wait for the robot to be available
while not client.is_running():
    time.sleep(0.2)

# Function to create a square with a specified rotation
def rotated_square(center_x, center_y, center_z, side_length, angle_deg):
    half_side = side_length / 2
    angle_rad = np.radians(angle_deg)
    waypoints = []

    # Define corners for a square centered at the origin, then apply rotation
    corners = [
        (-half_side, -half_side),
        (-half_side, half_side),
        (half_side, half_side),
        (half_side, -half_side),
        (-half_side, -half_side)  # Close the square
    ]

    # Rotate each corner and translate to the center
    for i, (x, y) in enumerate(corners):
        rotated_x = x * np.cos(angle_rad) - y * np.sin(angle_rad)
        rotated_y = x * np.sin(angle_rad) + y * np.cos(angle_rad)

        waypoint = Pose()
        waypoint.x = center_x + rotated_x
        waypoint.y = center_y + rotated_y
        waypoint.z = center_z

        # Set fixed orientation for each waypoint
        waypoint.rx = np.pi  # Fixed roll
        waypoint.ry = 0.0    # Fixed pitch
        waypoint.rz = angle_rad  # Yaw angle for this square

        waypoints.append(waypoint)
        print(f"Waypoint {i}: x={waypoint.x}, y={waypoint.y}, z={waypoint.z}, rx={waypoint.rx}, ry={waypoint.ry}, rz={waypoint.rz}")

    return waypoints

# Parameters for the squares
center_x = 0.623  # Center x-coordinate
center_y = 0.0589  # Center y-coordinate
center_z = 0.42  # Constant z-coordinate
initial_side_length = 0.06  # Side length of the first square (6 cm)

# Generate waypoints for each square with alternating rotation and increasing side length
angles = [45, 0, 45, 0]  # Rotation angles for each square
side_length = initial_side_length

# Execute each square individually
for angle in angles:
    # Generate waypoints for the current square
    waypoints = rotated_square(center_x, center_y, center_z, side_length, angle)
    
    # Move to the starting point of the current square without connecting to the last point
    client.move_to_pose(waypoints[0], toolSpeed, wait=True, relative=False, moveType=TrajectoryPlanMode.STRAIGHT)
    time.sleep(0.5)  # Pause before starting the square to avoid connecting paths

    # Execute each waypoint in the current square
    for waypoint in waypoints:
        client.move_to_pose(waypoint, toolSpeed, wait=True, relative=False, moveType=TrajectoryPlanMode.STRAIGHT)
        time.sleep(0.1)  # Adjust delay for smoother movement if needed

    # Increase side length for the next square
    side_length *= np.sqrt(2)

print("============ Task Complete")
