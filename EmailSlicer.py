email = str(input("Enter your email id : "))
username = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
print(f"Username: {username} domainName: {domain_name}")