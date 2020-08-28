x = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
# take each item in x, divide by 3, if no remaider, print it


y = [i for i in x if int(i) % 3 == 0]
for i in y:
    print(i)
