c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]

A = input()
for i in c_alpha:
    A = A.replace(i, '@')
    
print(len(A))
        