def euclides (a,b):
    if (a%b == 0): return b
    return euclides(b,a%b)

print(euclides (102, 3))