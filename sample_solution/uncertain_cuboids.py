from scipy.stats import uniform

def calculate_uncertain_cuboid_statistics(n_sample, length, width, height, range_length=0, range_width=0, range_height=0):
    '''
    Calculate the mean and standard deviation of the volume of a cuboid with uncertain dimensions.
    :param n_sample: int, The number of samples to take.
    :param length: float, The mean length of the cuboid.
    :param width: float, The mean width of the cuboid.
    :param height: float, The mean height of the cuboid.
    :param range_length: float, The range of the length of the cuboid.
    :param range_width: float, The range of the width of the cuboid.
    :param range_height: float, The range of the height of the cuboid.
    :return: tuple, The mean volume and standard deviation of the volume of the cuboid.
    '''

    # If all ranges are 0, the dimensions are certain
    if sum(map(bool, [range_length, range_width, range_height])) == 0:
        # Return the volume of the cuboid and 0 as the standard deviation
        return get_cuboid_volume(length, width, height), 0       

    # Create distributions for the dimensions
    # These are scipy.stats distributions, which can be used to sample values
    length_distribution = uniform(loc=length - range_length / 2, scale=range_length)
    width_distribution = uniform(loc=width - range_width / 2, scale=range_width)
    height_distribution = uniform(loc=height - range_height / 2, scale=range_height)

    # Create arrays of samples from the distributions
    lengths = length_distribution.rvs(n_sample)
    widths = width_distribution.rvs(n_sample)
    heights = height_distribution.rvs(n_sample)

    # Calculate the volumes of the cuboids
    # The function can work on arrays, so we can calculate all volumes at once
    # This is faster than looping over the samples
    volumes = get_cuboid_volume(lengths, widths, heights)

    # Calculate the mean and standard deviation of the volumes
    # There are calculated using the mean and std methods of the numpy array
    mean_volume = volumes.mean()
    std_volume = volumes.std()

    # Return the mean and standard deviation of the volumes
    return mean_volume, std_volume


def get_cuboid_volume(length, width, height):
    '''
    Calculate the volume of a cuboid.
    :param length: float or array, The length of the cuboid.
    :param width: float or array, The width of the cuboid.
    :param height: float or array, The height of the cuboid.
    :return: float or array, The volume of the cuboid.
    '''
    # No changes were made to this relative to the base version
    # If the dimensions are arrays, calculate the volumes element-wise
    return length * width * height

