from flask import Flask, request, render_template, jsonify
import praw
import validators
import predict
#save these using praw.ini files


reddit = praw.Reddit(client_id='xIQ7eUUJzsg5nA', 
	                 client_secret='14hz-3KSfKxkV1y2qB5B1xLWMvo', 
	                 user_agent='subreddit_data_analytics')

def parse_url(url):
    try:
    	url = url.decode('utf-8') #bytes type to string
    	url = url.split('/n')[0]  #(remove newline)
    except:
    	url = url
    	url = url.split('/n')[0]
    #validate url
    if(validators.url(url)):
    	submission = reddit.submission(url = url)
    	title = submission.title
    	body = submission.selftext
    	flair = submission.link_flair_text
    	#If you want, can check here if the flair is valid or not
    	submission.comments.replace_more(limit=None)
    	comments = ''
    	for top_level_comment in submission.comments:
    		comments = comments + ' ' + top_level_comment.body
    	
    	return ({"url" : url,
    		     "title" : title,
    	         "body" : body, 
    	         "flair" : flair,
    	         "comments" : comments})
    else:
    	return None



app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def send():
	if(request.method == 'POST'):
		url = request.form['url_to_post']
		# print(url)
		submission_dict = parse_url(url)
		# print(submission_dict)
		label_predicted = predict.preprocess(submission_dict)
		submission_dict["label_predicted"] = label_predicted
		print('*'*100)
		print(label_predicted)
		return render_template('show.html', data=submission_dict)

	return render_template('index.html')

@app.route("/automated_testing", methods=["GET", "POST"])
def automated_testing():
	#if check for post request
	print("I am in")
	file = request.files.to_dict()["upload_file"]
	response = {}
	for line in file:
		submission_dict = parse_url(line)
		# print(f"The Submission dict is {submission_dict} \n")
		label_predicted = predict.preprocess(submission_dict)
		response[submission_dict["url"]] = label_predicted

	file.close()

	#else see what to return when get request

	return jsonify(response)  #Send a json response

if __name__ == "__main__":
	app.run(threaded=False)
