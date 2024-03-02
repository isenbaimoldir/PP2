def list_to_set(x):
    return set(x)

numbers = list(map(int, input().split()))
print(list_to_set(numbers))