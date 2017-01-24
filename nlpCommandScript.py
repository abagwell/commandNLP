#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

cwd = os.getcwd()
gameVerbs = ["look", "take", "help", "inventory", "use", 
		"drop", "eat", "drink", "pull", "hit", "put", 
		"savegame", "loadgame", "push", "wield", "wear"]

prepositions = ["above", "at", "behind", "into", "on", "under", "with" ]

'''
verbPrepositionCombos = {'look':['at', 'under', 'above', 'into', 'behind'], 'take': [], 
						'help': [], 'inventory': [], 'use': ['on', 'with'], 'drop' : [], 'eat': [],
						'drink':[], 'pull': [], 'hit': [], 'put': [], 'hit': [], 'put': ['on', 'into', 'under', 'above', 'with'],
						'push': ['on'], 'wield': [], 'wear': [],}
'''
verbPrepositionCombos = {gameVerbs[0]:['at', 'under', 'above', 'into', 'behind'], gameVerbs[1]: [], 
						gameVerbs[2]:[], gameVerbs[3]: [], gameVerbs[4]: ['on', 'with'], gameVerbs[5] : [], gameVerbs[6]: [],
						gameVerbs[7]:[], gameVerbs[8]: [], gameVerbs[9]: [], gameVerbs[10]: [], gameVerbs[11]: [], gameVerbs[12]: ['on', 'into', 'under', 'above', 'with'],
						gameVerbs[13]: ['on'], gameVerbs[14]: [], gameVerbs[15]: [],}
synonymsDictionary = {}

'''

Definition:

'''

def buildSynonymDict():

	
	synonymFilePath = cwd + "/synonymFile.txt" #file source: https://justenglish.me/2014/04/18/synonyms-for-the-96-most-commonly-used-words-in-english/
	

	with open(synonymFilePath, 'r') as f:
		for line in f:
			verb, synonymList= line.split('—', 2)
			verb = verb.lower()
			verb = verb.strip(' \t\n\r')
			parsedSynonyms = synonymList.split(",")
			for word in parsedSynonyms:
				word = word.strip(' \t\n\r')
				synonymsDictionary[word] = verb



def parseCommand(commandString):
	parsedCommand = commandString.split()

'''

Definition: takes the command string entered by the user. It then tokenizes that input. Next, it performs
the processes that input: 

'''


def buildTuple(commandString):

	tupleReturned = ()

	#get tokens
	#perform analysis
		#get the verb, check to see if it exists in gameVerbs, if it doesn't look in synDic, If yes, match it, if no, exit
		#get the preposition, check to see if exists. if it doesn't look in synonyms, if it doesn't exit, if it does
		#look to see if the verb preposition combo is valid, if it is continue, if not return
		#get the object 
		# return tuple

	#if can't build 
	#return tuple


def main():
	
	buildSynonymDict()
	commandTuple = ()
	while not all(commandTuple):
		command = input("Your move: ")
		commandTuple = buildTuple(commandString)
	print commandTuple

	

if __name__ == '__main__':
	main()