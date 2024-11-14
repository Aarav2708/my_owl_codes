import math

# Define a circular trajectory in Cartesian space
def circular_trajectory(center_x, center_y, center_z, radius, steps=72):
    angle_step = 2 * math.pi / steps

    # Generate and print waypoints around the circle in the x-y plane
    for i in range(steps + 1):
        angle = i * angle_step
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        z = center_z
        rx, ry, rz = 0.0, 0.0, 0.0  # Fixed orientation for this example

        print(f"Waypoint {i}: x={x}, y={y}, z={z}, rx={rx}, ry={ry}, rz={rz}")

# Parameters for the circular path
center_x = 0.0
center_y = 0.0
center_z = 0.5
radius = 0.1

# Generate and print the trajectory waypoints
circular_trajectory(center_x, center_y, center_z, radius)
