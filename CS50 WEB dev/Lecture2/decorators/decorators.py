# function을 입력받아 다른 function으로 출력
# functional programming paradigm

def announce(f): # announce 함수는, f를 입력받아
    def wrapper(): # local 함수인 wrapper를 만들고
        print("about to run the function...")
        f()
        print('done with the function')
    return wrapper # wrapper함수를 return

@announce # @ : add decorator
def hello():
    print("hello, world!")

hello()
