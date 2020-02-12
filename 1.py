# @1, @2 ---> selection predicates
# A, B, A1, B1 ---> attributes of relations
# r, s, t ---> relations
# L1, L2, L3 ---> list path
# E1, E2, E3 ---> relational algebra expression
# $ ---> Select
# % ---> Project
# * ---> X(for cross multiplication)
# # ---> join
# UNION ---> union
# INTER ---> intersection
# AND ---> and
# OR ---> or


def select_basic(string):
	list1 = [string]
	string = string.strip(" ")
	while(string[0] == '(' and string[len(string)-1] == ')'):
		string = string.strip('(')
		string = string.strip(')')
	string = string.strip('$')
	string = string.strip(" ")
	theta = string[0:string.index('(')]
	inner_string = string[string.index('(')+1: -1]
	
	while(inner_string[0] == '(' and inner_string[len(inner_string)-1] == ')'):
			inner_string = inner_string.strip('(')
			inner_string = inner_string.strip(')')
	
	if(theta.find('AND') != -1):
		arr = theta.split('AND')
		list1.append('$' + arr[0] + '(' + '$' + arr[1] + '(' + inner_string +')' + ')' )
	if(theta.find('AND')!= -1 and inner_string.find('#') != -1):
		arr = theta.split('AND')
		arr2 = inner_string.split('#')
		list1.append('(' + '$' + arr[0] + '(' + arr2[0] + ')' + ')' + '#' + arr2[1][0: arr2[1].index('E')] + '(' + '$' + arr[1] + '(' + arr2[1][arr2[1].index('E'):] + ')' + ')')
	if(inner_string.find('$') != -1):		
		inner_string = inner_string.strip('$')
		inner_string = inner_string.strip(" ")
		theta2 = inner_string[0:inner_string.index('(')]
		inner_string2 = inner_string[inner_string.index('(')+1: -1]
		list1.append('$' + theta2 + '(' + '$' + theta + '(' + inner_string2 + ')' + ')' )	
	elif(inner_string.find('*') != -1):
		arr = inner_string.split('*')
		list1.append(arr[0] + ' #' + theta + " " +arr[1])
		list1.append(arr[1] + ' #' + theta + " " +arr[0])
	elif(inner_string.find('#') != -1):
		arr = inner_string.split('#')
		list1.append(arr[0] + '#' + theta + 'AND' + arr[1])	
	elif(inner_string.find('UNION') != -1):
		arr = inner_string.split('UNION')
		list1.append('$' + theta + '(' + arr[0] + ')' + 'UNION' + '$' + theta + '(' + arr[1] + ')' )
		list1.append('$' + theta + '(' + arr[1] + ')' + 'UNION' + '$' + theta + '(' + arr[0] + ')' )
	elif(inner_string.find('INTER') != -1):
		arr = inner_string.split('INTER')
		list1.append('$' + theta + '(' + arr[0] + ')' + 'INTER' + '$' + theta + '(' + arr[1] + ')' )
		list1.append('$' + theta + '(' + arr[1] + ')' + 'INTER' + '$' + theta + '(' + arr[0] + ')' )
		list1.append('$' + theta + '(' + arr[0] + ')' + 'INTER ' + arr[1] )
		list1.append('$' + theta + '(' + arr[1] + ')' + 'INTER ' + arr[0] )
	elif(inner_string.find('-') != -1):
		arr = inner_string.split('-')
		list1.append('$' + theta + '(' + arr[0] + ')' + '-' + '$' + theta + '(' + arr[1] + ')' )
		list1.append('$' + theta + '(' + arr[0] + ')' + '-' + arr[1] )
	print(list1)

def print_equivalents(string):
	print(string)

if __name__ == "__main__":
	fo = open("sample.txt","r");
	for i in fo:
		sample = i;
		sample = sample.strip("\n")
		sample = sample.strip("\t")
		sample = sample.strip(" ")
		select_basic(sample);
	fo.close()
