from urllib import urlopen
story = urlopen('https://sixty-north.com/publications.html')
story_words = []
for line in story:
	line_words = line.split()
	for word in line_words:
		story_words.append(word);
story.close()
for word in story_words:
	print(word)