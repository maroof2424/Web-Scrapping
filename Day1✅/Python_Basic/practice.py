name = "Maroof"
age = 17
price = 99.98
is_valid = True

print(" ")
print(f"My name is {name} my age is {age}")
print(f"models.py ma price ha {price} aur validaton status {is_valid}")

fruits = ["apple","banana","mango"]
user = {"name":"Maroof","age":16}

for i,fruit in enumerate(fruits):
    print(f"{i} : {fruit}")

print(f"username is {user["name"]} and age is {user["age"]}")





def greet_wrapper(func):
    def inner(name):
        print("🔔 Starting greeting...")
        func(name)  # original greet function call
        print("✅ Greeting complete!\n")
    return inner

@greet_wrapper
def greet(name):
    print(f"Hello {name}")

greet("Maroof")


with open("sample.txt","w") as file:
    file.write("Hello from Python!...")