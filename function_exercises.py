# 1. 
def is_two(number):
    number = int(number)
    return number % 2 == 0



# 2.
def is_vowel(string):
    string = str(string)
    if len(string) == 1 and string.lower() in ['a','e','i','o','u']:
        return True
    else: 
        return False
    


# 3. 
def is_consonant(string):
    string = str(string)
    if len(string) == 1 and string.lower() not in ['a','e','i','o','u'] and string.isalpha():
        return True
    else: 
        return False



# 4.
def capitalize_consonant(word):
    if word[0].lower() in ['a','e','i','o','u']:
        return f'{word} does not start with a consonant'
    else:
        return word.capitalize()



# 5.
def calculate_tip(bill_total, tip_percentage=.2):
    tip_amount = bill_total * tip_percentage
    return f'The amount to tip at {int(tip_percentage * 100)}% is ${tip_amount:.2f}!'



# 6.
def apply_discount(original_price, discount_percentage):
    discounted_price = original_price * (1 - discount_percentage)
    return f'The price after your discount is now ${discounted_price:.2f}!'



# 7.
def handle_commas(number):
    if type(number) == str:
        number = number.replace(',', '')
        if number.isdigit():
            return int(number)
        else:
            return False
    else:
        return False



# 8.
def get_letter_grade(number_grade):
    if type(number_grade) == int:
        if number_grade >= 90:
            return 'Letter Grade: A'
        elif number_grade >= 80:
            return 'Letter Grade: B'
        elif number_grade >= 75:
            return 'Letter Grade: C'
        elif number_grade >= 70:
            return 'Letter Grade: D'
        else:
            return 'Letter Grade: F'
    else:
        return f'{number_grade} is not a valid input'



# 9.
def remove_vowels(user_input):
    for char in user_input:
        if is_vowel(char):
            user_input = user_input.replace(char, '')
        else:
            continue
    return user_input



# 10. 
# import string

# def normalize_name(name):
#     special_chars = string.punctuation
#     if name[0].isdigit():
#         name = name.replace(name[0])
#     else:
#         continue
#     for char in name:
#         if char.isdigit():
#             name = name.replace(name[0],'')
#         elif char in special_chars:
#             name = name.replace(char, '')
#         else:
#             continue
#     return name.lower().strip().replace(' ','_')



# 11. 
def cumulative_sum(oldlist):
    newlist=[]
    c_sum = 0
    for num in oldlist:
        c_sum += num
        newlist.append(c_sum)
    print(f'old list: {oldlist}')
    print(f'new list: {newlist}')