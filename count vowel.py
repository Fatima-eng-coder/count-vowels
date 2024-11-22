s=input()
vowel="aeiou"
index=0
count=0
while index < len(s):
    if s[index] in vowel:
        count+=1
        
    index+=1
    
    
print(count)