# HW 2- Regular Expressions
#By Rakshit Sridhar

import re
import sys

with open ('test_dollar_phone_corpus.txt', 'r') as input:
    text_content= input.read()
    
phone_pattern = re.compile('|'.join([
        r'\(\d{3}\)[\s]\d{3}[\s-]\d{4}',  
        r'\(\d{3}\)[-]\d{3}[\s-]\d{4}',
        r'\d{3}[-]\d{3}[\s-]\d{4}' 
    ]), re.IGNORECASE)

    
telephone_matches= phone_pattern.findall(text_content)

with open('telephone_output.txt', 'w') as output_telephone:
    for match in telephone_matches:
        phone_number = ''.join(filter(None, match))
        if phone_number:
            output_telephone.write(phone_number+'\n')
    


    


