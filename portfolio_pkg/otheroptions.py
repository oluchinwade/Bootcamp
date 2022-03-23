def gender(gen):
    male = "Male" or "1"
    female = "Female" or "2"
    sex = input("1. Male 2. Female")
    if sex == male.lower():
        sex = "boy"
    else:
        sex == female.lower()
        gen = "girl"
    ''
def play_again():
    yes = "Yes" or "YES" or "yes" or "Y" or "y" or "1"
    no = "No" or "NO" or "no" or "N" or "n" or "2"
    yes_no = input("Would you like to try again? Yes/No")
    if yes_no == yes:
        print("Let's go again!")
    else:
        yes_no == no
        print("Thank you for playing! BYE!!")
        return