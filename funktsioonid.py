
def foo():
    print("see on funktsioon")

for i in range(2):
    foo()
def bar():
    tekst = "return niisama"
    tekst2 = "ei tagasta midagi"
    return

print(bar())

def far():
    print("See on esimene")
    return
    print("See on teine")
    
far()


def car():
    #return saab olla muutuja
    text = "tagastab selle"
    return text

def lar():
    #return saab olla konstant
    return "text"

print(lar())


def parameter_example(number: int, text: str):
    print(number, end = " ")
    print(text)
    pass

parameter_example(5, "see on argument")
parameter_example(number = 6, text = "see on konkreetne")

def comment_example(parameter: int, teine: str):
    """
    Take params and returns.
    
    This function is an example of commenting your code.
    
    :param parameter: example of an integer
    :param teine: example of a string
    :return: parameter and string tuple
    """
    print(parameter, teine)
    return (parameter, teine)

comment_example(10, "testing")