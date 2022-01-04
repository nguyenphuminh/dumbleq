import sys

f = open(sys.argv[1], "r")

mem = list(map(
    lambda ins: int(ins), 
    f.read()
     .replace("subleq ", "")
     .replace("\n", " ")
     .replace("\t", "")
     .split(" ")))

ptr = 0

while ptr >= 0:
    if mem[ptr] == -1:
        mem[mem[ptr + 1]] = ord(input()[0])
    elif mem[ptr + 1] == -1:
        print(chr(mem[mem[ptr]]), end = "")
    else:
        mem[mem[ptr+1]] -= mem[mem[ptr]]
        
        if mem[mem[ptr+1]] <= 0:
            ptr = mem[ptr+2]
            continue
    
    ptr += 3

f.close()
