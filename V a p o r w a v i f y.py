
print("Input the character you want in between every character")
print("""Examples: 
A " " or a space will look like this: t e s t
A "-" will look like this: t-e-s-t
""")
boop = input("Input the character without quotations: ")
string = input("Input text to V a p o r w a v i f y : ")

new_string_to_list = list(string)

vaper= (boop).join(new_string_to_list)
print(vaper)