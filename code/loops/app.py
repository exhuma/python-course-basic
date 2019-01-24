# Loop over each item in a list with an index
mydata = [1, 2, 3, 4]
for i, item in enumerate(mydata):
    print(i, item)

# Loop until the user wants to quit
response = 'y'
while response != 'n':
    response = input('Do you want to continue [y/n]?')
