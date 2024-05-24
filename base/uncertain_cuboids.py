import random
import math

def calculate_uncertain_cuboid_statistics(n_sample, mean_length, mean_width, mean_height, range_length=0, range_width=0, range_height=0):
    volumes = []

    for i in range(n_sample):
        length = random.uniform(mean_length - range_length / 2, mean_length + range_length / 2)
        width = random.uniform(mean_width - range_width / 2, mean_width + range_width / 2)
        height = random.uniform(mean_height - range_height / 2, mean_height + range_height / 2)

        volume = get_cuboid_volume(length, width, height)
        volumes.append(volume)

    mean_volume = sum(volumes) / n_sample
    total_square = 0
    for volume in volumes:
        total_square = total_square + volume ** 2
    std_volume = math.sqrt((total_square / n_sample) - mean_volume ** 2)

    return mean_volume, std_volume


def get_cuboid_volume(length, width, height):
    return length * width * height

