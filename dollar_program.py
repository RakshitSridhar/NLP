# HW 2- Regular Expressions
#By Rakshit Sridhar

import re
import sys

with open ('test_dollar_phone_corpus.txt', 'r') as input:
    text_content= input.read()
    
dollar_pattern =re.compile('|'.join([r'([$][0-9\.\,]+(thousand|million|billion|trillion)?)|(\s*[A-Z]*[a-z]+\s+(dollars|cents))|(a dollar)'
 ]), re.IGNORECASE)
    
dollar_matches= dollar_pattern.findall(text_content)

with open('dollar_output.txt', 'w') as output_dollar:
    for match in dollar_matches:
        dollar_amounts = ''.join(filter(None, match))
        if dollar_amounts:
            output_dollar.write(dollar_amounts+'\n')

    
