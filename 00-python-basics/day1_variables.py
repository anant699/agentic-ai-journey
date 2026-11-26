name = "Alex"           # string
age = 30                # integer
height = 5.9            # float
is_learning = True      # boolean
nothing = None          # the "no value" value

# Show the values
print("name:", name)
print("age:", age)
print("height:", height)
print("is_learning:", is_learning)
print("nothing:", nothing)

# Type checking
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_learning))  # <class 'bool'>
print(type(nothing))    # <class 'NoneType'>

# Type conversion
age_str = str(age)      # "30"
year = int("2026")      # 2026
print("age_str:", age_str, type(age_str))
print("year:", year, type(year))
print("year + 1 =", year + 1)
