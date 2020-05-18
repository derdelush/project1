string = "We will be the best java developers that the world has ever seen"
new_string = string.replace('java developers', 'Cloud Engineers')
ce = new_string[20:35]
print(ce)
shout = ce.upper()
final_string = ''.join(reversed(shout))
print(final_string)
