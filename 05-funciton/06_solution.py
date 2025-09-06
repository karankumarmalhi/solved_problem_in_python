def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="Karan", cast="Malhi", role="Developer")
print_kwargs(name="Karan", cast="Malhi")
print_kwargs(name="Karan")