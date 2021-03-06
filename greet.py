#!usr/env python3

def goodmorning(name):
    return 'Good mornin, {}.'.format(name)

def holidayGreeting(name, holiday, appropiateGreeting):
    if name == "" or name == None:
        name = "my Friend"
    return '{} {}, {}!'.format(appropiateGreeting, holiday, name)

def frame(framechar):
    for i in range(81):
        print(framechar, end='')

def fancyFrame(functionOutput, framechar):
    frame(framechar) 
    print('')
    frame(framechar) 
    print('')
    print(framechar + framechar + functionOutput.center(77) + framechar + framechar)
    frame(framechar) 
    print('')
    frame(framechar) 
    print('\n')

def Main():

    _FRAMECHAR = '#'

    holidayGreetingParams = ('', 'Eastern', 'Happy')
    fancyFrame(holidayGreeting(*holidayGreetingParams), _FRAMECHAR)
    fancyFrame(goodmorning('misi'), _FRAMECHAR)
    
    


if __name__ == '__main__':
    Main()
