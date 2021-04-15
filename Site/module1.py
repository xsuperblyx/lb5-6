from bottle import post, request
import re
import pdb
import json
@post('/home', method='post')
def my_form():
     questions={}
     mail = request.forms.get('ADRESS')
     question = request.forms.get('QUEST')
     regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
     if mail=="" or question=="": return "You didn't write email or question"
     else: 
        if (re.search(regex, mail)):
            questions[mail]=question
            with open ('questions.txt', 'a') as outfile:
                x = json.dumps(questions)
                open('questions.txt', 'a').write('\n' + x)
            return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "Email format error"  

