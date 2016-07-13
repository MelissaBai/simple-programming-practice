def add(dlista, dlistb):
    result = []
    carry = 0
    for i in range(max(len(dlista), len(dlistb))):
        numa = get_at_place(dlista, i)
        numb = get_at_place(dlistb, i)
        digit_sum = numa + numb + carry
        carry = 1 if digit_sum > 9 else 0
        result.append(digit_sum % 10)
    if carry:
        result.append(carry)
    return result

def get_at_place(dlist, place):
    if place >= len(dlist):
        return 0
    return dlist[place]

def to_dlist(n):
    result = []
    while n:
        result.append(n % 10)
        n /= 10
    return result

def from_dlist(dlist):
    result = 0
    while dlist:
        result *= 10
        result += dlist.pop()
    return result

for i in range(501):
    for j in range(100):
        dlista = to_dlist(i)
        dlistb = to_dlist(j)
        print '%s + %s = %s' % (dlista, dlistb, add(dlista, dlistb))
        assert from_dlist(add(dlista, dlistb)) == i + j
