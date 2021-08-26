# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequency(s):
	f = len(s)
	for ch in s:
		c = s.count(ch)
		f = min(f, c)
	return f

def leastfrequentletters(s):
	s = s.lower()
	alphs = ""
	for ch in s:
		if ch.isalpha():
			alphs += ch
	if alphs == "":
		return ""
	freq = leastfrequency(alphs)
	s = ""
	for ch in alphs:
		if alphs.count(ch) == freq:
			s += ch
	res = ""
	for i in range(26):
		if len(res) == len(s):
			return res
		ch = chr(ord("a")+i)
		if ch in s:
			res += ch
	return res