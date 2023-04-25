x='Robebert'
print(str.isdigit(x))
szer=10
#print('*' * (10//2),x,'*' * (10//2))
print(x.center(10, '*'))
print(x.rstrip('t'))
print(x.lstrip('r'))
print(x.isupper())
print(x.count('be'))
#print()

'''
''6. Dla chętych ciąg składa się tylko z cyfr i liter i ma conajmniej 1 dużą literę 
“Abc” ✅ 
“123abC” ✅ 
“ab123cd” 🚫 
“abcd” 🚫 
“ABC” 🚫 
“12345” 🚫
'''