# Short Form Generator using Python
user_input = str(input("Enter a phrase you want acronym(short form) of: "))
res = user_input.split()
acronym = ''
for i in res:
    acronym = acronym + str(i[0]).upper()
print(acronym)