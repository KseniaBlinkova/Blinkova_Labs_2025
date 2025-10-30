def sort_without_lambda(data):
    return sorted(data, key=abs, reverse=True)

def sort_with_lambda(data):
    return sorted(data, key=lambda x: abs(x), reverse=True)

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
