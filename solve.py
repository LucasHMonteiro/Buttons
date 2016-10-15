import sys

def solve(buttons):
	pass

def array_to_int(array):
	length = len(array)
	integer = 0
	for i in range(length):
		if array[i]:
			integer += 2**(length - i - 1)
	return integer

def press(buttons, pos):
	if len(buttons) == 1:
		buttons[0] = (buttons[0]-1) % 2
		return buttons
	if pos == 0:
		buttons[pos] = (buttons[pos]-1) % 2
		buttons[pos+1] = (buttons[pos+1]-1) % 2
	elif pos == len(buttons)-1:
		buttons[pos] = (buttons[pos]-1) % 2
		buttons[pos-1] = (buttons[pos-1]-1) % 2
	else:
		buttons[pos] = (buttons[pos]-1) % 2
		buttons[pos+1] = (buttons[pos+1]-1) % 2
		buttons[pos-1] = (buttons[pos-1]-1) % 2
	return buttons

def play(buttons):
	a = 0
	print(buttons)
	while 1:
		try:
			a = int(input())
			if a < 0:
				break
			press(buttons, a)
			print(buttons)
		except:
			pass

def _hash_gen(size):
	for x in range(2**size):
		yield x, False 

def hash_gen(size):
	return dict(_hash_gen(size))
	pass

def in_hash(key):
	return _hash[key]
	pass

def print_falses():
	for key, value in _hash.items():
		if not value:
			print(bin(key), key, value)

def check_final_state(buttons):
	integer = array_to_int(buttons)
	final = array_to_int(final_state)
	return integer == final or integer == complement(buttons) 

def complement(buttons):
	return array_to_int(buttons) ^ 2**len(buttons)-1
	pass

def backtracking(buttons, pos):
	press(buttons, pos)
	if check_final_state(buttons):
		return True
	if not in_hash(array_to_int(buttons)):
		_hash[array_to_int(buttons)] = True
		_hash[complement(buttons)] = True
		for x in range(len(buttons)):
			if backtracking(buttons, x):
				return True
	press(buttons, pos)
	return False

def main(argv):
	sys.setrecursionlimit(10000)
	buttons = [0, 0, 0, 0, 0, 1, 0, 0]
	global final_state
	final_state = [1, 0, 1, 0, 1, 0, 1, 0]
	if argv[0] == 'try':
		play(buttons)
	elif argv[0] == 'solve':	
		global _hash
		_hash = hash_gen(len(buttons))
		_hash[array_to_int(buttons)] = True
		_hash[complement(buttons)] = True
		print(backtracking(buttons, 0))
		#print(_hash)
		print_falses()

if __name__ == '__main__':
	main(sys.argv[1:])