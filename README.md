# PythonPractice
## String
```python
# Keep only alphabit and num
normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
# Get Max with directory
max(charcounter.items(), key=operator.itemgetter(1))[0]
# string get first n charator
sample_str[ 0 : N ]
```
## int
```python
# max number
float('inf')
# min number
float('-inf')
```
## list
```python
# add a list to another list
stack.extend(root.children[::-1])
# add a single value
stack.apend(val)
# python lambda sort
boxTypes.sort(key=lambda box: box[1], reverse=True)
```

## counter
```python
# count words
counter = Counter(word.lower() for word in paragraph.split()) # this is word
# go through each value
for ss in Counter(s).values(): # this is char
#init with empty
charcounter = Counter()
charcounter = Counter(myString)
charcounter[s[endi]] += 1
# delete one of the counter
if charcounter[s[endi]] == 1: del scounter[s[endi]]
```