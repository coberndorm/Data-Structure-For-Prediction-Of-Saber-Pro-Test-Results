
def permutaciones (base, s):
    if (s==""):
        print (base)
    for i in range(len (s)):
        permutaciones(base + s [i], s[0:i]+s[i+1:len(s)])


permutaciones("", "abc")