class TextAnalyzer(object):
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        self.fmtText = formattedText
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        # Create dictionary
        freqMap = {}
    for word in set(wordList): # use set to remove duplicates in list
        freqMap[word] = wordList.count(word)
        return freqMap
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0



#Press Shift+Enter to run the code
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
analyzed = TextAnalyzer(givenstring)
#convert data to lowercase
print("Formatted Text:", analyzed.fmtText)
#counts the frequency
freqMap = analyzed.freqAll()
print(freqMap)
#counts the frequency of specific word.
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")
