import os
import zipfile
import sys

def check_files(folder, required_files):
    """
    Checks whether all required files are present in the specified folder.

    Parameters:
    - folder (str): The name of the folder to check.
    - required_files (list): A list of required file names.

    Returns:
    - missing_files (list): A list of missing files. Empty if all files are present.
    """
    missing_files = []
    for file in required_files:
        file_path = os.path.join(folder, file)
        if not os.path.isfile(file_path):
            missing_files.append(file)
    return missing_files

def create_zip(zip_name, folders):
    """
    Creates a zip archive containing the specified folders.

    Parameters:
    - zip_name (str): The name of the zip file to create.
    - folders (list): A list of folder names to include in the zip.
    """
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in folders:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Add file to zip with relative path
                    zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(folder)))
    print(f"All required files are present. Created '{zip_name}' successfully.")

def main():
    # Define the required files for each folder
    required_files = {
        'ex1': [
            'jacobian_examples.py',
            'sample_ground_truth.mat',
            'sample_velocities.py',
            'robot.py'
        ],
        'ex2': [
            'IK_example.py',
            'robot.py'
        ],
        'ex3': [
            'linear-joint_rajectory.py',
            'linear_workspace_trajectory.py',
            'robot.py',
            'verify_linear_joint_trajectory.py',
            'verify_linear_workspace_trajectory.py',
            'visualize_trajectory.py'
        ],
        'ex4': [
            'grav_comp.py'
        ]
    }

    # List to collect all missing files
    all_missing = {}

    # Check each folder for missing files
    for folder, files in required_files.items():
        if not os.path.isdir(folder):
            all_missing[folder] = ['Folder does not exist']
            continue
        missing = check_files(folder, files)
        if missing:
            all_missing[folder] = missing

    # If there are missing files, report them and exit
    if all_missing:
        print("Error: The following required files are missing:")
        for folder, files in all_missing.items():
            print(f"\nFolder '{folder}':")
            for file in files:
                print(f"  - {file}")
        print("\nPlease ensure all required files are present before creating the submission.")
        sys.exit(1)

    # If all files are present, create the zip archive
    zip_name = 'handin.zip'
    folders_to_zip = ['ex1', 'ex2', 'ex3', 'ex4']
    create_zip(zip_name, folders_to_zip)

if __name__ == "__main__":
    main()
