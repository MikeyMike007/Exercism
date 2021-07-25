import random
import string


class Robot:

    # Class attribute - The set robot_names includes all names for all current
    # Robots at a given time. Please note that all Robots have unique names
    robot_names = set()

    def __init__(self):
        """
        Initiate an instance of the class Robot. Set the name of a Robot
        instance.
        """
        self.name = self.generate_robot_name()

    def reset(self):
        """
        Reset a robot name. Give the robot a new name.
        """
        old_name = self.name
        self.name = self.generate_robot_name()
        Robot.robot_names.remove(old_name)

    def generate_robot_name(self):
        """
        Generate a unique robot name. Return the name.
        """
        # Generates a name until its unique among all active robots
        while True:
            candidate_name = self.generate_name()
            if candidate_name not in Robot.robot_names:
                Robot.robot_names.add(candidate_name)
                return candidate_name


    def generate_name(self):
        """
        Generate a candidate of a robot name. Return the candidate name.
        """
        return "".join(
            random.choices(string.ascii_uppercase, k=2)
            + random.choices(string.digits, k=3)
        )
