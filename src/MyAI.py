# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

from AI import AI
from Action import Action
import random
from copy import deepcopy

class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
		self.__rowDimension = rowDimension
		self.__colDimension = colDimension
		self.__totalMines = totalMines
		self.__moveCount = 0
		self.__repeatMove = 0
		self.__flaggedMines = []
		self.__toUncover = []
		self.__uncovered = []
		self.__possibleMine = []
		self.__nearMine = []
		self.__guessMine = []
		self.__numberDict = {}
		self.__blankDict = {}
		self.__allFounded = False
		self.e = [startX, startY]

		########################################################################
		#							YOUR CODE ENDS							   # 
		########################################################################

	def getAction(self, number: int) -> "Action Object":
		if len(self.__flaggedMines) == self.__totalMines:
			if not self.__allFounded:
				for y in range(self.__rowDimension):
					for x in range(self.__colDimension):
						if self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
							self.__toUncover.append([x,y])
				self.__allFounded = True
			else:
				while self.__toUncover:
					self.e = self.__toUncover.pop()
					self.__uncovered.append(self.e)
					action = AI.Action.UNCOVER
					self.__moveCount += 1
					return Action(action, self.e[0], self.e[1])
		if self.__moveCount == self.__colDimension * self.__rowDimension - self.__totalMines:
			#print("mine founded")
			return Action(AI.Action.LEAVE)
		if self.__moveCount == 0:
			self.__uncovered.append(self.e)
			for y in range(self.e[1] - 1, self.e[1] + 2):
				if y in range(self.__rowDimension):
					for x in range(self.e[0] - 1, self.e[0] + 2):
						if x in range(self.__colDimension):
							if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0:
									self.__toUncover.append([x,y])
		if number == 0:
			for y in range(self.e[1] - 1, self.e[1] + 2):
				if y in range(self.__rowDimension):
					for x in range(self.e[0] - 1, self.e[0] + 2):
						if x in range(self.__colDimension):
							if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0:
									self.__toUncover.append([x,y])
		elif number > 0:
			mineCount = 0
			blankCount = 0
			blank = []
			for y in range(self.e[1] - 1, self.e[1] + 2):
				if y in range(self.__rowDimension):
					for x in range(self.e[0] - 1, self.e[0] + 2):
						if x in range(self.__colDimension):
							if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
								blank.append([x,y]);
								blankCount += 1
							if self.__possibleMine.count([x,y]):
								mineCount += 1
			#print(self.e, mineCount, blankCount, number)
			if blankCount + mineCount == number:
				for y in range(self.e[1] - 1, self.e[1] + 2):
					if y in range(self.__rowDimension):
						for x in range(self.e[0] - 1, self.e[0] + 2):
							if x in range(self.__colDimension):
								if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
									self.__possibleMine.append([x,y])
			elif mineCount == number:
				for y in range(self.e[1] - 1, self.e[1] + 2):
					if y in range(self.__rowDimension):
						for x in range(self.e[0] - 1, self.e[0] + 2):
							if x in range(self.__colDimension):
								if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
									self.__toUncover.append([x,y])
			else:
				self.__nearMine.append(self.e)
				self.__numberDict[self.e[0]*1000 + self.e[1]] = number
				self.__blankDict[self.e[0]*1000 + self.e[1]] = blank
		#print("toUn ", self.__toUncover)
		#print("unco ",self.__uncovered)
		#print("nearmine ",self.__nearMine)
		#print("possMine ", self.__possibleMine)
		#print("flagged ", self.__flaggedMines)
		while self.__toUncover:
			self.e = self.__toUncover.pop()
			self.__uncovered.append(self.e)
			action = AI.Action.UNCOVER
			self.__moveCount += 1
			return Action(action, self.e[0], self.e[1])
		while self.__nearMine:
			self.e = self.__nearMine.pop(0)
			#print(self.e, " near mine")
			mineCount = 0
			blankCount = 0
			blank = []
			for y in range(self.e[1] - 1, self.e[1] + 2):
				if y in range(self.__rowDimension):
					for x in range(self.e[0] - 1, self.e[0] + 2):
						if x in range(self.__colDimension):
							if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
								blank.append([x,y]);
								blankCount += 1
							if self.__possibleMine.count([x,y]):
								mineCount += 1
			#print(self.e, mineCount, blankCount, self.__numberDict[self.e[0]*1000 + self.e[1]])
			if blankCount + mineCount == self.__numberDict[self.e[0]*1000 + self.e[1]]:
				for y in range(self.e[1] - 1, self.e[1] + 2):
					if y in range(self.__rowDimension):
						for x in range(self.e[0] - 1, self.e[0] + 2):
							if x in range(self.__colDimension):
								if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
									self.__possibleMine.append([x,y])
				self.__repeatMove = 0
				self.e = min(self.__possibleMine)
				for m in self.__possibleMine:
					if m not in self.__flaggedMines:
						self.e = m
						self.__flaggedMines.append(m)
						break
				action = AI.Action.FLAG
				return Action(action, self.e[0], self.e[1])
			elif mineCount == self.__numberDict[self.e[0]*1000 + self.e[1]]:
				for y in range(self.e[1] - 1, self.e[1] + 2):
					if y in range(self.__rowDimension):
						for x in range(self.e[0] - 1, self.e[0] + 2):
							if x in range(self.__colDimension):
								if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
									self.__toUncover.append([x,y])
				self.__repeatMove = 0
				break
			else:
				self.__nearMine.append(self.e)
				self.__blankDict[self.e[0]*1000 + self.e[1]] = blank
				self.__repeatMove += 1
			#print(self.__repeatMove, self.__nearMine)
			if self.__repeatMove > len(self.__nearMine) + 5:
				length = len(self.__nearMine)
				for i in range(0, length):
					for j in range(i+1, length):
						mine1 = deepcopy(self.__blankDict[self.__nearMine[i][0]*1000 + self.__nearMine[i][1]])
						mine2 = deepcopy(self.__blankDict[self.__nearMine[j][0]*1000 + self.__nearMine[j][1]])
						count1 = deepcopy(self.__numberDict[self.__nearMine[i][0]*1000 + self.__nearMine[i][1]])
						count2 = deepcopy(self.__numberDict[self.__nearMine[j][0]*1000 + self.__nearMine[j][1]])
						#print(count1, count2)
						for y in range(self.__nearMine[i][1] - 1, self.__nearMine[i][1] + 2):
							if y in range(self.__rowDimension):
								for x in range(self.__nearMine[i][0] - 1, self.__nearMine[i][0] + 2):
									if x in range(self.__colDimension):
										if self.__possibleMine.count([x,y]):
											count1 -= 1
											#print([x,y])
						for y in range(self.__nearMine[j][1] - 1, self.__nearMine[j][1] + 2):
							if y in range(self.__rowDimension):
								for x in range(self.__nearMine[j][0] - 1, self.__nearMine[j][0] + 2):
									if x in range(self.__colDimension):
										if self.__possibleMine.count([x,y]):
											count2 -= 1
											#print([x,y])
						#print(self.__nearMine[i], count1, mine1)
						#print(self.__nearMine[j], count2, mine2)
						templist1 = [item for item in mine1 if item not in mine2]
						templist2 = [item for item in mine2 if item not in mine1]
						if len(templist1) == 0:
							if count1 == count2:
								for t in templist2:
									if self.__toUncover.count(t) == 0 and self.__possibleMine.count(t) == 0:
										self.__toUncover.append(t)
									#print("2 add")
							elif count2 - count1 == len(templist2):
								for t in templist2:
									self.__possibleMine.append(t)
									blank = []
									for y in range(self.__nearMine[i][1] - 1, self.__nearMine[i][1] + 2):
										if y in range(self.__rowDimension):
											for x in range(self.__nearMine[i][0] - 1, self.__nearMine[i][0] + 2):
												if x in range(self.__colDimension):
													if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
														blank.append([x,y]);
									self.__blankDict[self.__nearMine[i][0]*1000 + self.__nearMine[i][1]] = blank
						if len(templist2) == 0:
							if count1 == count2:
								for t in templist1:
									if self.__toUncover.count(t) == 0 and self.__possibleMine.count(t) == 0:
										self.__toUncover.append(t)
									#print("1 add")
							elif count1 - count2 == len(templist1):
								for t in templist1:
									self.__possibleMine.append(t)
									blank = []
									for y in range(self.__nearMine[j][1] - 1, self.__nearMine[j][1] + 2):
										if y in range(self.__rowDimension):
											for x in range(self.__nearMine[j][0] - 1, self.__nearMine[j][0] + 2):
												if x in range(self.__colDimension):
													if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
														blank.append([x,y]);
									self.__blankDict[self.__nearMine[i][0]*1000 + self.__nearMine[i][1]] = blank
						if len(templist1) == 1 and len(templist2) == 1:
							#print(templist1, templist2)
							if count1 - count2 == 1:
								#print("1 mine 2 tounc")
								if self.__toUncover.count(templist2[0]) == 0 and self.__possibleMine.count(templist2[0]) == 0:
									self.__toUncover.append(templist2[0])
								self.__possibleMine.append(templist1[0])
								blank = []
								for y in range(self.__nearMine[i][1] - 1, self.__nearMine[i][1] + 2):
									if y in range(self.__rowDimension):
										for x in range(self.__nearMine[i][0] - 1, self.__nearMine[i][0] + 2):
											if x in range(self.__colDimension):
												if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
													blank.append([x,y]);
								self.__blankDict[self.__nearMine[i][0]*1000 + self.__nearMine[i][1]] = blank
							if count2 - count1 == 1:
								#print("2 mine 1 tounc")
								if self.__toUncover.count(templist1[0]) == 0 and self.__possibleMine.count(templist1[0]) == 0:
									self.__toUncover.append(templist1[0])
								self.__possibleMine.append(templist2[0])
								blank = []
								for y in range(self.__nearMine[j][1] - 1, self.__nearMine[j][1] + 2):
									if y in range(self.__rowDimension):
										for x in range(self.__nearMine[j][0] - 1, self.__nearMine[j][0] + 2):
											if x in range(self.__colDimension):
												if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
													blank.append([x,y]);
								self.__blankDict[self.__nearMine[j][0]*1000 + self.__nearMine[j][1]] = blank
				#print(self.__toUncover)
				if self.__toUncover:
					self.__repeatMove = 0
					break
				if len(self.__possibleMine) != len(self.__flaggedMines):
					self.__repeatMove = 0
					self.e = min(self.__possibleMine)
					for m in self.__possibleMine:
						if m not in self.__flaggedMines:
							self.e = m
							self.__flaggedMines.append(m)
							break
					action = AI.Action.FLAG
					return Action(action, self.e[0], self.e[1])
				#for i in range(0, length):
				#	for j in range(i+1, length):
				#		for k in range(j+1, length):


				self.__repeatMove = 0
				self.__guessMine = []
				for y in range(self.__rowDimension):
					for x in range(self.__colDimension):
						if self.__toUncover.count([x,y]) == 0 and self.__uncovered.count([x,y]) == 0 and self.__possibleMine.count([x,y]) == 0:
							self.__guessMine.append([x,y])
				self.e = random.choice(self.__guessMine)
				#print("guess on ",self.e)
				self.__uncovered.append(self.e)
				action = AI.Action.UNCOVER
				self.__moveCount += 1
				return Action(action, self.e[0], self.e[1])
		while self.__toUncover:
			self.e = self.__toUncover.pop()
			self.__uncovered.append(self.e)
			action = AI.Action.UNCOVER
			self.__moveCount += 1
			#print("unco")
			return Action(action, self.e[0], self.e[1])
		return Action(AI.Action.LEAVE)

		
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
