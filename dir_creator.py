import os
subs =['Physics', 'Chemistry', 'Systems_Biology', 'Mathematics', 'Earth_Science']

for j in subs:
    str1='mkdir {}'.format(j)
    os.system(str1)
    for i in range(1,11):
        str3='cd {} && mkdir Sem_{}'.format(j,i)
        os.system(str3)
for j in subs:
    for i in range(1,11):
        str3='cd {}/Sem_{} && echo empty > tt.txt'.format(j,i)
        os.system(str3)        