import requests
import js2py

js_obj = js2py.EvalJs()
data = open('爱奇艺js.js', 'r', encoding='utf8').read()
js_obj.execute(data)

result = js_obj.rsaFun("123456")
print(result)

