"""Dcitonary"""

my_dictioanry = { # Dictionary
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

print(my_dictioanry)
print(my_dictioanry['key1'])

# Add new key-value pair
my_dictioanry['key4'] = 'value4'

print(my_dictioanry)

# Loop through dictionary
for key in my_dictioanry:
    print(key)
    print(my_dictioanry[key])

# Delete key-value pair
del my_dictioanry['key4']

print(my_dictioanry)