from flask import Flask, request, render_template, url_for, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
	return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
 	with open('database.txt', mode='a') as database:
 		email = data["email"]
 		subject = data["subject"]
 		message = data["message"]
 		file = database.write(f'\n{email}, {subject},{message}') 

def write_to_csv(data):
 	with open('database.csv', mode='a', newline='') as database2:
 		email = data["email"]
 		subject = data["subject"]
 		message = data["message"]
 		csv_writer = csv.writer(database2, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
 		csv_writer.writerow([email, subject,message]) 
		
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		write_to_csv(data)
		return 'It works. Yippie!!'
	else:
		return 'Something went wrong. Please try again'
	#return render_template('index.html')


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
# 	if request.method == 'POST':
# 	 	data = request.form.to_dict()
# 	 	write_to_file(data)
# 	 	return 'It works!!!'
#     else:
#     	return 'something went wrong. Try again!'
	# 	write_to_csv(data)
	# 	#return redirect('/work.html')
		
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    #return 'form submitted hooray!!!'#render_template('login.html', error=error)

@app.route('/work')
def work():
 	return render_template('work.html')

