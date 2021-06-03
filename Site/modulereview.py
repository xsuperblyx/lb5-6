from bottle import post, request
from datetime import datetime
import re
import pdb
import json
@post('/otzivi', method='post')
def reviews():
    #вносим в переменные данные, внесенные пользователем
    revv=request.forms.get('REV')
    nickk=request.forms.get('NICK')
    markk=request.forms.get('MRK')
    #проверка введенных данных
    if (revv!='' and nickk!='' and markk!='' and len(markk)==1 and (markk=='1' or markk=='2' or markk=='3' or markk=='4' or markk=='5')):
        f = open('revstxt.txt', 'a') #параметр 'a' позволяет не переписать файл, а дописать к уже существующим записям
        #добавление отзыва в текстовый файл
        f.write(str(nickk) + '\n' + str(markk) + '/5 (' + str(datetime.now().date()) + ')\n' + str(revv) + '\n---\n')
        f.close()
        return "Thank you!"
    else:
        return "Data entered incorrectly"

