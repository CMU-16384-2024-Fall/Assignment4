import numpy as np
import math
from frankapy import FrankaArm

# Constants
g = 9.81  # gravitational acceleration (m/s^2)

# Masses and lengths for the 2D simplified model (in meters and kg)
link_masses = {
    5: 1.225946,  # Mass of link 5
    6: 1.666555   # Mass of link 6
}

# Lengths of the links (in meters)
link_lengths = {
    5: 0.384,  # Length of link 5
    6: 0.1     # Length of link 6 to its CoM
}

# Function to compute the Jacobian for the RR arm
def compute_jacobian(theta5, theta6):
    """
    TODO: Implement the Jacobian matrix for the RR arm based on joint angles theta5 and theta6.

    Parameters:
    - theta5 (float): Angle of joint 5 in radians.
    - theta6 (float): Angle of joint 6 in radians.

    Returns:
    - J (np.ndarray): 2x2 Jacobian matrix.
    """
    # --------------- BEGIN STUDENT SECTION ----------------------------------
    # Replace the following lines with your implementation
    raise NotImplementedError
    # --------------- END STUDENT SECTION ------------------------------------

    return J

# Function to compute the gravitational torques for joint 5 and 6 using the Jacobian
def compute_gravitational_torques(joint_5_angle, joint_6_angle):
    """
    TODO: Implement the computation of gravitational torques using the Jacobian.

    Parameters:
    - joint_5_angle (float): Current angle of joint 5 in radians.
    - joint_6_angle (float): Current angle of joint 6 in radians.

    Returns:
    - torques (np.ndarray): Array containing torques for joints 5 and 6.
    """
    # --------------- BEGIN STUDENT SECTION ----------------------------------
    # Replace the following lines with your implementation
    raise NotImplementedError
    # --------------- END STUDENT SECTION ------------------------------------

    return torques

if __name__ == "__main__":
    fa = FrankaArm()

    # Reset the joints to a known configuration
    fa.reset_joints()

    # Get the current joint angles after reset
    joint_angles = fa.get_joints()

    # Start a sweep of 30-degree increments until +90 degrees from the reset position
    initial_angle_5 = joint_angles[4]  # Joint 5 (index 4)
    initial_angle_6 = joint_angles[5]  # Joint 6 (index 5)

    # Define tolerance
    torque_tolerance = [2.47, 1.74, 0.64]  # Nm

    print("Gravity Compensation Verification\n")
    print("-------------------------------------------------------------")
    print(f"{'Joint 6 Angle (deg)':<20}{'Calculated Torque (Nm)':<25}{'Actual Torque (Nm)':<20}{'Difference (Nm)':<15}{'Result'}")
    print("-------------------------------------------------------------")

    # Loop to increment the angle of joint 6 by 30 degrees until 90 degrees
    for i in range(3):
        # Increment joint 6 by 30 degrees
        joint_angles[5] = initial_angle_6 + math.radians(30 * (i + 1))

        # Move the arm to the new joint angles
        fa.goto_joints(joint_angles)

        # Get the updated joint angles
        joint_5_angle = joint_angles[4]
        joint_6_angle = joint_angles[5]

        # Calculate the gravitational torques using the Jacobian
        calculated_torques = compute_gravitational_torques(joint_5_angle, joint_6_angle)

        # Get the actual torques from the API
        actual_torques = fa.get_joint_torques()

        # Calculate difference for joint 6
        torque_difference = abs(calculated_torques[1] - actual_torques[5])

        # Determine pass or fail
        result = "PASS" if torque_difference <= torque_tolerance[i] else "FAIL"

        # Print the results for the 6th joint
        print(f"{math.degrees(joint_6_angle):<20.2f}{calculated_torques[1]:<25.2f}{actual_torques[5]:<20.2f}{torque_difference:<15.2f}{result}")

    print("-------------------------------------------------------------")
    print("\nVerification Completed.")
