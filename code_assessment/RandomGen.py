import random
import numpy as np
# How many times of simulation we want to run
times = 100


class RandomGen(object):

# The constructor method for a class
    def __init__(self):
        self._random_nums = set([])
        self._probabilities = []

# Generate 5 random numbers without duplication
    def generate_random_nums(self):
        for i in range(0, 5):
            randi = random.randint(-1000, 1000)
            self._random_nums.add(randi)
            list1 = list(self._random_nums)
            list1.sort()
        return list1

# Generate 5 random >=0 probabilities, the sum must be 1
    def generate_probabilities(self):
        n = 5
        list2 = []
        values = [0.0, 1.0] + [round(random.random(), 4) for _ in range(n - 1)]
        values.sort()
        _probabilities = [values[i + 1] - values[i] for i in range(n)]
        for i in _probabilities:
            if i != 0:
                list2.append(i)
        return list2

# print out simulated probabilities
    def next_num(self):
        list3 = []
        for i in range(0, times):
            randc = np.random.choice(_random_nums_final, p=_probabilities_final)
            list3.append(randc)
            unique_list = np.unique(list3)

        for i in _random_nums_final:
            if i in unique_list:
                print('%d: %d times, probability is: %.4f.' % (i, list3.count(i), round(list3.count(i) / times, 4)))
            else:
                print('%d: 0 times.' % i)


if __name__ == '__main__':
    call_class = RandomGen()
    _random_nums_final = call_class.generate_random_nums()
    _probabilities_final = call_class.generate_probabilities()
    print('If we run the process %d times:' % times, '\n')
    print('the random numbers are: %s' % _random_nums_final)
    print('the random probabilities are: %s' % _probabilities_final)
    call_class.next_num()
    print('\n')

    _random_nums_final = [-1, 0, 1, 2, 3]
    _probabilities_final = [0.01, 0.3, 0.58, 0.1, 0.01]
    print('If we run the process %d times on a given list of number and a given list of probabilities:' % times, '\n')
    print('the given numbers are: %s' % _random_nums_final)
    print('the given probabilities are: %s' % _probabilities_final)
    call_class.next_num()