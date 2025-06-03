def log_user(name, age, status="unverified"):
    # user = "User: " + name + " Age: " + str(age) + " Status: " + status
    # user = "User: {0} Age: {1} Status: {2}".format(name, age, status)
    user = f"User: {name} Age: {age} Status: {status}"
    return user


print(log_user("Alice", 30, "active"))
# print(log_user(age=30, name="Bubu"))
print(log_user("Bob", 25))
