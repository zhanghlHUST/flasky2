from flask import Flask,render_template

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name == 'world':
        name = '<em>World</em>'
    return render_template('hello-1.html', name=name, digits=[1,2,3,4,5],
                           users=[{'name':'John'},
                                  {'name':'Tom', 'hidden':True},
                                  {'name':'Lisa'},
                                  {'name':'Bob'}])

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)