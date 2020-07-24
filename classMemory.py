class Class1:
    name = ''
    class1List = []

class Class2:
    name = ''

    def __init__(self):
        self.class2List = []


sam = Class1()
yuchi = Class1()
gavin = Class2()
sasha = Class2()

sam.name = 'Smaran GK'
yuchi.name = 'Yuchen Y'
print(sam.name)
print(yuchi.name)

sam.class1List.append('Math')
print(sam.name, ' is in', sam.class1List)
print(yuchi.name, ' is in', yuchi.class1List)
print('This is weird, I never added math to yuchi!')
print(Class1.name)

gavin.name = 'Gavin Z'
sasha.name = 'Sasha A'
sasha.class2List.append('Psych')
print(sasha.name, ' is in', sasha.class2List)
print(gavin.name, ' is in', gavin.class2List)