from postfix_notation import Calculator

input = ["2", "1", "-"]
s = []
result = Calculator(input, s)
print(int(result))
1
input = ["1", "2", "*", "3", "4", "*", "+"]
s = []
result = Calculator(input, s)
print(int(result))
14
input = ["4", "2", "/", "4", "4", "4", "/", "2", "*", "/", "-"]
s = []
result = Calculator(input, s)
print(int(result))
0
input = ["278241", "489", "/", "6456", "*", "46546", "+"]
s = []
result = Calculator(input, s)
print(int(result))
3720010