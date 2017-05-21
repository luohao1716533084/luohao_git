#coding:utf-8
from bs4 import BeautifulSoup

with open("E:/kaoshixing/LTE-关键技术.txt", 'r', encoding='utf-8') as f:
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')

question = soup.select('#content div div div dl dt span.qc')
choose = soup.select('#content div div dl span dd label a')
answer = soup.select('#content div div div dl div div.answerRight')

list_answer = []
for i in answer:
    list_answer.append(i.get_text().strip())

list_answers = [''.join(i).split()[0:2] for i in list_answer]

list_question = []
for i in question:
    list_question.append(i.get_text().strip())

list_questions = [str(''.join(i).split()[1::]) for i in list_question]

list_choose = []
for i in choose:
    list_choose.append(i.get_text().strip())

list_chooses = []
for i in range(0, 80):
    list_chooses += [[]]

list_chooses[0].append(list_choose[0])

list_chooses_count = 0
for i in list_choose[1::]:
    if i[0] == 'A' or i[0] == '正':
        list_chooses_count += 1
    list_chooses[list_chooses_count].append(i)

list_questions_num = []
for i in range(0, 80):
    list_questions_num += [[]]

questions_count = [i + 1 for i in range(len(list_questions))]

for i, j, k in zip(questions_count, list_questions, list_questions_num):  #增加问题列表序号
    list_questions_num[int(i-1)].append(str(i) + str(".") + j)

with open("E:/kaoshixing/LTE-关键技术-answer.txt", 'w', encoding='utf-8') as f:
    for i, j, k in zip(list_questions_num, list_answers, list_chooses):
        f.write(str(i[0]) + '\n')
        for c in k:
            f.write(str(c) + '\n')
        f.write(str(j[0] + j[1]) + '\n' + '\n')