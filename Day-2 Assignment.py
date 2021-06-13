'''How to print a value?'''
print("30 days 30 hour challenge")
print('30 days 30 hour challenge')

'''Assigning String to Variable:'''
H = "Thirty"
print(H)

'''Indexing using String:'''
Days = "Thirty days"
print(Days[5])

'''How to print the particular character from certain text?'''
Challenge = "I won"
print(Challenge[3:4])

'''Print the length of Character:'''
Challenge = "I won"
print(len(Challenge))

'''Convert String into lower character:'''
Challenge = "I will win"
print(Challenge.lower())

'''String Concatenation – Joining two strings:'''
y = "30 Days"
x = "30 hours"
c = x + y
print(c)

'''Adding space during concatenation:'''
x = "30 Days"
y = "30 hours"
z = x + " " + y
print(z)

'''casefold() - Usage:'''
text = "Thirty days and Thirty hours"
x = text.casefold()
print(x)

'''Capitalize()'''
text = "Thirty days and Thirty hours"
x = text.capitalize()
print(x)

'''find()'''
text = "Thirty days and Thirty hours"
x = text.find("d")
print(x)

'''isalpha()'''
text = "Thirty days and Thirty hours"
x = text.isalpha()
print(x)

'''isalnum()'''
text = "30daysand30hours"
x = text.isalnum()
print(x)

