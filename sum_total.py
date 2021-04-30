dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for i in dict:
    lenght=len(dict[i])
    count=count+lenght
print(count)
    