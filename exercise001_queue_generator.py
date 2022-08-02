# credit: Nado Coding's "Python Free Course (Basic)" YouTube
# secnario: you own a coffee shop. we need to create a queue generator. 
#           everyday, you can only serve 10 coffes. 
#           let's create a queue generator. 

#1) My codes:
class SoldOutError(Exception):
    pass

coffee = 10
guest = 1
order = 0

try:
    while coffee >0 or coffee > order:
        order = int(input("How many coffee to order?: "))
        if order < 1 or order > coffee:
            raise ValueError
        elif coffee == order:
            raise SoldOutError
        else:
            print("Queue {}: {} coffee(s) ready"\
                .format(guest, order))
            guest +=1
            coffee -=order
            print("[{} coffees available]" .format(coffee))
except ValueError:
    print("You have entered wrong value")
except SoldOutError:
    print("Sold out!")

# It works OK. But there are several issues.

# Failure Note: 
# a. there are too many or, >, < .. in one code. It is not only unclear but also difficult to manage.
# b. in case of error, program stops asking user to enter the value again. It just stops.
#    this is because I added condition in while, instead of using while True.
#    also, coffee == order clause should be after coffee -= order clause. 

#2) Instructor's codes:

class SoldOutError(Exception):
    pass

coffee = 10
guest = 1

while(True): # thanks to this, codes will still run in case of errors.
    try:
        print("[Left coffee: {}]" .format(coffee))
        order =int(input("How many coffee do you want: "))
        if order > coffee: # let's simplify by dividing scenario.
            print("Not enought coffee")
        elif order <= 0:
            raise ValueError
        else:
            print("Queue {}: {} coffee(s) ready"\
                    .format(guest, order))
            guest += 1
            coffee -= order
        if coffee == 0:
            raise SoldOutError
    except ValueError:
        print("Worng number entered")
    except SoldOutError:
        print("Sold Out!")
        break
    
