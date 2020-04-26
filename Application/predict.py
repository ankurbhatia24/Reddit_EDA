import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
# from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
import pickle
import stopwords

EMBEDDING_DIM = 300
MAX_TITLE_LENGTH =  20 
MAX_COMMENTS_LENGTH = 200
MAX_BODY_LENGTH = 150
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;.]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
# STOPWORDS = set(stopwords.words('english'))
STOPWORDS = stopwords.stop_words()

#load model
loaded_model = keras.models.load_model('final_model.h5', compile=False)

label_decode_dict = {0: 'AskIndia',
                         1: 'Coronavirus',
                         2: 'Non-Political',
                         3: 'Scheduled',
                         4: 'Photography',
                         5: 'Science/Technology',
                         6: 'Politics',
                         7: 'Business/Finance',
                         8: 'Policy/Economy',
                         9: 'Sports',
                         10: 'Food',
                         11: 'AMA'}

sequence_length = {"title" : MAX_TITLE_LENGTH,
                   "comments" : MAX_COMMENTS_LENGTH,
                   "body" : MAX_BODY_LENGTH,
                   "title_body" : MAX_TITLE_LENGTH + MAX_BODY_LENGTH,
                   "title_comments" : MAX_TITLE_LENGTH + MAX_COMMENTS_LENGTH,
                   "title_comments_body" : MAX_TITLE_LENGTH + MAX_COMMENTS_LENGTH + MAX_BODY_LENGTH
                   }

def string_form(value):
    return str(value)

def clean_text(text):
    text = BeautifulSoup(text, "lxml").text
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text

def label_decode(label_value):
 	return label_decode_dict.get(label_value)


def preprocess(data_dict):
	url = data_dict["url"]
	title = data_dict["title"]
	body = data_dict["body"]
	flair = data_dict["flair"]
	comments = data_dict["comments"]
    #clear body of removed/deleted/nan posts
	empties = ['nan', '[deleted]', '[removed]']
	for empty in empties:
		body = body.replace(empty, '')

	title = string_form(title)
	body = string_form(body)
	comments = string_form(comments)

	title = clean_text(title)
	body = clean_text(body)
	comments = clean_text(comments)

	# return ({"url" : url,
 #    		 "title" : title,
 #    	     "body" : body, 
 #    	     "flair" : flair,
 #    	     "comments" : comments})

 #    also see here cleaning of emojis
	# here combine the feature accoring to the model

	text = str(title) #change accordingly
	text_type = "title"

	#load the saved Tokenizer
	#Load tokenizer
	tokenizer = pickle.load(open(f"{text_type}_tokenizer.pickle", "rb" ))
	max_sequence_length = sequence_length.get(text_type)
	#load the max_sequence_length
	#####
	print(text)
	text = tokenizer.texts_to_sequences([text])
	print(text)
	text = pad_sequences(text, 
		                 maxlen=max_sequence_length)
	print(text)
	# loaded_model = keras.loaded_model('final_model.h5') #loaded globally
	# loaded_model.summary()
	predict = loaded_model.predict(text)
	print(predict)
	label_decoded = label_decode(predict.argmax(axis = 1)[0])

	return label_decoded
	



