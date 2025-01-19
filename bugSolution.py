def function(a: int, b: int) -> int:
    return a + b

result = function(5, 5)
print(result)

#Alternative solution with explicit type checking:
def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError("Inputs must be integers.")

result = function(5,5)
print(result) 