#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:05:30 2018

@author: shanefenton09
"""

#IMPORTS
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#SETS
posSet = set()
negSet = set()
vocabulary = set()


#DICTS
negDict = dict()
posDict = dict()


#DataFrame
bothDataFrame = pd.DataFrame()

#COUNTS
testTotalLines = 0
trainPosCount = 0
trainNegCount = 0
trainTotalLines = 0

#DRAWING GRAPH
numNegTweetsBefore = 0
numPosTweetsBefore = 0

numNegTweetsAfter = 0
numPosTweetsAfter = 0

#THESE VALUES ARE TO STORE THE DATA WITHOUT FILTERS
negDictTwo = dict()
posDictTwo = dict()
bothDataFrameTwo = pd.DataFrame()
posSetTwo = set()
negSetTwo = set()
vocabularyTwo = set()

#--------------------------------------------           
#           START FUNCTION
#-------------------------------------------- 
def start():
   
    #Stage One
    storeAllUniqueWords()   
    storeAllUniqueWordsWithoutFilter()
    
    recordFrequencyOfWords()
    recordFrequencyOfWordsWithoutFilter()
    
    #Stage Two  
    calculateWordProbability()
    calculateWordProbabilityWithoutFilter()
    
    #Stage Three
    classifyingUnseenTweets()
    
    #Opening Text Files
    negTxtFile = open('dataFiles/test/testNeg.txt',newline='',encoding='latin-1')
    posTxtFile = open('dataFiles/test/testPos.txt',newline='',encoding='latin-1')
    
    negTxtFile1 = open('dataFiles/test/testNeg.txt',newline='',encoding='latin-1')
    posTxtFile1 = open('dataFiles/test/testPos.txt',newline='',encoding='latin-1')
    
    #Classifying all unseen tweets before data filter
    classifyingUnseenTweetsTest(negTxtFile,"Negative","before")
    classifyingUnseenTweetsTest(posTxtFile,"Positive","before")
    
    #Classifying all unseen tweets after data filter
    classifyingUnseenTweetsTest(negTxtFile1,"Negative","after")
    classifyingUnseenTweetsTest(posTxtFile1,"Positive","after")
    
    #Stage Four
    visualization()
    
    
    
#--------------------------------------------           
#   STORING ALL UNIQUE WORDS IN A SET
#-------------------------------------------- 
def storeAllUniqueWords():
    
    #Accessing global variables
    global vocabulary
    
    #Opening text files
    negTxtFile = open('dataFiles/test/testNeg.txt',newline='',encoding='latin-1')
    posTxtFile = open('dataFiles/test/testPos.txt',newline='',encoding='latin-1')
    
    #For each line in the negative text file
    for line in negTxtFile:
            #Split string into individual words
            negWords = re.findall(r'\w+', line)
            #Add words to the set
            for negWord in negWords:
                vocabulary.add(negWord)
            

    #For each line in the positive text file
    for line in posTxtFile:
            #Split string into individual words
            posWords = re.findall(r'\w+', line)
            #Add words to the set
            for posWord in posWords:
                vocabulary.add(posWord)
                
                
#--------------------------------------------           
#   STORING ALL UNIQUE WORDS IN A SET
#-------------------------------------------- 
def storeAllUniqueWordsWithoutFilter():
    
    #Accessing global variables
    global vocabularyTwo
    
    #Opening text files
    negTxtFile = open('dataFiles/test/testNeg.txt',newline='',encoding='latin-1')
    posTxtFile = open('dataFiles/test/testPos.txt',newline='',encoding='latin-1')
    
    #For each line in the negative text file
    for line in negTxtFile:
            #Split string into individual words
            l = negTxtFile.readline()
            negWords = l.split()
            
            #Add words to the set
            for negWord in negWords:
                vocabularyTwo.add(negWord)
            

    #For each line in the positive text file
    for line in posTxtFile:
            #Split string into individual words
            l = posTxtFile.readline()
            posWords = l.split()
            #Add words to the set
            for posWord in posWords:
                vocabularyTwo.add(posWord)

#--------------------------------------------           
#       RECORDING FREQUENCY OF WORDS
#-------------------------------------------- 
def recordFrequencyOfWords():
    
    #Accessing global variables
    global vocabulary
    global posDict
    global negDict
   
    #Opening text files
    negTxtFile = open('dataFiles/test/testNeg.txt',newline='',encoding='latin-1')
    posTxtFile = open('dataFiles/test/testPos.txt',newline='',encoding='latin-1')
    
    #Putting all unique words into both dictionaries 
    posDict = dict.fromkeys(vocabulary,0)
    negDict = dict.fromkeys(vocabulary,0)
    
    #For each line in the negative text file
    for line in negTxtFile:
            #Split string into individual words
            negWords = re.findall(r'\w+', line)
            #Add words to the set
            for negWord in negWords:
                if negWord in negDict:
                    negDict[negWord]+=1

    #For each line in the positive text file
    for line in posTxtFile:
            #Split string into individual words
            posWords = re.findall(r'\w+', line)
            #Add words to the set
            for posWord in posWords:
                if posWord in posDict:
                    posDict[posWord]+=1
            
    #For each word  in the vocabulaary      
    for eachWord in vocabulary:
        
        negFreq = negDict.get(eachWord)
        print(eachWord, " in neg dict frequency", negFreq)
            
        posFreq = posDict.get(eachWord)
        print(eachWord, " in pos dict frequency", posFreq)
            
        print("")   
        

#--------------------------------------------           
#       RECORDING FREQUENCY OF WORDS
#-------------------------------------------- 
def recordFrequencyOfWordsWithoutFilter():
    
    #Accessing global variables
    global vocabularyTwo
    global posDictTwo
    global negDictTwo
   
    #Opening text files
    negTxtFile = open('dataFiles/test/testNeg.txt',newline='',encoding='latin-1')
    posTxtFile = open('dataFiles/test/testPos.txt',newline='',encoding='latin-1')
    
    #Putting all unique words into both dictionaries 
    posDictTwo = dict.fromkeys(vocabularyTwo,0)
    negDictTwo = dict.fromkeys(vocabularyTwo,0)
    
    #For each line in the negative text file
    for line in negTxtFile:
            #Split string into individual words
            l = negTxtFile.readline()
            negWords = l.split()
            #Add words to the set
            for negWord in negWords:
                if negWord in negDict:
                    negDictTwo[negWord]+=1

    #For each line in the positive text file
    for line in posTxtFile:
            #Split string into individual words
            l = posTxtFile.readline()
            posWords = l.split()
            #Add words to the set
            for posWord in posWords:
                if posWord in posDict:
                    posDictTwo[posWord]+=1
            
    #For each word  in the vocabulaary      
    for eachWord in vocabulary:
        
        negFreq = negDictTwo.get(eachWord)
        #print(eachWord, " in neg dict frequency", negFreq)
            
        posFreq = posDictTwo.get(eachWord)
        #print(eachWord, " in pos dict frequency", posFreq)
            
        #print("")  
    
#--------------------------------------------           
#      CALCULATING WORD PROBABILITY
#-------------------------------------------- 
def calculateWordProbability():
    
    #Setting panda configurations
    pd.set_option('display.max_rows',30)
    pd.set_option('display.expand_frame_repr', False)
    #pd.set_option('display.max_columns', 7)
    
    #Getting acccess to dictionaries
    global posDict
    global negDict
    global bothDataFrame
    
    #Creating data frames 
    negDataFrame = pd.DataFrame(list(negDict.items()), columns=['Word', 'Neg Frequency'])
    posDataFrame = pd.DataFrame(list(posDict.items()), columns=['Word', 'Pos Frequency'])
    
    #Merging data frames into one, to show both frequencies
    bothDataFrame = pd.merge(negDataFrame,posDataFrame,on="Word")
    
    #Adding coloumn for total frequencies
    bothDataFrame["Total Freq"] = bothDataFrame['Neg Frequency'] + bothDataFrame['Pos Frequency']
   
    #Adding column for negative probability
    bothDataFrame["Neg Probability"] = bothDataFrame['Neg Frequency'] / bothDataFrame["Total Freq"]
    
    #Adding column for positive probability
    bothDataFrame["Pos Probability"] = bothDataFrame['Pos Frequency'] / bothDataFrame["Total Freq"]
  
    #Printing dataframe 
    print(bothDataFrame)
    
#--------------------------------------------           
#      CALCULATING WORD PROBABILITY
#-------------------------------------------- 
def calculateWordProbabilityWithoutFilter():
    
    #Setting panda configurations
    pd.set_option('display.max_rows',30)
    pd.set_option('display.expand_frame_repr', False)
    #pd.set_option('display.max_columns', 7)
    
    #Getting acccess to dictionaries
    global posDictTwo
    global negDictTwo
    global bothDataFrameTwo
    
    #Creating data frames 
    negDataFrame = pd.DataFrame(list(negDictTwo.items()), columns=['Word', 'Neg Frequency'])
    posDataFrame = pd.DataFrame(list(posDictTwo.items()), columns=['Word', 'Pos Frequency'])
    
    #Merging data frames into one, to show both frequencies
    bothDataFrameTwo = pd.merge(negDataFrame,posDataFrame,on="Word")
    
    #Adding coloumn for total frequencies
    bothDataFrameTwo["Total Freq"] = bothDataFrameTwo['Neg Frequency'] + bothDataFrameTwo['Pos Frequency']
   
    #Adding column for negative probability
    bothDataFrameTwo["Neg Probability"] = bothDataFrameTwo['Neg Frequency'] / bothDataFrameTwo["Total Freq"]
    
    #Adding column for positive probability
    bothDataFrameTwo["Pos Probability"] = bothDataFrameTwo['Pos Frequency'] / bothDataFrameTwo["Total Freq"]
  
    #Printing dataframe 
    print(bothDataFrameTwo)
    
   

#--------------------------------------------           
#      CALCULATING WORD PROBABILITY
#-------------------------------------------- 
def classifyingUnseenTweets():
    
    #Asking user for tweet
    newTweet = input('Enter a tweet:')

    #Creating a dictionary to store each tweets word as key, and value will be 1 if that word is more positive, 0 if more negative
    tweetDict = dict()
        
    #Accessing global dataframe
    global bothDataFrame
    
    #Splitting tweet into words
    words = newTweet.split()
    
    #Setting keys from array
    tweetDict = dict.fromkeys(words,0)
    
    #Going through the keys(words) and values in tweet dictionary
    for key,value in tweetDict.items():
        try:
           #Gets the neg prob and pos prob for that word
           wordPosProb = bothDataFrame.loc[bothDataFrame.Word==key,'Pos Probability'].values[0]
           wordNegProb = bothDataFrame.loc[bothDataFrame.Word==key,'Neg Probability'].values[0]
  
           #If word is more negative
           if  wordPosProb < wordNegProb:
               tweetDict[key] = "neg"
           #If word is more positive   
           elif wordPosProb > wordNegProb:
               tweetDict[key] = "pos"
           #If they are even    
           elif wordNegProb == wordPosProb:
               tweetDict[key] = "even"
             
        except:
            print("the word isnt there")
       
    #Printing dictionary
    print(tweetDict)
    
    #Count of neg,pos, even count    
    countDict = {"pos":0,"neg":0,"even":0}
    
    #Counts the number of positive,negative, and even words in the tweet given
    for key,value in tweetDict.items():
        #If word is neg, add one
        if value == "neg":
            countDict["neg"] += 1
        #If word is pos, add one
        elif value == "pos":
            countDict["pos"] += 1
        #If word is even, add one
        elif value == "even":
            countDict["even"] += 1
            
    #Getting outcome by getting max values
    outcome = max(countDict, key=countDict.get)
    
    #Printing out outcome
    print("This tweet is ",outcome)
        
    
#--------------------------------------------           
#      CALCULATING WORD PROBABILITY
#-------------------------------------------- 
def classifyingUnseenTweetsTest(txtFile,name,time):
    
    #Accessing global variables
    global bothDataFrame
    global numNegTweetsBefore
    global numPosTweetsBefore
    global numNegTweetsAfter
    global numPosTweetsAfter
    
    
    # *** IF TIME IS BEFORE ***
    if time == 'before':
        
        testPosCount = 0
        testNegCount = 0
        totalLength = 0
        
        #For each line in the negative text file
        for lines in txtFile:
            
            #Reading line with filter
            theLine = re.findall(r'\w+', lines)
         
            #Setting keys from array
            tweetDic = dict.fromkeys(theLine,0)
        
            #Going through the keys(words) and values in tweet dictionary
            for key,value in tweetDic.items():
                
                try:
                    #Gets the neg prob and pos prob for that word
                    wordPosProb = bothDataFrame.loc[bothDataFrame.Word==key,'Pos Probability'].values[0]
                    wordNegProb = bothDataFrame.loc[bothDataFrame.Word==key,'Neg Probability'].values[0]
                  
                    #If word is more negative
                    if  wordPosProb < wordNegProb:    
                        tweetDic[key] = "neg"
                    #If word is more positive   
                    elif wordPosProb > wordNegProb:
                        tweetDic[key] = "pos"
                    #If they are even    
                    elif wordNegProb == wordPosProb:
                        tweetDic[key] = "even"
                except:
                    print("the word isnt there")
           
          
                #Printing dictionary
                #print(tweetDic)
        
            #Count of neg,pos, even count    
            countDict = {"pos":0,"neg":0,"even":0}
        
            #Counts the number of positive,negative, and even words in the tweet given
            for key,value in tweetDic.items():
                #If word is neg, add one
                if value == "neg":
                    countDict["neg"] += 1
                #If word is pos, add one
                elif value == "pos":
                    countDict["pos"] += 1
                #If word is even, add one
                elif value == "even":
                    countDict["even"] += 1
                
            #Getting outcome by getting max values
            outcome = max(countDict, key=countDict.get)
        
            #Printing out outcome
#            print("----------------------------------------")
#            print(lines)
#            print("This tweet is: ",outcome)
#            print("----------------------------------------")
            
            #Calculating number of tweets
           
            if outcome == 'pos':
                testPosCount += 1
                
            if(outcome == 'neg'):
                testNegCount += 1
                
            totalLength += 1
        
        #Printing total number of pos tweets
        print("Total number of positive tweets in the ",name," file is: ", testPosCount)
        
        #Printing total number of neg tweets
        print("Total number of negative tweets in the ",name," file is: ", testNegCount)
      
        #Setting global variables to pass to graph function
        if name == 'Negative':
           numNegTweetsBefore = testNegCount 
        elif name == 'Positive':
            numPosTweetsBefore = testPosCount
        
    
    
    # *** IF TIME IS AFTER ***
    elif time == 'after':  
        
        testPosCount = 0
        testNegCount = 0
        totalLength = 0
        
        #For each line in the negative text file
        for lines in txtFile:
            
            #Reading line without filter
            theLine = txtFile.readline()
            theLine = theLine.split()
            
            #Setting keys from array
            tweetDic = dict.fromkeys(theLine,0)
        
            #Going through the keys(words) and values in tweet dictionary
            for key,value in tweetDic.items():
                
                try:
                    #Gets the neg prob and pos prob for that word
                    wordPosProb = bothDataFrameTwo.loc[bothDataFrameTwo.Word==key,'Pos Probability'].values[0]
                    wordNegProb = bothDataFrameTwo.loc[bothDataFrameTwo.Word==key,'Neg Probability'].values[0]
                  
                    #If word is more negative
                    if  wordPosProb < wordNegProb:    
                        tweetDic[key] = "neg"
                    #If word is more positive   
                    elif wordPosProb > wordNegProb:
                        tweetDic[key] = "pos"
                    #If they are even    
                    elif wordNegProb == wordPosProb:
                        tweetDic[key] = "even"
                except:
                    print("the word isnt there1")
          
                #Printing dictionary
                #print(tweetDic)
        
            #Count of neg,pos, even count    
            countDict = {"pos":0,"neg":0,"even":0}
        
            #Counts the number of positive,negative, and even words in the tweet given
            for key,value in tweetDic.items():
                #If word is neg, add one
                if value == "neg":
                    countDict["neg"] += 1
                #If word is pos, add one
                elif value == "pos":
                    countDict["pos"] += 1
                #If word is even, add one
                elif value == "even":
                    countDict["even"] += 1
                
            #Getting outcome by getting max values
            outcome = max(countDict, key=countDict.get)
        
            #Printing out outcome
#            print("----------------------------------------")
#            print(lines)
#            print("This tweet is: ",outcome)
#            print("----------------------------------------")
            
            #Calculating number of tweets
           
            if outcome == 'pos':
                testPosCount += 1
                
            if(outcome == 'neg'):
                testNegCount += 1
                
            totalLength += 1
        
        #Printing total number of pos tweets
        print("Total number of positive tweets in the ",name," file is: ", testPosCount)
        
        #Printing total number of neg tweets
        print("Total number of negative tweets in the ",name," file is: ", testNegCount)
      
        #Setting global variables to pass to graph function
        if name == 'Negative':
            numNegTweetsAfter = testNegCount
        elif name == 'Positive':
            numPosTweetsAfter = testPosCount
           
    
    
#--------------------------------------------           
#            VISUALIZATION
#-------------------------------------------- 
def visualization():
    
    #SHOW RESULTS BEFORE YOU TAKE OUT THE @ SYMBOLS AND STUFF
    global bothDataFrame

    global numNegTweetsBefore
    global numPosTweetsBefore

    global numNegTweetsAfter
    global numPosTweetsAfter
    
    print("pos before :" ,numPosTweetsBefore," , pos after: " ,numPosTweetsAfter)
    print("neg before :" ,numNegTweetsBefore," , neg after: " ,numNegTweetsAfter)
    
    numLines = 1000
    
   # Make a fake dataset:
    height = [numPosTweetsBefore, numNegTweetsBefore, numPosTweetsAfter, numNegTweetsAfter]
    bars = ('pos before', 'neg before', 'pos after', 'neg after')
    y_pos = np.arange(len(bars))
     
    # Create bars
    plt.bar(y_pos, height)
    plt.ylim(0, 1000)
     
    # Create names on the x-axis
    plt.xticks(y_pos, bars)
     
    # Show graphic
    plt.show()

    
    
start()
