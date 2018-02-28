#!usr/env python3

def goodmorning(name):
    return 'Good mornin, {}.'.format(name)

def holidayGreeting(name, holiday, appropiateGreeting):
    if name == "" or name == None:
        name = "my Friend"
    return '{} {}, {}!'.format(appropiateGreeting, holiday, name)

def fancyFrame(functionOutput):
    for i in range(81):
        print('*', end='')
    print('\n' + functionOutput.center(80))
    for i in range(81):
        print('*', end='')
    print('\n')

def Main():

    holidayGreetingParams = ('', 'Eastern', 'Happy')
    fancyFrame(holidayGreeting(*holidayGreetingParams))
    fancyFrame(goodmorning('misi'))
    
    


if __name__ == '__main__':
    Main()
