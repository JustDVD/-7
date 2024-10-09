my_dict = {'David': 2002,
           'Max': 2003,
           'Daniel': 2002}
print(my_dict)
print(my_dict.get('David'))
print(my_dict.get('Alex'))
my_dict.update({'Alex': 2001,
                'Sasha': 2000})
a = my_dict.pop('Daniel')
print(a)
print(my_dict)
my_set = {1, 2, 3, 1,2, 'dog', 'cat', 'dog', True, 0.5}
print(my_set)
my_set.update({21, 1024, (4, 5, 6, 1)})
my_set.remove('dog')
print(my_set)