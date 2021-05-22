s=input()
count=0
new_cnt=0
new_str=""
for char in s:
    if char == new_str:
        count+=1
    else:
        new_cnt=max(count,new_cnt)
        count=1
        new_str=char

new_cnt=max(count,new_cnt)
print(new_cnt)