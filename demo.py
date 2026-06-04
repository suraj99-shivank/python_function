word = learning
with open("demo.py", "r") as f:
    data = f.read()
    if word in data:
        print("The word is present in the file.")
    else:
        print("The word is not present in the file.")
f.close()
