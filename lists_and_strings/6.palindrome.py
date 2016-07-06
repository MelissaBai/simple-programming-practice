def palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    return True

assert palindrome('')
assert palindrome('a')
assert palindrome('aa')
assert not palindrome('ab')
assert palindrome('aba')
assert palindrome('abba')
assert not palindrome('abcbacd')
print 'Success'
