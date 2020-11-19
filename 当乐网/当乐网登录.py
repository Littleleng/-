import requests
import js2py

js_obj = js2py.EvalJs()
data = open('当乐网js.js', 'r', encoding='utf8').read()
js_obj.execute(data)

result = js_obj.rsa("123456")
print(result)

url = 'https://oauth.d.cn/auth/login?' \
      'display=web&' \
      'name=dcn_215418001&' \
      'pwd={}&to=https%253A%252F%252Fwww.d.cn%252F&geetest_challenge=03796f2b6009c81a653578433d226072&geetest_validate=f14085d62406c0aeb77d9167bdd28db1' \
      '&geetest_seccode=f14085d62406c0aeb77d9167bdd28db1%7Cjordan'.format(result)