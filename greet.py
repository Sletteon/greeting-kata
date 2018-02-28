#!usr/env python3

def goodmorning(name):
    print('Good mornin, {}.'.format(name))

def holidayGreeting(name, holiday, appropiateGreeting):
    return '{} {}, {}!'.format(appropiateGreeting, holiday, name)

def fancyFrame(functionOutput):
    print('*********************************************************************************')
    print(functionOutput)
    print('*********************************************************************************')

def Main():

    holidayGreetingParams = ('misi', 'Eastern', 'Happy')
    fancyFrame(holidayGreeting(*holidayGreetingParams))
    


if __name__ == '__main__':
    Main()
