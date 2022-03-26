


"""""
The program is trying to determine which paymen option is better (more money).
First option is 100 dollars per day for 10 days. The secon doption is 1 dollars  a day with it being doubled each day for 10 days.
There will be two functions to calculate the pay rate.
function1 will calculate the amount for the first option, function 2 will calulate the amount for the second

function1 will output 100 * 10 days.
function2 will loop 10 times, with each time, doubling the amount and add the amount to the total.

if the amount is equal, we output to the user "Option 1 and option 2 are the same"
if the option 1 is better, we output to the user "Option 1 is better"
if the option 2 is better, we output to the user "Option 2 is better"
"""""

"""

# option1
    return 100 * 10

# option2
    amount = 1
    list1 = []
    loop 10 times
        add amount to list1
        amount *= 2
    sum = sum of all items in loop
    retrun sum
# main
    var1 = option1
    var2 = option1

    if car1 = var2
         we output to the user "Option 1 and Option 2 pays the same"
    if var1 < var2 
        "Option 2 is better"
    else
        "Option 1 is better"

main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    print("list1", list1)
    total = sum(list1)
    return total 

def main():
    answer = ""
    var1 = option1() 
    var2 = option2() 
    print("from main: var1", var1, "var2", var2)
    if var1 == var2:
        answer =  "Option 1 and Option 2 pays the same"
    elif var1 < var2: 
       answer = "Option 2 is better"
    else:
      answer = "Option 1 is better"
    print(answer)

main()