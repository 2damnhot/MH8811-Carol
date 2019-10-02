def hello_w():
    print('Hello, world!')

def ask_n():
    ask_name = input('What is your name?')
    print('Hello,',ask_name + '!')

def ask_temp():
    question = input('What temperature do you want in Celsius?')
    Celsius = float(question)
    Fahrenheit = Celsius*1.8+32
    print(Fahrenheit)
    
#what else can make a function? count down from 5 to 1  
def count_down():
    n=5
    while n>0:
        print(n)
        n=n-1
    print('you died!')

"------------------------------------------------------------------------------------------"

while True:
    print('Hello Brave Warroior you made it which door do u want to choose?')
    print('1: greeting the world\n2: greeting you\n3: convert temperature from Celsius to Fahrenheit')
    line = input('>')
    if line == '1':
        hello_w()
        ask_stop = input('Do u wanna to choose again?Yes or No?')
        if ask_stop == 'Yes':
            continue  
        if ask_stop =='No':
            break
        else:
            print('Wrong Choice!')
            count_down()
    if line == '2':
        ask_n()
        ask_stop = input('Do u wanna to choose again?Yes or No?')
        if ask_stop == 'No':
            break
        elif ask_stop == 'Yes':
            continue
        else:
            print('Wrong Choice!')
            count_down()
    if line == '3':
        ask_temp()
        ask_stop = input('Do u wanna to choose again?Yes or No?')
        if ask_stop == 'Yes':
            continue
        if ask_stop == 'No':
            break
        else:
            print('Wrong Choice!')
            count_down()
    else:
        print("There is no other doors. Please choose 1, 2 or 3")
print('Ok Bye!')
