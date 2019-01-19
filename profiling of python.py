# determine profiling of python programs

import cProfile

def sum():
    print(2+8)


cProfile.run('sum()')
