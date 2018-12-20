import json, time
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

from datamuse_search import datamuse	# datamuse(clue, length = 3)
from google_search import google		# google(clue, length=None, seleniumUsed=False)
from wikipedia_search import wikipedia	# wikipedia(clue, length=None, seleniumUsed=False)
from try_words import try_words			# try_words(word_list, desired_word)
from words import get_word_list			# get_word_list(length)

# Declare static file and flask
app = Flask(__name__, static_url_path='/static')

# Disable CORS
CORS(app)

@app.route('/solve/<day>/<month>/<year>')
def solve(day, month, year):

	date = 'C:/Users/Asus/Desktop/demo2/static/data/' + day + '_' + month + '_' + year + '.json'
	with open(date) as json_file:
		data = json.load(json_file)


	across_no = []
	down_no = []
	across_clue = [""]*10
	down_clue = [""]*10
	across_word = []
	down_word = []


	"""
	ok = 0
	s = ""
	for c in data['across']:
		no = int(c['no'])
		across_no.append(no)
		across_clue[no] = c['text']

		for i in range(0,25,5):
			for j in range (5):
				for c_no in data['cells']:
					if int(c_no) == no:
						ok = 1
			if ok == 1:
				s = ""
				for k in range(5):
					if (data['answers'][i+k] != "-1"):
						s = s + data['answers'][i+k]
						print(s)
				ok = 0
		across_word[no] = (s.lower())



	print (across_no)
	print (across_clue)
	print (across_word)
	"""
	"""
	for c in data['down']:
		down_word[c['no']] = c['text']
	"""



	s = ""
	for i in range(0,25,5):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	down_word.append(s.lower())
	s = ""
	for i in range(1,25,5):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	down_word.append(s.lower())
	s = ""
	for i in range(2,25,5):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	down_word.append(s.lower())
	s = ""
	for i in range(3,25,5):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	down_word.append(s.lower())
	s = ""
	for i in range(4,25,5):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	down_word.append(s.lower())

	s = ""
	for i in range(0,5):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	across_word.append(s.lower())
	s = ""
	for i in range(5,10):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	across_word.append(s.lower())
	s = ""
	for i in range(10,15):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	across_word.append(s.lower())
	s = ""
	for i in range(15,20):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	across_word.append(s.lower())
	s = ""
	for i in range(20,25):
		if (data['answers'][i] != "-1"):
			s = s + data['answers'][i]
	across_word.append(s.lower())

	write_answer = "{"
	i = 0
	for c in data['across']:
		a = solve_one_word(c['text'], len(across_word[i]), across_word[i])
		write_answer += "\"A_" +str(i)+ "\": \"" + a[0] + "\","
		i = i + 1

	i = 0
	for c in data['down']:
		d = solve_one_word(c['text'], len(down_word[i]), down_word[i])
		if i == 4:
			write_answer += "\"D_" +str(i)+ "\": \"" + d[0] + "\""
		else:
			write_answer += "\"D_" +str(i)+ "\": \"" + d[0] + "\","
		i = i + 1
	write_answer += "}"

	time.sleep(0.2)
	name = 'C:/Users/Asus/Desktop/demo2/static/'+day + '_' + month + '_' + year + 'answer.json'
	file = open(name, "w")
	file.write(write_answer)
	file.close()

	time.sleep(0.2)
	data = {}
	data['state'] = ["DONE!"]
	with open('static/state.json', 'w') as write_file:
		json.dump(data, write_file)

	return "hello"

def solve_one_word(clue, length, desired_word):
	#clue = clue.replace("+", " ")
	print(clue, length, desired_word)
	possible_words = []

	possible_words.extend(datamuse(clue, length))
	time.sleep(0.2)
	data = {}
	data['state'] = ["... datamuse is added"]
	data['answer'] = [""]
	with open('static/state.json', 'w') as write_file:
		json.dump(data, write_file)
	#print("... datamuse is added")

	possible_words.extend(google(clue, length))
	time.sleep(0.2)
	data = {}
	data['state'] = ["... google is added"]
	data['answer'] = [""]
	with open('static/state.json', 'w') as write_file:
		json.dump(data, write_file)
	#print("... google is added")

	possible_words.extend(wikipedia(clue, length))
	time.sleep(0.2)
	data = {}
	data['state'] = ["... wikipedia is added"]
	data['answer'] = [""]
	with open('static/state.json', 'w') as write_file:
		json.dump(data, write_file)
	#print("... wikipedia is added")

	#possible_words.extend(get_word_list(length))
	time.sleep(0.2)
	data = {}
	data['state'] = ["... wordset is added"]
	data['answer'] = [""]
	with open('static/state.json', 'w') as write_file:
		json.dump(data, write_file)
	#print("... wordset is added")

	#print(possible_words)
	time.sleep(0.2)
	data = {}
	data['state'] = ["... trying to solve ..."]
	data['answer'] = [""]
	with open('static/state.json', 'w') as write_file:
		json.dump(data, write_file)
	#print("... trying to solve ...")
	return try_words(possible_words, desired_word)

# Run app
if __name__ == '__main__':
	app.run(host="0.0.0.0")
