def one():
    print("1")
    two()
    
def two():
    print("2")
    one()

one()
two()
