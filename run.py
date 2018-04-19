#coding=utf-8  
import itchat
import requests

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '',  # Tuling Key
        'info': msg,  
        'userid': '', 
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')

@itchat.msg_register(itchat.content.TEXT)

def print_content(msg):
    return get_response(msg['Text'])

@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def print_content(msg):
    return get_response(msg['Text'])

itchat.auto_login(enableCmdQR=1)
itchat.run()

