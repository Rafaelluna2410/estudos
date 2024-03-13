'''

# 1 multiderivação direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultDerivada(Base1, Base2, Base3):
    pass


# 2 multiderivação indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base3):
    pass

class MultDerivada(Base3):
    pass

No final, a que herda sempre vai herdar tudo independente da forma
'''




