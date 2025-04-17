def log_in(name, password):
    dic = {
        "Asha": "12",
        "John": "abcd",
    }
    
    if name in dic:
        if dic[name] == password:
            return "Login successful"
        else:
            return "Login unsuccessful"
    else:
        return "User doesn't exist"

print(log_in("Asha", "12"))
print(log_in("Asha", "1234"))
# print(log_in("A", "12"))
