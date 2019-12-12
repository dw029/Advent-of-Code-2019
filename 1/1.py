import math

f = open('input.txt', 'r').readlines()

def calcFuel(mass):
        if mass <= 6:
                return 0
        return (math.floor(mass/3) - 2) + calcFuel(math.floor(mass/3) - 2)


accumulator = 0
for line in f:
	accumulator += calcFuel(int(line))

print(accumulator)
