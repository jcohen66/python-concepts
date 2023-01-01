# Should not use eval in prod because
# you cant validate arguments before
# execution.

def cal(a, b, op): return eval(f'{a} {op} {b}')

print(cal(1,2,'+'))
print(cal(10,4,'-'))
print("Cat",2,'+')

