import sys



import pygame

from pygame.locals import QUIT



UserName = input('please type your full government official name: ')
userAnswer = None;
score = 0;

Q1 = "How much bigger would our sun need to be to turn into a black hole: \n a) 20 to 30 times larger \n b) 10 to 20 times larger \n c) 30 to 40 times larger \n d) 40 to 50 times larger"
Q2 = "What is the closest estimate for the number of galaxies in the observable universe? \n a) 1-2 million \n b) 2 trillion+ \n c) 3-4 billion \n d) 6 billion"
Q3 = "What is the densest part of a black hole called: \n a) Tipping point \n b) Singularity \n c) Accretion Disk \n d) Event Horizon"
Q4 = "What type of galaxy is our galaxy, the Milky Way? a - Elliptical Galaxy b - Irregular Galaxy c - Lenticular Galaxy d - Spiral Galaxy"
Q5 = "Did Einstien believe in black holes: \n a) No, no one in his time period thought they could exist \n b) Yes, he spent the rest of his life trying to prove their existence \n c) No, his work suggested their existence but he spent his life trying to disprove them \n d) Yes, he was so convinced of their existence he was cast out of the scientific community "
Q6 = "Around how many stars are contained in a galaxy? \n a)200,000-300,000 \n b) 500,000-1,000,000 \n c) 2,000,000-3,000,000 \n d) 1,000,000 - 1 trillion"
Q7 = "A supernova is when a star explodes and dies and in the process spews every possible element out of it in a colorful death: \n a) true \n b) false"
Q8 = "How many years after the supposed creation of the universe were galaxies formed? \n a) 1 million \n b) 10 million \n c) 400 million \n d) 1 billion"
Q9 = "Black holes with no accretion disk cannot be seen: \n a) true \n b) false"
Q10 = "What is a feature of a light blue star? \n a) contains metals \n b) has a termperature of 6,000-7,000 K \n c) contains helium and some hydrogen \n d) contains calcium"

questionList = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]



class Question:

	def __init__ (self, prompt, response):

		self.prompt = prompt

		self.response = response


questions = {
  questionList[0]: "a",
  questionList[1]: "b",
  questionList[2]: 'c',
  questionList[3]: 'd',
  questionList[4]: 'c',
  questionList[5]: 'd',
  questionList[6]: 'a',
  questionList[7]: 'c',
  questionList[8]: 'a',
  questionList[9]: 'c'
}

'''

query_List = [

	Question(questionList[0], 'a'),

  Question(questionList[1], 'b'),

  Question(questionList[2], 'c'),

  Question(questionList[3], 'd'),

  Question(questionList[4], 'a')]'''





def Score(i):
  if userAnswer == questions[questionList[i]]:
    score += 1
  print(score)

for key in questions:
  userAnswer = input("What do you think is the answer? Please type in lowercase with no extra spaces: " + key)
  Score(key)




