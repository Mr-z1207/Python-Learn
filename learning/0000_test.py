L = ['adam', 'LISA', 'barT']


def Slower(x):
    return x[0].upper() + x[1:].lower()


newL = map(Slower, L)
print(list(newL))


str = "123abcrunoob3111222212121112"
print(str.strip('12'))


def sayHi():
    print('Hi')


def callSayHi(fn):
    print('Call')
    return fn()


callSayHi(sayHi)

p = [('username', 'email'), ('password', 'passwd'), ('entry', 'mweibo')]
print(type(p))
