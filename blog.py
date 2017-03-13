from flask import Flask, render_template
import time
import os
app = Flask(__name__)


def generate_list(list_of):
	for filename in os.listdir(path='.'):
		if filename.endswith('.txt'):
			list_of.append(filename)
	return list_of

@app.route('/')
def index():
	list_of_art = list()
	list_of_art = generate_list(list_of_art)
	return render_template('index.html', list=list_of_art)

@app.route('/new')
def entry():
	return render_template('enter_article.html')

@app.route('/articles')
def data():
	list_of_art = list()
	list_of_art = generate_list(list_of_art)
	dict_of_art = dict()

	file = None
	text = None
	for indice , article in enumerate(list_of_art, start=1):
		file = open(article, 'r').readlines()
		statinfo = time.ctime(os.stat(article).st_ctime)
		print(statinfo)
		file.append(str(statinfo))
		dict_of_art[str(indice)] = file
	print(dict_of_art)

	return render_template('articles.html', names=list_of_art, files=dict_of_art )

if __name__ == "__main__":
    app.run()