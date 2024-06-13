import random
import math

def calculate_uncertain_cuboid_statistics(n_sample, mean_length, mean_width, mean_height, range_length=0, range_width=0, range_height=0):
    '''
    Calculate the mean and standard deviation of the volume of a cuboid with uncertain dimensions.
    :param n_sample: int, The number of samples to take.
    :param mean_length: float, The mean length of the cuboid.
    :param mean_width: float, The mean width of the cuboid.
    :param mean_height: float, The mean height of the cuboid.
    :param range_length: float, The range of the length of the cuboid.
    :param range_width: float, The range of the width of the cuboid.
    :param range_height: float, The range of the height of the cuboid.
    :return: tuple, The mean volume and standard deviation of the volume of the cuboid.
    '''

    # Create a list to store the volumes of the cuboids
    volumes = []

    # Loop over the number of samples
    for i in range(n_sample): 
        # Generate random dimensions for the cuboid
        length = random.uniform(mean_length - range_length / 2, mean_length + range_length / 2)
        width = random.uniform(mean_width - range_width / 2, mean_width + range_width / 2)
        height = random.uniform(mean_height - range_height / 2, mean_height + range_height / 2)

        # Calculate the volume of the cuboid
        volume = get_cuboid_volume(length, width, height)
        # Add the volume to the list
        volumes.append(volume)

    # Calculate the mean and standard deviation of the volumes
    mean_volume = sum(volumes) / n_sample
    total_square = 0
    for volume in volumes:
        total_square = total_square + volume ** 2
    std_volume = math.sqrt((total_square / n_sample) - mean_volume ** 2)

    # Return the mean and standard deviation of the volumes
    return mean_volume, std_volume


def get_cuboid_volume(length, width, height):
    '''
    Calculate the volume of a cuboid.
    :param length: float, The length of the cuboid.
    :param width: float, The width of the cuboid.
    :param height: float, The height of the cuboid.
    :return: float, The volume of the cuboid.
    '''
    return length * width * height

