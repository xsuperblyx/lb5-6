from bottle import post, request
import re
import pdb
import json
@post('/home', method='post')
def my_form():
     mail = 'qwerty@mail.ru'
     questions = {}
     qwer='dsadsadsacsfg'
     if mail=="" or qwer=="": return "You didn't write email or question"
     else: 
        match=re.search(r'([@]mail[.]ru)',mail)
        if match!=None:
            questions[mail]=qwer
            with open ('questions.txt', 'a') as outfile:
                x = json.dumps(questions)
                open('questions.txt', 'a').write('\n' + x)
            return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "Email format error"  

