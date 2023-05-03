#basically random numbers generators are used to generate on the base of soemthing like computer time's clock. The dependency on anything
# are called seed. Now we can change the seed. We can change the seed by giving our own seed some values.
import random
random.seed(13413)
random_int=random.randint(1,100)
print(random_int)
random_float=random.random()
print(random_float)