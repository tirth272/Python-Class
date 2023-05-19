def rev_str(str):
    if len(str) % 4 == 0:
       return ''.join(reversed(str))
    return str

print(rev_str('heyy'))
