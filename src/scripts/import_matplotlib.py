import matplotlib.pyplot as plt
import numpy as np

# Function to create a rotated square with a specified rotation
def rotated_square(center_x, center_y, side_length, angle_deg):
    half_side = side_length / 2
    angle_rad = np.radians(angle_deg)

    # Define corners for a square centered at the origin
    corners = [
        (-half_side, -half_side),
        (-half_side, half_side),
        (half_side, half_side),
        (half_side, -half_side),
        (-half_side, -half_side)  # Close the square
    ]

    # Rotate each corner and translate to the center
    rotated_corners = []
    for x, y in corners:
        rotated_x = x * np.cos(angle_rad) - y * np.sin(angle_rad)
        rotated_y = x * np.sin(angle_rad) + y * np.cos(angle_rad)
        rotated_corners.append((center_x + rotated_x, center_y + rotated_y))

    return rotated_corners

# Parameters for the squares
center_x = 0.623  # Center x-coordinate
center_y = 0.0589  # Center y-coordinate
initial_side_length = 0.06  # Side length of the first square (6 cm)
angles = [45, 0, 45, 0]  # Rotation angles for each square

# Set up the plot
plt.figure(figsize=(8, 8))
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)

# Plot each square
side_length = initial_side_length
for i, angle in enumerate(angles):
    # Get the rotated square's corners
    square_corners = rotated_square(center_x, center_y, side_length, angle)
    
    # Extract x and y coordinates for plotting
    x_coords, y_coords = zip(*square_corners)
    
    # Plot the square
    plt.plot(x_coords, y_coords, label=f'Square {i+1} (Angle {angle}°)', marker='o')

    # Increase side length for the next square
    side_length *= np.sqrt(2)

# Set plot labels and legend
plt.xlabel('X Coordinate (m)')
plt.ylabel('Y Coordinate (m)')
plt.title('Path of Four Squares with Alternating Rotations')
plt.legend()
plt.axis('equal')
plt.grid(True)

# Show the plot
plt.show()
