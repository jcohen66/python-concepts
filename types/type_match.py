var = 'Python'

match var:
  case str():
    print('str')
  case bool():
    print("bool")
  case float():
    print('float')
  case int():
    print('int')
  case list():
    print('list')
  case None:
    print("None")
  case _: 
    print('Unknown')