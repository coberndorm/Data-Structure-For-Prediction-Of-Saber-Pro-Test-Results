
def conjuntos(base, s):
    if (len(s) == 0):
        print (base)
    else:
        conjuntos(base + s[0], s [1:])
        conjuntos (base, s [1:])

conjuntos("", "abcd")
