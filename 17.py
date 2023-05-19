def string(str):
  l = len(str)

  if l > 2:
    if str[-3:] == 'ing':
      str += 'ly'
    else:
      str += 'ing'

  return str
print(string('hello'))
print(string('hing'))
print(string('heyyyy'))