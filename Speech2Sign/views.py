from django.http import HttpResponse
from django.shortcuts import render, redirect
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.staticfiles import finders
import sys
import os
import argparse
from nltk.parse.stanford import StanfordParser
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tree import *
from nltk.stem import PorterStemmer
import nltk



def home_view(request):
	return render(request,'home.html')



def animation_view(request):
	if request.method == 'POST':
		text = request.POST.get('sen')
		#tokenizing the sentence
		text.lower()
		#tokenizing the sentence
		words = word_tokenize(text)

		tagged = nltk.pos_tag(words)
		tense = {}
		tense["future"] = len([word for word in tagged if word[1] == "MD"])
		tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
		tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
		tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])



		#stopwords that will be removed
		stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's',"'", "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't","should"])



		#removing stopwords and applying lemmatizing nlp process to words
		lr = WordNetLemmatizer()
		filtered_text = []
		for w,p in zip(words,tagged):
			if w not in stop_words:
				if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
					filtered_text.append(lr.lemmatize(w,pos='v'))
				elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
					filtered_text.append(lr.lemmatize(w,pos='a'))

				else:
					filtered_text.append(lr.lemmatize(w))


		#adding the specific word to specify tense
		words = filtered_text


		filtered_text = []
		for w in words:
			path = w + ".mp4"
			f = finders.find(path)
			#splitting the word if its animation is not present in database
			if not f:
				for c in w:
					filtered_text.append(c)
			#otherwise animation of word
			else:
				filtered_text.append(w)
		words = filtered_text;


		return render(request,'animation.html',{'words':words,'text':text})
	else:
		return render(request,'animation.html')



os.environ['STANFORD_PARSER'] = 'C:/Users/Shree/Downloads/CS 753/project/stanford-parser-full-2018-10-17'
os.environ['STANFORD_MODELS'] = 'C:/Users/Shree/Downloads/CS 753/project/stanford-parser-full-2018-10-17'
os.environ['JAVAHOME'] = "C:\\Program Files\\Java\\jdk-9.0.4\\bin\\java.exe"
def animation_view2(request):
	if request.method == 'POST':
		text = request.POST.get('sen')
		#tokenizing the sentence
		text.lower()
		#tokenizing the sentence
		words = word_tokenize(text)
		print(words)
		parser=StanfordParser(model_path='C:/Users/Shree/Downloads/CS 753/project/stanford-parser-full-2018-10-17/stanford-parser-3.9.2-models/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
		englishtree=[tree for tree in parser.parse(text.split())]
		parsetree=englishtree[0]
		dict={}
		parenttree= ParentedTree.convert(parsetree)
		for sub in parenttree.subtrees():
			dict[sub.treeposition()]=0
# -------------------
		isltree=Tree('ROOT',[])
		i = 0
		for sub in parenttree.subtrees():
			if(sub.label()=="NP" and dict[sub.treeposition()]==0 and dict[sub.parent().treeposition()]==0):
				dict[sub.treeposition()]=1
				isltree.insert(i,sub)
				i+=1

			if(sub.label()=="VP" or sub.label()=="PRP"):
				for sub2 in sub.subtrees():
					if((sub2.label()=="NP" or sub2.label()=='PRP')and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
						dict[sub2.treeposition()]=1
						isltree.insert(i,sub2)
						i=i+1

# ---------------------
		for sub in parenttree.subtrees():
			for sub2 in sub.subtrees():
				if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
					dict[sub2.treeposition()]=1
					isltree.insert(i,sub2)
					i=i+1

		parsed_sent=isltree.leaves()
		words=parsed_sent
		stop_words=set(stopwords.words("english"))

		lemmatizer = WordNetLemmatizer()
		ps = PorterStemmer()
		lemmatized_words=[]
		# print(parsed_sent)
		for w in parsed_sent:
			lemmatized_words.append(lemmatizer.lemmatize(w))
		islsentence = ""
		# print(lemmatized_words)
		filtered_text = []
		for w in lemmatized_words:
			if w not in stop_words:
				filtered_text.append(w)
				islsentence+=w
				islsentence+=" "
		# print(islsentence)
		words = filtered_text
		print(words)
		filtered_text = []
		for w in words:
			path = w + ".mp4"
			f = finders.find(path)
			#splitting the word if its animation is not present in database
			if not f:
				for c in w:
					filtered_text.append(c)
			#otherwise animation of word
			else:
				filtered_text.append(w)
		words = filtered_text;
		return render(request,'animation2.html',{'words':words,'text':text})
	else:
		return render(request,'animation2.html')



