def debugger(num):
    print(f"This will check if {num} is a power of 2")
    result = "Yes" if (num & (num - 1)) == 0 else "No"
    print(f"Result: {result}")


debugger(16)
