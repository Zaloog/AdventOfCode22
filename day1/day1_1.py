
elf_cal_list = []
elf_cal = 0

with open("input.txt", "r") as f:
    for line in  f.readlines():
        if line == "\n":
            elf_cal_list.append(elf_cal)
            elf_cal = 0
        else:
            elf_cal += int(line[:-1])

print(max(elf_cal_list))
    
