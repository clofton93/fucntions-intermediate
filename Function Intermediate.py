x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x[1])

students[0]['last_name'] = 'Bryant'
print(students[0])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

players = [
    {'first_name' : 'Joe', 'last_name': 'Burrow'},
    {'first_name' : 'Matt', 'last_name' : 'Stafford'},
    {'first_name' : 'Odell', 'last_name' : 'Beckham'},
    {'first_name' : 'Tee', 'last_name' : 'Higgins'}
]


def iterateDictionary(students):
    for student in students:
        print(student)

iterateDictionary(students)


def iterateDictionary2(key, players):
    for player in players:
        print(player[key])
        
iterateDictionary2('first_name', players)
    

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(dojo):
    for key in dojo:
        print(len(dojo[key]), key, dojo[key])

printinfo(dojo)
