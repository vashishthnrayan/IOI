mic_dict = {'name' : 'Vashishth','age' : 14,'class' : 7}
print(mic_dict['name'])
print(mic_dict.get('age'))

mic_dict['school'] = 'DAV'
print(mic_dict)

mic_dict['class'] = 8
print(mic_dict)

mic_dict.pop('age')
print(mic_dict)


print(mic_dict.get('school'))

print(mic_dict.clear())