squares_set = set()
cubes_set = set()


for i in range(1000):
	squares_set.add(i**2)
	cubes_set.add(i**3)
	
squares_and_cubes_set = squares_set & cubes_set

print(squares_and_cubes_set)