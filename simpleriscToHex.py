import sys

opcode=['add','sub','mul','div','mod','cmp','and','or','not','mov','lsl','lsr','asr','nop','ld','st','beq','bgt','b','call','ret']
movu=['','u','h']

if (len(sys.argv) == 1):
    print("\nPlease type python ./simpleriscToHex.py filename.txt\n")
    exit()
file1 = open(sys.argv[1])
lines = file1.readlines()

def fun(a):
	inp=""
	for i in lines:
		line = i.split()
		operand = opcode.index(line[0])
		line.pop(0)
		#print(line, opcode[operand])
		
# opcode[int('0b'+b[:5],2)]+movu[int('0b'+b[14:16],2)], int('0b'+b[5],2), 'r'+str(int('0b'+b[6:10],2)), 'r'+str(int('0b'+b[10:14],2)), int('0b'+b[16:],2)
		if (opcode[operand] == 'ld' or opcode[operand] == 'st'):
			rd = int(line[0][1:4])
			rs1 = int(line[1][1:4])
			imm = int(line[2])
			out = (operand << 27)+(1 << 26)+(rd << 22)+(rs1 << 18)+(imm)
		elif (opcode[operand] == 'ret' or opcode[operand] == 'nop'):
			out = (operand << 27)
		elif (opcode[operand] in ['call', 'b', 'beq', 'bgt']):
			out = (operand << 27)+(int(line[0]))
		elif (opcode[operand] == 'cmp'):
			if (line[1][0]=='r'):
				rs1 = int(line[0][1:4])
				rs2 = int(line[1][1:4])
				out = (operand << 27)+(rs1 << 18)+(rs2 << 14)
			else:
				rs1 = int(line[0][1:4])
				imm = int(line[1])
				out = (operand << 27)+(1 << 26)+(rs1 << 18)+imm
		elif (opcode[operand] in ['not','mov']):
			rd = int(line[0][1:4])
			if (line[1][0] != 'r'):
				imm = int(line[1])
				out = (operand << 27)+(1 << 26)+(rd << 22)+(imm)
			else:
				rs1 = int(line[1][1:4])
				out = (operand << 27)+(rd << 22)+(rs1 << 14)
		else:
			rd = int(line[0][1:4])
			if (line[2][0] == 'r'):
				rd = int(line[0][1:4])
				rs1 = int(line[1][1:4])
				rs2 = int(line[2][1:4])
				out = (operand << 27)+(rd << 22)+(rs1 << 18)+(rs2 << 14)
			else:
				rd = int(line[0][1:4])
				rs1 = int(line[1][1:4])
				imm = int(line[2])
				out = (operand << 27)+(1 << 26)+(rd << 22)+(rs1 << 18)+(imm)
		# print(hex(out)[2:])
		inp += str(hex(out)[2:])+" "
	print(inp)
fun(lines)
input()
