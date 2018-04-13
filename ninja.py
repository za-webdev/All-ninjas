from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def no_ninjas():
	return "No Ninjas here"

@app.route('/ninja')
def all_ninjas():
	return render_template('about.html', allNinjas=True)

@app.route('/ninja/<color_ninja>')
def color(color_ninja):
	return render_template('about.html',color=color_ninja, allNinjas=False)

app.run(debug=True)