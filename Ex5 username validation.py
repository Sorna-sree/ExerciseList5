''' Validate user input for username. Conditions - username length 
should be between 4 and 8, should not start with a number, 
should not start or end with '_', and only alphabets, numbers and
'_' is allowed.When the user enters an username, you should print all
possible errors in the username.
For eg - if input is 1b%  - the output should be 'Username
length should be >4 <8, no numeric at the start and no special chars 
allowed' '''

user_name=input("Enter the username: ")

if(len(user_name)>=4 and len(user_name)<=8 ) and user_name.isalpha() and user_name[0]!='_' and user_name[-1]!='_':
    print("valide username")
if(len(user_name)<=4 and len(user_name)>=8):
    print("user name length should be between 4 and 8")
if(user_name.isalpha()==False):
    print("username should not startwith number and spcial character should use only alphabets")
if(user_name[0]=='_' or user_name[-1]=='_'):
    print("should not start or end with '_' ")
    
 
