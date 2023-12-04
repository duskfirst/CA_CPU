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
		print('Instruction:', i, '->', b[:5], b[5], b[6:10], b[10:14], b[14:16], b[16:])
		print(opcode[int('0b'+b[:5],2)]+movu[int('0b'+b[14:16],2)], int('0b'+b[5],2), 'r'+str(int('0b'+b[6:10],2)), 'r'+str(int('0b'+b[10:14],2)), int('0b'+b[16:],2))
		print()