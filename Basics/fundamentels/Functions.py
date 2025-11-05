def table():
    user = int(input("Enter The Interger: "))
    for i in range(1,11):
        return(f"{i}x{user}={i*user}")


def math(*args):
    total = 0
    for num in args:
        total += num
    return total


def create_profile(**kwargs):
    print("user profile")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
create_profile(name ='Starwin ',age =22, job='currently no job ' )
    
