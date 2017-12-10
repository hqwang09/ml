# nltk

1)Source code:
  a) concordance.py - the solution code
  b) test_concordance.py - the test code
  c) 3 test data files: test1.txt, test2.txt, test3.txt
  To generate the print in the sample provided, please run 
    $python test_concordance.py Test_concordance.test_split_sentences_bw
  To test with other text, please first enter into the downloaded folder and run the following commands in python console:
  >>>import concordance

  >>>concord = concordance.Concordance()
  
  >>>words_frequency=concord.wordsCont(text)  #where text is the text used for test
  
  >>>concord.printWordsFrequency(words_frequency) #print out the words account in the sample format

  The above code has been tested with python 3.5.2

2)It cost about 4 to 5 hours to research the method, implement the code and solve some nuts and bolts issues found during test.

3)The deficiency of the code:
  The main difficulty of this test would be how to treat those nuts and bolts of special words abbreviations and delimiters. For example, a simple r'[\w]+' regex patter will split abbreviation word "i.e." into two words "i" and "e". To improve the code, we need to use the code to learn with more text, find out these issues and add the correct treatment of these issues into the code, like compare machine learning image recognition with human recognition to help the improve the machine image recognition accuracy.
