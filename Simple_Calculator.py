user_wants_to_calculate_again = True

print("1. addition")
print("2. subtraction")
print("1. multiplication")
print("1. division")

while user_wants_to_calculate_again:
    
    num1 = float(input("Enter your first number : "))
    num2 = float(input("Enter your second number : "))

    choice =input("\nEnter your choice(1/2/3/4) :")
    if choice in ('1','2','3','4'):

        if choice == '1':
            print(num1 , "+", num2, "=" , num1+num2)

        elif choice == '2':
            print(num1 , "-", num2, "=" , num1-num2)    

        if choice == '3':
            print(num1 , "*", num2, "=" , num1*num2)    

        if choice == '4':
            print(num1 , "/", num2, "=" , num1/num2)    

    else:
        print("Invalid choice")
    play_again =input("\n Do you want to calculate again?(yes/no): ").lower()
    if play_again != 'yes':
        user_wants_to_calculate_again = False            