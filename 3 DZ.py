a = int(input())   #https://stepik.org/lesson/3369/step/8?unit=952

import itertools

def sequence(num):
    return ([num for i in range(num)])
    
num = [sequence(i) for i in range(1, a+1)]  

print(*list(itertools.chain(*num))[:a])




#list_num = [int(i) for i in input().split()]     #https://stepik.org/lesson/3369/step/9?unit=952
#ind = int(input())
#if ind in list_num:
    #print(*[i for i, e in enumerate(list_num) if e == ind] )
#else: print('Отсутствует')



#from collections import Counter                   # https://stepik.org/lesson/3373/step/6?unit=956
#counter = Counter(input().lower().split())
#for i in counter:
    #print (i, counter[i])



#with open('D:\Скачал\dataset_3363_2.txt', 'r') as f:        # https://stepik.org/lesson/3363/step/2?unit=1135
#     import re
#     code = f.read()
#     result_list_num = re.findall(r'\d+', code)
#     result_list_letter = [c for c in code if c.isalpha()]
#     decode = []
#     out = open('D:\Скачал\solution.txt', 'w')
#     for i in list(zip(result_list_letter, result_list_num)):
#         decode.append(i[0]*int(i[1]))
#     out.write("".join(decode))
# print("".join(decode))




import re, collections                                        # https://stepik.org/lesson/3363/step/3?unit=1135
# with open ('D:\Скачал\dataset_3363_3.txt', 'r') as file:
#     words_for_count = collections.Counter(re.findall(r'\w+', file.read().lower())).most_common(5)
#     print(*words_for_count[0])




# import numpy as np                                          # https://stepik.org/lesson/3363/step/4?unit=1135
# marks = []
# with open('D:\Скачал\dataset_3363_4 (2).txt', 'r') as f:
#     for line in f:
#         line = tuple(map(int, line.split(";")[1:]))
#         print(sum(line) / len(line))
#         marks.append(line)
#
# marks = np.array(marks)
# print(*np.sum(marks, 0)/len(marks))




# import requests                                              # https://stepik.org/lesson/3378/step/3?unit=961
#
# link = 'https://stepic.org/media/attachments/course67/3.6.3/'
# text_in = '699991.txt'
#
# while text_in:
#     print(text_in)
#     req = requests.get(link + text_in)
#     if req.text.startswith('We'):
#         print(req.text)
#         text_in = False
#     else: text_in = req.text
