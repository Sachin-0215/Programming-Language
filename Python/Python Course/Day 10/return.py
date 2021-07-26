# Multiple return values

def format_name(f_name,l_name):
    if f_name=="" or l_name =="":
        return 
    formatted_F_name = (f_name.title())
    formatted_L_name = (l_name.title())
    return (f"{formatted_F_name} {formatted_L_name}")

formatted_string = format_name(input("What is your first name? "),input("What is your last name? "))    

print(formatted_string)
