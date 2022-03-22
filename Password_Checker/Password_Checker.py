# uses python 2.7.17
# compatible with 3.x
'''
Rules:
    * 8 to 32 characters
    * at least one numeric digit
    * at least one uppercase letter
    * at least one lowercase letter
    * at least one symbol from the set ~!@#$%^&*
    * must not have other characters than the above
    * starting character must not be a number
Sample passwords are in password.txt
'''

import sys
print(sys.version)
# create the pass checking function
import re
def pass_checker():

    # create password.txt file and make it appendable
    with open ("password.txt", "a+") as passwords:
        # read line-by-line
        lines = passwords.readlines()
        # truth functions for the checking below
        upper = lambda x: 1 if re.search(r'[A-Z]',x) else 0
        lower = lambda x: 1 if re.search(r'[a-z]',x) else 0
        symbols = lambda x: 1 if re.search(r'[~!@#$%^&*]',x) else 0
        numbers = lambda x: 1 if re.search(r'[0-9]',x) else 0

        invalid_words = [] # this will help prevent output duplicates

        #goes line-by-line in the password.txt file
        for line in lines:
            pw = line.strip() # removes whitespace for each password (does \n for everything otherwise)
            total = upper(pw)+lower(pw)+symbols(pw)+numbers(pw)

            # point system to check the password against the password criteria
            if total != 4:
                if pw not in invalid_words:
                    print('NO {}'.format(pw))
                    invalid_words.append(pw)
                else:
                    continue
            if pw[0] in r'[0-9]':
                if pw not in invalid_words:
                    print('NO {}'.format(pw))
                    invalid_words.append(pw)
                else:
                    continue
            for i in pw:
                if pw not in invalid_words:
                    if not re.search(r'[a-zA-Z0-9~!@#$%^&*]',i):
                        print("NO {}".format(pw))
                        invalid_words.append(pw)
                else:
                    continue
            if not re.search(r'[a-zA-Z0-9~!@#$%^&*]',i):
                if not 8 <= len(pw) <= 32:
                    print('NO {}'.format(pw))
        #print(invalid_words) uncomment to check all words that were invalid
            
                

            

                   
                


pass_checker()
