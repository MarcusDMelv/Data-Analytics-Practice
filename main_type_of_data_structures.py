"""print('hello world')
greet = 'hello world'

print(greet.title())
print(greet.upper())
print(greet.isdigit())
print(greet.islower())
greet = greet.title()
print(greet)
greet = greet.upper()
print(greet)
# list -> square brackets
greet_list = ['Hello','World', 'I', 'Am','A','List']
greet_list.append('Wooo')

print(greet_list)
# tuples -> not modifiedable -> parethesis
greet_tuple = ('Hello','World')
# Dictionaries -> Curly Brackets
greet_dict = {'lattitude':4065.76,
              'longittude': -678.8}
#edit dictionaries
greet_dict['lattitude'] = 40.56

bigbro = input('What is your brothers name:\n')
bigbroNumber = input('\n\tNumber:')
phonebook = {'Marcus':6028103704,
             bigbro: bigbroNumber}

print(phonebook)

import  time
for x in greet_list:
    time.sleep(2)
    print(x)
greet_list.append('Oh yea! I am really about that life you know what I am saying?')
for x in greet_list:
    time.sleep(2)
    print(len(x),x)
"""


class practice:
    
    def list(self):
        # square brackets
        new_list = ['apples', 'strawberries', 'grapes', 'pears']
        # go through list
        for item in new_list:
            item = item.title()
            print(item)
        # add to list
        new_list.append('chocolate')
        print(new_list)
        # remove from list
        new_list.remove('chocolate')
        print(new_list)

    def tuple(self):
        # tuple cannot be modified ( more secured )
        # uses ( )
        new_tuple = (('email', '@email.com'),
                     ('password', 'fhjjh$#'))
        print(new_tuple)

    def dictionaries(self):
        # curly brackets
        new_dict = {
            'email': '@email.com',
            'password': '#jflerke#$$fl'
        }
        print(new_dict)


practice = practice()
practice.list()
practice.tuple()
practice.dictionaries()
