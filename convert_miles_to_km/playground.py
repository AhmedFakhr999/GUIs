# def calc(n, **kw):
#     """Calculate something based on n and keyword arguments"""
#     print(f"n = {n}")
#     print(f"Keyword arguments: {kw}")
    
#     # You can add calculation logic here
#     result = n
#     for key, value in kw.items():
#         if key == 'add':
#             result += value
#         elif key == 'multiply':
#             result *= value
#         elif key == 'subtract':
#             result -= value
    
#     return result

# # Example 1: Simple keyword arguments
# print(calc(5, add=3, multiply=2))  # n=5, kw={'add': 3, 'multiply': 2}

# # Example 2: More complex operations
# print(calc(10, increment=5, square=True))

# # Example 3: No keyword arguments
# print(calc(7))  # n=7, kw={}

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)