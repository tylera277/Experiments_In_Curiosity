# Words


def resting_length_initialize(resting_length, number_of_springs, standard_length):

    #three_quarteth_spring = int(3.0*number_of_springs/4.0)
    halfeth_spring = int(number_of_springs / 2.0)
    counter = 1

    for spring in range(halfeth_spring, number_of_springs, 1):
        resting_length[spring] = ((-2*standard_length) / number_of_springs) * spring + (2 * standard_length) 
        #print("BEep: ", resting_length[spring])
    return resting_length
