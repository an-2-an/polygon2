# LIST

a = ['Andy', 'Bobby', 'Charlie', 'Dan']

# print(type(a))
# print(a)
# print(len(a))

# for idx in range(len(a)):
#     el = a[idx]
#     print(idx, el, len(el))

# m = 0
#
# for el in a:
#     print(el)
#     if len(el) > m:
#         m = len(el)
#
# print('max len =', m)

for idx, el in enumerate(a, start=1001):
    print(f'{idx}) {el}')
