from owl_client import OwlClient, Joint
import time
import math

client = OwlClient("10.42.0.54")
jointSpeed = 50  # degrees/sec

# Wait for robot to be available
while not client.is_running():
    time.sleep(0.2)

# Define the zero configuration for the robot
zero_position = Joint()
zero_position.Base = 0.0
zero_position.Shoulder = 0.0
zero_position.Elbow = 0.0
zero_position.Wrist1 = 0.0
zero_position.Wrist2 = 0.0
zero_position.Wrist3 = 0.0

# Move robot to zero configuration initially
client.move_to_joint(zero_position, jointSpeed)
time.sleep(1)

# Define the circular trajectory function
def circular_trajectory(center_x, center_y, center_z, radius, steps=72):
    waypoints = []
    angle_step = 2 * math.pi / steps

    # Generate waypoints around the circle in the x-y plane
    for i in range(steps + 1):
        angle = i * angle_step

        # Set joint positions for circular motion in x-y plane
        waypoint = Joint()
        waypoint.Base = center_x + radius * math.cos(angle)
        waypoint.Shoulder = center_y + radius * math.sin(angle)
        waypoint.Elbow = center_z  # Keep z constant

        waypoints.append(waypoint)

    return waypoints

# Generate a circular trajectory with given parameters
center_x = 0.0  # Replace with center x-coordinate
center_y = 0.0  # Replace with center y-coordinate
center_z = -1.57  # Replace with center z-coordinate (constant height)
radius = 0.1  # Replace with desired radius
waypoints = circular_trajectory(center_x, center_y, center_z, radius)

# Execute the trajectory
for waypoint in waypoints:
    client.move_to_joint(waypoint, jointSpeed)
    time.sleep(0.1)  # Adjust delay for smoother movement

# Return to zero position after the trajectory
client.move_to_joint(zero_position, jointSpeed)
print("============ Task Complete")
