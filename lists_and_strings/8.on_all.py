def on_all(alist, func):
    return [func(a) for a in alist]






g = lambda x: x**2
print on_all(range(21), g)
