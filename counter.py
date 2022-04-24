from collections import Counter

l=[1,2,3,4,1,2,3,1,2,1]
print(Counter(l))

estudiantes= "carlos claudio brenda flor nicolas flor carlos"
print(Counter(estudiantes))

print(Counter(estudiantes.split()))