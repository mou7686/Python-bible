# get user email address
email=input("what is your email address?:").strip()
#slice out user name
user_name=email[:email.index("@")]
#slice domain name
domain=email[email.index("@")+1:]
#format message
output="Your username is {} and your domain name is {}".format(user_name,domain)
#diplay output message
print(output)
