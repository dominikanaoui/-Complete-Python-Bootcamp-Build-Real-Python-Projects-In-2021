#First solution doesn't work as in a path there are spaces
#a = open('D:\Udemy Complete Python Bootcamp Build Real Python Projects in 2021\Program1\File.txt', 'r')
#print(a.read())

a = open(r"D:\Udemy Complete Python Bootcamp Build Real Python Projects in 2021\Program1\File.txt")
print(a.read())