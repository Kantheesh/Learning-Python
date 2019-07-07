'''
9. Take below as input dictionary
sample = {
	'user1' : 'yogi',
	user2 : 'booboo',
	user3 : 'rupert',
	user4 : 'teddy',
	user5 : 'care',
	user6 : 'winnie',
	user7 : 'sooty',
	user8 : 'padders',
	user9 : 'polar',
	user10 : 'grizzly',
	user11 : 'baloo',
	user12 : 'bungle',
	user13 : 'fozzie',
	user14 : 'huggy',
	user15 : 'barnaby',
	user16 : 'hair',
	user17 : 'greppy'
}
Perform basic operations like::
	(a) user15 no longer has a machine assigned
	(b) The name of user16's machine is changed to 'Ursa'
	(c) user17 is leaving the company, and a new user, user18, will be assigned his machine
	(d) user5, user6, and user7 are all leaving at exactly the same time, but their machine names are to be stored in a list called machines.
	(e) Print a list of each (hint) user, with their machine, in any order. Do not print users that have no machine defined for them (like user15, for example) -> Try this after 2nd chapter.
'''

sample = {
	'user1' : 'yogi',
	'user2' : 'booboo',
	'user3' : 'rupert',
	'user4' : 'teddy',
	'user5' : 'care',
	'user6' : 'winnie',
	'user7' : 'sooty',
	'user8' : 'padders',
	'user9' : 'polar',
	'user10' : 'grizzly',
	'user11' : 'baloo',
	'user12' : 'bungle',
	'user13' : 'fozzie',
	'user14' : 'huggy',
	'user15' : 'barnaby',
	'user16' : 'hair',
	'user17' : 'greppy'
}

print("-----------------------------------------------------")
samplek = {'user15': None}
sample.update(samplek)
print(sample)
print("-----------------------------------------------------")

sample1 = {'user16': 'Ursa'}
sample.update(sample1)
print(sample)
print("-----------------------------------------------------")

sample.popitem()					#sample.keys(replace('user17', 'user18'))
sample2 = {'user18': 'greppy'}		#print(sample)
sample.update(sample2)
print(sample)
print("-----------------------------------------------------")


m = sample.get('user5')
print(m)
n = sample.get('user6')
print(n)
p = sample.get('user7')
print(p)
o = m,n,p
print(o)
machines = list(o)
print(machines)
sample.pop('user5')
sample.pop('user6')
sample.pop('user7')
print(sample)
print("-----------------------------------------------------")

