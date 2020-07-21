print('hello world')

def menu(food, *args, **kwargs):
  """ hogehoge Docstrings """
  print(food)
  print(args)
  print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

print(menu.__doc__)