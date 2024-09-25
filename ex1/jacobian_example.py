import numpy as np
from robot import Robot

# Create the 10R robot
link_lengths_10R = np.ones(10) * 5
link_masses_10R = np.ones(10)
joint_masses_10R = np.ones(10)
robot10R = Robot(
    link_lengths=link_lengths_10R,
    link_masses=link_masses_10R,
    joint_masses=joint_masses_10R,
    end_effector_mass=1
)

# Define the joint angles
thetas_10R = np.array([0, 0.1, 0.2, 0.3, 0.4, 0, -0.1, -0.2, -0.3, -0.4])

# --------------- BEGIN STUDENT SECTION (Compute Joint Torques) ---------------
# TODO: Compute the Jacobian at the end effector and calculate the joint torques

# Hints:
# - Use the jacobians method to compute the Jacobian matrix.
# - Define the wrench as specified.
# - Compute Tau as the transpose of the Jacobian times the wrench.

# Your code starts here

...

# Your code ends here
# --------------- END STUDENT SECTION ------------------------------------------

# Print the resulting joint torques
print("\nJoint Torques to apply the given wrench at the end effector:")
print(Tau)
