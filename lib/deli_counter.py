katz_deli = []
def line(katz_deli):
    
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
    # position = 1
        for i in range(len(katz_deli)):
            line_message +=  f' {i + 1}. {katz_deli[i]}'
        # position += 1
    
        print (line_message)
    
def take_a_number(katz_deli, customer_name):
    katz_deli.append(customer_name)
    position = len(katz_deli)
    print(f"Welcome, {customer_name}. You are number {position} in line.")
    

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]
    