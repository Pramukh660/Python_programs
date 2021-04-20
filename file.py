print('Enter the names of members of your family')
a = input()
b = input()
c = input()
d = input()
def family():
    for names in range(1, 5):
        print(str(names) + '. ', end="")
        if names == 1:
            print(a)
        elif names == 2:
            print(b)
        elif names == 3:
            print(c)
        elif names == 4:
            print(d)

family()