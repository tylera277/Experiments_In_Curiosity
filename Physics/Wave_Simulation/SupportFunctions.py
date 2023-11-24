# Words


def resting_length_initialize(resting_length, number_of_springs, standard_length):

    three_quarters = int(3.0*number_of_springs / 4.0)
    running_fraction = (number_of_springs - three_quarters)

    for spring in range(three_quarters, number_of_springs):
        resting_length[spring] = spring * ((4 * standard_length)/number_of_springs)

    return resting_length