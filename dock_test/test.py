#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request

app = Flask(__name__)

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['GET'])
def index():
    return "Hello World"
    
if __name__ == '__main__':
    app.run()

