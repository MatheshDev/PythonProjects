fileName = "student.txt"

# f = open(fileName,"x")
# Write (append mode for practice)
f = open(fileName, "a")
f.write("Maddy\n")
f.write("Chubby\n")
f.write("Sai\n")
f.write("Santhosh\n")
f.write("Navvu\n")
f.close()

f.close()

with open(fileName, "r") as f:
    for line in f:
        print("Welcome", line.strip())