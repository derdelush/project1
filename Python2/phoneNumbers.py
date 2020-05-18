contacts = {
    'Mike': '0744555555',
    'John': '0732444444',
    'George': '0745666666',
    'Timmy': '0722444444',
    'Cartman': '0755664477',
    'Stan': '07545466654',
    'Kenny': '0765465466',
    'Kyle': '0789798795',
    'Butters': '07897987897',
    'Jimmy': '0788987465'
    }

listOfNumbers, listOfNames = list(contacts.values()), list(contacts.keys())
print(listOfNumbers[::2])
print(listOfNames[-5:])
