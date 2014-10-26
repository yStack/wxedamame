# -*- coding:utf-8 -*-
import hashlib
import time
import xml.etree.ElementTree as ET
from flask import Flask, render_template, request

app = Flask(__name__)

def acess_verification():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    token = 'edamame123'
    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    hashstr = hashlib.sha1(''.join(tmplist)).hexdigest()
    if hashstr == signature:
        return echostr

def parse_msg(xml_string):
    root = ET.fromstring(xml_string)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg

def response(msg,content):
    resp_msg = INF % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), content )
    return resp_msg

INF = \
'''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
'''

HELP_INF = \
'''
你好
'''

def is_new_user(msg)
    return msg['MsgType'] == "event" and msg['Event'] == "subscribe"


@app.route('/')
def homepage():
     return render_template('index.html')

@app.route('/weixin',methods = ['GET', 'POST'])
def re_msg():
    if request.method == 'GET':
        return acess_verification()
    if request.method == 'POST':
        data = request.data
        msg = parse_msg(data)
        if is_new_user(msg):
            return response(msg,HELP_INF)


if __name__ == "__main__":
    app.debug = False
    app.run()