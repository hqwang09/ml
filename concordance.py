import re

class Concordance(object):
    def __init__(self):
        """
          Initialize regular expression pattern used to split 
        sentences and words.
        """
        self._sentence_pattern = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
        self._word_delimiter = r'[()\[\]{}/\\\<>$;,:\-—"\s]+'
    
    def getIndexStr(self, i):
        """
          Return the alphabetical string according to integer index, 
        e.g. 1 ==> a, 26 ==> z, 27 ==> aa, 28 ==> ab.
          Input: i - an integer
          Output: Alphabetical string transformed from input i.
        """
        numOfCharacters = 26
        res = chr((i-1) % numOfCharacters + ord('a')) * \
                  (1 + (i-1)//numOfCharacters) + "."
        return res
    
    def splitToSentences(self, txt):
        """
          Split a paragraph txt to sentences.
          Input: txt in string format.
          Output: A list of sentences splited from input txt.
        """
        sentences = re.split(self._sentence_pattern, txt)
        return sentences
    
    def wordsCount(self, txt):
        """
          Count words frequency in txt.
          Input: txt in string format.
          Output: A dictionary with key as the word splited, value as a list where the
               first element of the list is the number of occurences of the key, and 
               the rest elements as the sentences number of the occurences of the key. 
        """
        frequency = {}
        sentences = self.splitToSentences(txt)
        for i in range(len(sentences)):
            sentence = sentences[i].lower().strip(r'?|!|.').strip() #strip off end characters .?! and white space
            words = list(filter(None, re.split(self._word_delimiter, sentence))) #tokenize words
            for word in words:
                if word in frequency:
                    frequency[word][0] += 1 #Words occurences add by 1.
                    frequency[word].append(i+1) #Words occurences sentence number.
                else:
                    frequency[word] = [1, i+1] #Words occurence and sentence number.
        return frequency
    
    def printWordsFrequency(self, frequency):
        """
          Print out the words frequency accouting in the format provided by sample.
        """
        i = 1 
        for key, item in sorted(frequency.items()):
            print("{:4s} {:20s} {{{}:{}}}".format(self.getIndexStr(i), key, item[0], \
                                                  ",".join(str(x) for x in item[1:])))
            i += 1                              