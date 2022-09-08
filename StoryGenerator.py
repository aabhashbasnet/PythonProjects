# Story Generator 
import random
starting = ['Few years ago', 'Yesterday', 'Once Upon a time', 'Last Friday','In the jungle']
subject = ['an old man','a white rabbit','a beautiful couple','a one eyed rhino']
name_of_subject = ['ram','hawk', 'Peter','Tom']
incident = ['was running', 'was sitting still','is being chased']
ending = ["died","lived happily","roamed here and there"]
print(random.choice(starting) +', '+random.choice(subject) + " named " + random.choice(name_of_subject)+ " " +random.choice(incident) + " and "+ random.choice(ending))
