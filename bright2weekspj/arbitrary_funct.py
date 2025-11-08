def build_profile (first,last, **user_info ):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

personal_details = build_profile('bright','adieme', age = '34',
                                 location = 'london', origin = 'nigeria'
                                 ,hobbies = 'coding, music and dancing')
print(personal_details)



