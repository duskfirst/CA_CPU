opcode=['add','sub','mul','div','mod','cmp','and','or','not','mov','lsl','lsr','asr','nop','ld','st','beq','bgt','b','call','ret']
movu=['','u','h']

a = input('Enter string input of hex of rom: ')

def fun(a):
	a = a.split()
	for i in a:
		s=int(i,16)
		b=bin(s)[2:]
		while (len(b) < 32):
			b='0'+b
		inst = opcode[int('0b'+b[:5],2)]
# opcode[int('0b'+b[:5],2)]+movu[int('0b'+b[14:16],2)], int('0b'+b[5],2), 'r'+str(int('0b'+b[6:10],2)), 'r'+str(int('0b'+b[10:14],2)), int('0b'+b[16:],2)
		if (inst == 'ld' or inst == 'st'):
			inst += ' r'+str(int('0b'+b[6:10],2)) + ", " + str(int('0b'+b[16:],2)) + '[r'+str(int('0b'+b[10:14],2)) + "]"
			print(inst)
			continue
		elif (inst == 'ret' or inst == 'nop'):
			print(inst)
			continue
		elif (inst in ['call', 'b', 'beq', 'bgt']):
			print(inst, int('0b'+b[5:],2))
			continue
		elif (inst == 'cmp'):
			if (int('0b'+b[5],2)):
				inst += ' r'+str(int('0b'+b[10:14],2)) + ", " + str(int('0b'+b[16:],2))
			else:
				inst += ' r'+str(int('0b'+b[10:14],2)) + ", " + 'r'+str(int('0b'+b[14:18],2))
			print(inst)
			continue
		elif (inst in ['not','mov']):
			if (int('0b'+b[5],2)):
				inst += ' r'+str(int('0b'+b[6:10],2)) + ", " + str(int('0b'+b[16:],2))
			else:
				inst += ' r'+str(int('0b'+b[6:10],2)) + ", " + 'r'+str(int('0b'+b[14:18],2))
			print(inst)
			continue
		else:
			inst += ' r'+str(int('0b'+b[6:10],2)) + ", " + 'r'+str(int('0b'+b[10:14],2))
			if (int('0b'+b[5],2)):
				inst += ", " + str(int('0b'+b[16:],2))
			else:
				inst += ", " + 'r'+str(int('0b'+b[14:18],2))
			print(inst)

fun(a)
input()