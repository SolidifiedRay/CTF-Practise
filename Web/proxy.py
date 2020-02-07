#http://wargames.csaw.io:5003/

#!/usr/bin/python3

from flask import Flask, request, send_file

app = Flask(__name__)

form = '''
<form>
<input name="page" placeholder="page">
<input type="submit" name="submit">
</form>

<form>
<input type="submit" name="src" value="show source" >
</form>
'''

@app.route('/')
def index():
    if 'page' in request.args:
        page = request.args.get('page')
        page = page.replace('../', '')
        return send_file(page)
    if 'src' in request.args:
        return open('app.py').read()
    return form


if __name__ == "__main__":
    app.run('0.0.0.0', 5002)



#http://localhost:5003/secret