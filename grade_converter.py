# FILE NAME - grade_converter.py

# NAME: Casey Tatar
# DATE: 3/1/206
# BRIEF DESCRIPTION:  Most learning management systems (Blackboard, Brightspace, etc.) have a feature where grades can be expressed as either percentages or letters. This experience will ask for a percentage and - using the table found in the specifications - return the corresponding letter grade.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    
    grade_converter()

def grade_converter():
    
   print('===== Grade Converter =====')
   grade = int(input('Enter a numerical grade (1-100): '))

   if 0 <= grade < 65:
      print('F')
   elif 65 <= grade < 70:
      print('D')
   elif 70 <= grade < 80:
      print('C')
   elif 80 <= grade < 90:
      print('B')
   elif 90 <= grade <= 100:
      print('A')
   elif 100 < grade <= 1000:
      print('A+')
   else:
    print('INVALID GRADE')


main()
    









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Be careful about including and excluding numbers that are inputed by the user. 





'''
