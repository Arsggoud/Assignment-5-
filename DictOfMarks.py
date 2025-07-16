Dict = {'Alice':80, 'Arun':90, 'Ron':52,}
name = input("Enter the student's name:-- ")
keys = list(Dict.keys())
if name == keys[0]:
    print(f"{name}'s marks: {Dict[name]}")
elif name == keys[1]:
    print(f"{name}'s marks: {Dict[name]}")
elif name == keys[2]:
    print(f"{name}'s marks: {Dict[name]}")
else:
    print("Student not found.")