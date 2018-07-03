# Question: Consider the following list:
# ids=["B3","\nB4","\nB5","\nB6"]
# Then, write a program that produces a text file which looks like this:
#   B3
#   B4
#   B5
#   B6

ids=["B3","\nB4","\nB5","\nB6"]

file = open("Section-4.1.output.txt", 'w')
for id in ids:
    file.write(id)
file.close()

