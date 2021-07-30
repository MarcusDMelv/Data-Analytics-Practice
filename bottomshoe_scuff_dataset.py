"""
Ranking


"""
from sklearn import tree
import sys
from PIL import Image
import time

# training data
# features='[[btm_shoe,scuff,fade]]
# labels = [['Not used','Excellent Used','Very Used','Really Used']]
features = [[100, 0, 0], [97, 5, 7], [85, 8, 10], [75, 8, 20], [78, 10, 30]]
labels = [['New'], ['Excellent Used'], ['Very Used'], ['Really Used'], ['Too Used']]

shoe_classifier = tree.DecisionTreeClassifier()
shoe_classifier = shoe_classifier.fit(features,labels)

running = True

out = 'exit'

print('Start program')

while running:
    btm_shoe = input('Bottom Of Shoe:')
    btm_shoe = btm_shoe.lower()
    if btm_shoe == 'exit':
        running = False
    else:
        #time.sleep()
        scuff = input('Scuff:')
        #time.sleep()
        fade = input('Fade: ')
        print(shoe_classifier.predict([[btm_shoe,scuff,fade]]))
    print('Goodbye!')