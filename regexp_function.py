import re

# Define a function for validating an Email
def check(Email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern, Email):
        print("valid email address")
    else:
        print("invalid email address")

# Main function
if __name__ == '__main__':

	# Enter the email
	email = input("Enter your email address: ")
    # calling run function
	check(email)

#--------------------------------------------------------------------
	
# Function to check Bangladesh number
def validate_not_mobile(value):
    phone_object= re.compile((r'^\+?(880)?(0|7)\d{9,13}$'))

    if phone_object.search(value):
        print("This is Bangladesh number")
    else:
        print("This not Bangladesh number")

validate_not_mobile(input("Enter your number: "))


#-----------------------------------------------------------------------
# Function to check USA telephone number
def validate_not_mobile(value):
    phone_object= re.compile((r'^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$'))

    if phone_object.search(value):
        print("This is USA telephone number")
    else:
        print("This not USA telephone number")

validate_not_mobile(input("Enter your USA telephone number: "))

#-------------------------------------------------------------------
#Function to check 16 characters password
def validate_not_password(value):
    phone_object= re.compile((r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
))

    if phone_object.search(value):
        print("This is a valid password")
    else:
        print("Invalid password")

validate_not_password(input("Enter your password: "))
