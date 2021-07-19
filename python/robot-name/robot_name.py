import random
import string


class Robot:

    # Class attribute - The set robot_names includes all names for all current
    # Robots at a given time. Please note that all Robots have unique names
    robot_names = set(())

    def __init__(self):
        """
        Initiates a Robot with a unique name
        """
        # Name the Robot with a unique name
        self.name = self.generate_robot_name()
        # Save the robot name in the class attribute set robot_names. Just in
        # order to keep track of all the names of the active robots.
        Robot.robot_names.add(self.name)

    def reset(self):
        """
        Resets a robots name and gives it a new unique name
        """
        # Remove the current robot_name from the set robot_names
        Robot.robot_names.remove(self.name)

        # Set a new unique name for the Robot
        self.name = self.generate_robot_name()

        # Add the new unique name for the Robot to the set of robot_names
        Robot.robot_names.add(self.name)

    def generate_robot_name(self):
        """
        Generates a unique name for the robot_names
        """
        test_name = self.generate_name()

        # Generates a name until its unique among all active robots
        for test_name in Robot.robot_names:
            test_name = self.generate_name()

        return test_name

    def generate_name(self):
        """
        Generates a name according to the predefined format
        """
        random.seed()
        name = "".join(
            random.choices(string.ascii_uppercase, k=2)
            + random.choices(string.digits, k=3)
        )
        return name
