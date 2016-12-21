import random

subjects = ["You"]
s_verbs = ["are"]
adjectives = ["beautiful", "radiant", "intelligent", "generous", "kind", "compassionate", "charming", 
"fearless", "honest", "great", "determined", "dependable", "modest", "patient", "polite", "rational",
"loving", "loyal", "understanding", "warmhearted", "thoughtful"]
puncuation_marks = [".", "!"]
words = [subjects, s_verbs, adjectives]

#Using a nested list, randomly pick from 'words' and concatenate them together.
def compliment():
	choices = [random.choice(group) for group in words]
	puncuation = random.choice(puncuation_marks)
	print(' '.join(choices) + puncuation)

compliment()
