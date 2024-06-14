phrase = str(input('Type a sentence: ')).upper().strip()

print('The sentence has {} letters A'.format(phrase.count('A')))
print('First A is on position {}'.format(phrase.find('A')+1))
print('Last A is on position {}'.format(phrase.rfind('A')+1))