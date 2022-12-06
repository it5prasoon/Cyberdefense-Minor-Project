import urllib
import urllib.parse, urllib.request, urllib.error
import queue
from datetime import datetime as dt

target_url = "http://10.10.186.101"
word_file = "ans.txt"
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
operation="Web directory fuzzing"

ext = [".php", ".bak", ".txt", ".inc", ".js"]

def list_build(word_file):
	fd = open(word_file, "r")
	raw_words = fd.readlines()
	fd.close()

	found_res = False
	words = queue.Queue()

	for word in raw_words:
		word = word.rstrip()

		if resume is not None:
			if found_res:
				words.put(word)
			else:
				if word == resume:
					found_res = True
		else:
			words.put(word)

	return words

def bruter(wrd_queue, file_name, extensions=None):
	fd = open(file_name, "w")

	while not wrd_queue.empty():
		attempt = wrd_queue.get()
		attempt_list = []
		if "." not in str(attempt):
			attempt_list.append("/{}/".format(attempt))
		else:
			attempt_list.append("/{}".format(attempt))
		#attempt_list.append("/%s/" % attempt)

		if extensions:
			for extension in extensions:
				attempt_list.append("/{}{}".format(attempt, extension))

		for brute in attempt_list:
			url = "%s%s" % (target_url, urllib.parse.quote(brute))
			print("url", url)

			try:
				headers = {}
				headers["User-Agent"] = user_agent
				r = urllib.request.Request(url, headers=headers)

				response = urllib.request.urlopen(r)
				if len(response.read()):
					resp = str(response.code) +" :: "+url+"\n"
					fd.write(resp)
			except urllib.error.HTTPError as e:
				if hasattr(e, 'code') and e.code != 404:
					resp = "[!!!]" + " :: " +str(e.code) + " :: " + url+"\n"
					fd.write(resp)

		

def back(file_name):
	wrd_queue = list_build(word_file)
	bruter(wrd_queue, file_name)


def fun():
	print("Enter the target url with FUZZ in the position of what you want to fuzz")
	global target_url
	target_url = input()
	print("Currently using dictionary at:",word_file)
	ch = print("Change dictionary? (y/N): ")
	if(ch=="y" or ch =="Y"):
		word_file = input("Enter path to dictionary: ")
	
	name = dt.isoformat(dt.now())
	file_name = "outputs/DirFuzz/"+name+".txt"
	print("[!] Results will be written to file:",file_name)
	return file_name



back("sample")