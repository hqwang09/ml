import unittest
import concordance

"""
  Test cases for Concordance class to split sentences and words accounting.
"""

class Test_concordance(unittest.TestCase):
    def setUp(self):
        self._concord = concordance.Concordance()
        pass
    
    def test_split_sentences_bw(self):
        with open('test1.txt', 'r') as f:
            text = f.read().lower()
            words_frequency = self._concord.wordsCount(text)
            self._concord.printWordsFrequency(words_frequency)
        return None
    
    def test_word_count_spaCy(self):
        with open('test2.txt', 'r') as f:
            text = f.read().lower()
            words_frequency = self._concord.wordsCount(text)
            self._concord.printWordsFrequency(words_frequency)
        return None
        
    def test_word_count_test3(self):
        with open('test3.txt', 'r') as f:
            text = f.read().lower()
            words_frequency = self._concord.wordsCount(text)
            self._concord.printWordsFrequency(words_frequency)
        return None
    
if __name__ == '__main__':
    unittest.main()
