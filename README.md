# PythonPractice
## String
```python
# Keep only alphabit and num
normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
# Counter
counter = Counter(word.lower() for word in paragraph.split()) # this is word
for ss in Counter(s).values(): # this is char
# Get Max with directory
max(words.items(), key=operator.itemgetter(1))[0]

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


