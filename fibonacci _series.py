# Method for fibonacci series
def fibonacci(count):
    a = [1, 2]
    # Lambda function to append fibonacci numbers series
    any(map(lambda _: a.append(sum(a[-2:])), range(2, count)))
    return a[:count]

# Print fibonacci series from 1 to 50
print(fibonacci(50))