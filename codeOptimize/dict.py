from time import time

t = time();
list = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd']

#û��ת��Ϊ�ֵ��ת��Ϊ�ֵ��ʱ��һ��
list = dict.fromkeys(list, True);

print(list)

filter = []

for i in range(1000000):
    for find in ['is','hat','new','list','old','.']:
        if find not in list:
            filter.append(find)

print("total run time: ")
print time() - t

