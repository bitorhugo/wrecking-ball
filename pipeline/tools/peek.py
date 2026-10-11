import sys,re
p=sys.argv[1]; t=open(p,encoding='utf-8',errors='replace').read()
t=re.sub(r'-\n','',t); 
pages=re.split(r'\n=== PAGE (\d+) ===\n',t)
# abstract
m=re.search(r'(?is)abstract(.{0,1500})',t); print('ABSTRACT:',re.sub(r'\s+',' ',m.group(1)) if m else '-')
pat=re.compile(sys.argv[2] if len(sys.argv)>2 else r'(speedup|×|energy (saving|reduction|efficien)|baseline|simulat|gem5|zsim|ramulator|dataset|real (hardware|system)|UPMEM|static graph|dynamic)',re.I)
seen=0
for i in range(1,len(pages),2):
    pg=pages[i]; body=re.sub(r'\s+',' ',pages[i+1])
    for s in re.split(r'(?<=[.!?])\s+',body):
        if pat.search(s) and re.search(r'\d',s) and 40<len(s)<400:
            print(f'[p{pg}] {s}'); seen+=1
            if seen>=int(sys.argv[3] if len(sys.argv)>3 else 25): sys.exit()
