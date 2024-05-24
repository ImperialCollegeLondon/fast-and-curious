from scipy.stats import uniform

def calculate_uncertain_cuboid_statistics(n_sample, length, width, height, range_length=0, range_width=0, range_height=0):
    if sum(map(bool, [range_length, range_width, range_height])) == 0:
        return get_cuboid_volume(length, width, height), 0       

    length_distribution = uniform(loc=length - range_length / 2, scale=range_length)
    width_distribution = uniform(loc=width - range_width / 2, scale=range_width)
    height_distribution = uniform(loc=height - range_height / 2, scale=range_height)

    lengths = length_distribution.rvs(n_sample)
    widths = width_distribution.rvs(n_sample)
    heights = height_distribution.rvs(n_sample)

    volumes = get_cuboid_volume(lengths, widths, heights)

    mean_volume = volumes.mean()
    std_volume = volumes.std()

    return mean_volume, std_volume


def get_cuboid_volume(length, width, height):
    return length * width * height

