import random

colors =["Orange","White","Pink"]

results=random.choices(colors, weights=[18,12,5], k=10)

print(results)