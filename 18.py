def fun(str1):
  s1 = str1.find('not')
  s2 = str1.find('poor')
  

  if s2 > s1 and s1>0 and s2>0:
    str1 = str1.replace(str1[s1:(s2+4)], 'good')
    return str1
  else:
    return str1
print(fun('The guy is not that poor'))
print(fun('The guy is poor'))
