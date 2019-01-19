# creating histogram

def histogram( list ):
    for n in list:
        output = ''
        times = n
        while (times > 0):
            output += '(@_@)'
            times = times - 1
        print(output)


histogram([2, 3, 6, 5, 5, 0, 6])
