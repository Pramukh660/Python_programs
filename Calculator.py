print('Welcome to a simple calculator.\nTo find : ')

calculator = ["> Sum enter '+'","> Difference enter '-'","> Product enter '*'","> Quotient and Remainder enter '/'"]
for x in calculator:
    print(x)
print()
print('Please enter any one of the four \nsymbols mentioned above and press enter\n')

while True :
    q = input()

    if q == '+':
        print('To find the sum of two number')
        def add():
            a = input('Enter the first number: ')
            b = input('Enter the second number: ')
            sum = int(a)+int(b)
            print('The sum of '+str(a)+' and '+str(b)+' is: ' + str(sum))
        add()
        print("\n*******************************************************\n")

    elif q == '-':
        print('To find difference of two numbers')
        def difference():
            c = input('Enter the first number: ')
            d = input('Enter the second number: ')
            diff = int(c)-int(d)
            print('The difference of '+str(c)+' and '+str(d)+' is: ' + str(diff))
        difference()
        print("\n*******************************************************\n")

    elif q == '*':
        print('To multiply two numbers')        
        def mul():
            #Multiply two numbers 
            c = input('Enter the first number: ')
            d = input('Enter the second number: ')   
            mul = int(c) * int(d)
            print('the product of '+str(c)+' and '+ str(d)+ ' is '+ str(mul))
        mul()
        print("\n*******************************************************\n")

    elif q == '/':
        print('To divide two numbers')
        def div(): #Divide two numbers
            e = float(input('Enter the numerator: '))
            f = float(input('Enter the denominator: '))
            try:
                quotient = float(e) / float(f)
                remain = float(e) % float(f) 
                print('Quotient is: '+ str(quotient))
                print('Remainder is: '+ str(remain))  
            except ZeroDivisionError:
                print('Cannot divide a number by zero !!')
                print('PLease enter a valid denominator\n')
                div() 
            return quotient, remain
        div()
        print("\n*******************************************************\n")

    else :
        print('Please do not enter any other keys')
        print("\n*******************************************************\n")
        continue