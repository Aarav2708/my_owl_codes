from owl_client import OwlClient, Pose,TrajectoryPlanMode
import time
import math
import numpy as np


client = OwlClient("10.42.0.54")
toolSpeed = 0.1  # Set an appropriate tool speed for the movement
      
# Wait for the robot to be available
while not client.is_running():
    time.sleep(0.2)

# Define a circular trajectory in Cartesian space
def circular_trajectory(center_x, center_y, center_z, radius, steps=72):
    waypoints = []
    angle_step = 2 * math.pi / steps

    # Generate waypoints around the circle in the x-y plane
    for i in range(steps + 1):
        angle = i * angle_step
        waypoint = Pose()
        
        # Position for circular motion in x-y plane, z remains constant
        waypoint.x = center_x + radius * math.cos(angle)
        waypoint.y = center_y + radius * math.sin(angle)
        waypoint.z = center_z

        # Orientation (rx, ry, rz) can be set as needed
        waypoint.rx = np.pi  # Replace with desired roll in radians
        waypoint.ry = 0.0  # Replace with desired pitch in radians
        waypoint.rz = 0.0  # Replace with desired yaw in radians

        waypoints.append(waypoint)

    return waypoints

# Generate the trajectory waypoints
center_x = 0.623  # Center x-coordinate
center_y = 0.0589  # Center y-coordinate
center_z = 0.393  # Constant z-coordinate
radius = 0.1  # Radius of the circular path
waypoints = circular_trajectory(center_x, center_y, center_z, radius)

# Execute each waypoint in Cartesian space
for waypoint in waypoints:
    client.move_to_pose(waypoint, toolSpeed, wait=True, relative=False, moveType=TrajectoryPlanMode.STRAIGHT)
    time.sleep(0.1)  # Adjust delay for smoother movement if needed

print("============ Task Complete")
