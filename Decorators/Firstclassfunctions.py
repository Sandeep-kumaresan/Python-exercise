def shout(text):
    return text.upper()
print(shout("uBuNtU"))

yell=shout
print(yell('KaLi lInUx'))

def whisper(text):
    return text.lower()

def greet(func):
    con=func("""PaSsIng ThIs aRgUmEnT""")
    print(con)
greet(whisper)
greet(shout)

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15=create_adder(15)
print(add_15(10))
