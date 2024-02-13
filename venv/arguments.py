#argument and keyword arguments
def user_info(name, age = 0, city = "Selangor"):
    '''This function prints name, age, and city from argumments'''

    print('{} is {} years old, from {}'.format(name, age, city))

user_info('Nabil Husni', 28, 'Kuala Lumpur')
user_info('Nadim')
user_info('Nadim', 2)

def user_detail(fname, lname, email, study, *args, **kwargs):
    '''This function is to use *args & **kwargs'''

    print('{} {} email address is {} currently studying {} on {} {}'.format(fname,lname,email, study, *args, **kwargs))

user_detail('Nabil', 'Husni', 'mail@mail.com', "Python", 13, 'February 2024')