[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/EZDP9Yh_)

# Rangoli Drawing with Orangewood Robot using Position Control

This project demonstrates the use of an Orangewood robot to draw a rangoli pattern on a flat surface using position control, bypassing traditional trajectory control. The project leverages ROS and the MoveIt packages for planning and executing the robot's movements, along with the `owl_client` library for direct control. By controlling the robot’s position in precise increments, the design achieves the traditional rangoli pattern effect. This setup allows users to experiment with custom designs and refine position control methods without relying on trajectory planning, offering insights into fine motor control and ROS-based manipulation.

## Key Features

- **Position Control**: Direct position control for drawing without predefined trajectories.
- **MoveIt Integration**: Uses MoveIt for planning and collision checking.
- **Customizable Patterns**: Easily modify patterns to experiment with various rangoli designs.
- **Orangewood Robot Control**: Interfaced with the `owl_client` library for smooth and responsive operation.

For setup instructions, dependencies, and usage, refer to the sections below.


## Installation

1. Follow the steps listed on [Orangewood Sim Stack Repository](https://github.com/orangewood-co/orangewood_sim_stack.git).
2. Navigate to the src folder of the workspace and clone [my_owl_codes repository](https://github.com/Aarav2708/my_owl_codes.git).
3. To connect the Robot to the computer, follow these instructions on [Owl Robot Client](https://owldoc.bitbucket.io/installation.html)


## Setting up Network for the Robot

## Network Setup

The robot has a static IP address assigned, which is `10.42.0.54`, but you can verify it by checking the network settings on the NUC (Settings -> Network -> Wired). A direct connection from the PC to the robot reduces network hardware delay.

1. **Connect the OWL control box** directly to the remote PC with an Ethernet cable.
2. **On the remote PC**, turn off all network devices except the “wired connection” (e.g., turn off Wi-Fi).
3. Open **Network Settings** and create a new Wired connection with the following settings. You may want to name this new connection "OWL" or something similar:
```bash
   - IPv4: Manual
   - Address: 10.42.0.52
   - Netmask: 255.255.255.0
   - Gateway: 10.42.0.1
```
4. Verify the connection from the remote PC with the command:

  ```bash
   ping 10.42.0.54
```
## OWL Client PC

To use the OWL Python client, ensure it is installed. Currently, it can only be installed from the Bitbucket source.

1. Clone the `owl_robot_client` repository on the local PC:

   ```bash
   git clone https://Orangewoodlabs@bitbucket.org/owl-dev/owl_robot_client.git -b main
    ```
2. Install the python library by running following command in cloned directory.
   ```bash
    # Make sure python3 is installed
    $ python3
    Python 3.8.10 (default)
    >>> from owl_client import OwlClient
    >>>
   
   
## Running the simulation
   ```bash
   cd orangewood_ws/sec/my_owl_codes/src/sim_codes/
   python3 waypoinst_sim.py
   
## Running the code
   ```bash
   cd orangewood_ws/src/my_owl_codes/src/hardware_scripts
   python3 hardware_code.py


