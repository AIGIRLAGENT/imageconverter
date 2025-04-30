#SID
#Diving into AI and started to learn Python as building blocks
#ASCII ART for S
print("SID"  )
print("1. Simple way to Print the name")
print(" SSS ")
print("S   S")
print("S"    )
print(" SSS ")
print("    S")
print("S   S")
print(" SSS ")
print("\n")
print("2. More efficient way to print ASCII using a loop")

s_art = [" SSS ","S   S","S"    ," SSS ","    S","S   S"," SSS "]
for ASCII_S in s_art:
  print(ASCII_S)

print("\n")
print("3. Most efficient way to print ASCII using a loop and by defining a function")
def print_s():
  s_art_1 = [" SSS ","S   S","S"    ," SSS ","    S","S   S"," SSS "]
  for ASCII_S2 in s_art_1:
    print(ASCII_S2)
print_s()

print("\n")
#ASCII ART for K
print("KUMAR")
print("1. Simple way to Print the name")
print("K   K")
print("K  K" )
print("K K"  )
print("K"    )
print("K K"  )
print("K  K" )
print("K   K")

print("\n")
print("2. More efficient way to print ASCII using a loop")
k_art= ["K   K","K  K" ,"K K"  ,"K"    ,"K K"  ,"K  K" ,"K   K"]
for ASCII_K in k_art:
  print(ASCII_K)

print("\n")
print("3. Most efficient way to print ASCII using a loop and defining a function")

def print_k():
  k_art2 = ["K   K","K  K" ,"K K"  ,"K"    ,"K K"  ,"K  K" ,"K   K"]
  for ASCII_K2 in k_art2:
    print(ASCII_K2)
print_k()

print("\n")
print("These were ways to print one character at a time. But what if you wanted to print the full name like SID. You define function with each charcter first. then assign this function to variable and then print the variable with ZIP()")

def get_s():
  return [" SSS ","S   S","S    "," SSS ","    S","S   S"," SSS "]

def get_i():
  return ["IIIII","  I  ","  I  ","  I  ","  I  ","  I  ","IIIII"]

def get_d():
  return ["DDDD ","D   D","D   D","D   D","D   D","D   D","DDDD "]

s_art= get_s()
i_art= get_i()
d_art= get_d()

for s_line,i_line,d_line in zip (s_art,i_art,d_art):
  print(s_line + " " +" "+ i_line + "  "+" "+ d_line)





