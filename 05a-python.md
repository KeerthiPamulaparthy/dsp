# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and Tuples are similar in that both are a sequence of values, and the values can be strings, lists or tuples. However, the key difference between them is that lists are mutable, whereas tuples are immutable. Tuples will work as keys in a dictionary, due to the fact that tuples are immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> 
Lists and Sets are similar in that they can be used in a for loop, they support ‘x in list’, ‘x in set’.
Lists and sets are different in that lists are ordered, while sets are unordered. Lists can contain duplicates, while sets contain no duplicate elements.

List example:
>basket = ['apple', 'banana','apple']
>basket
['apple', 'banana', 'apple']

Sets example:
>basket = set(['apple', 'banana','apple'])
>basket
{'apple', 'banana'}

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda expressions can be used to create small anonymous functions. They can be used whereever function objects are used, and are restricted to a single expression.
Example: sorted(professor_dict.items(), key = lambda name: name[1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions can be used to define and create lists. 
numbers = [1,2,3]
Squares = [ (x*x) for x in numbers ]

Map: map() is a function with two arguments where the first argument is the function and the second argument is sequence. map() applies the function to all the elements of the sequence and returns a new list with the elements changed by function. 

numbers = [1,2,3]
Squares =  map(lambda x: x*x, numbers)

Filter:Provides a way to filter the elements in the list.
numbers = [1,2,3]
odd = filter(lambda x: x % 2 != 0, numbers)

Set comprehensions are similar to list comprehension, but they return a set and not a list.
Example: squares = set(n**2 for n in range(10))

A Dictionary comprehension takes two lists and creates a dictionary where the item at each position in the first list becomes a key and the item at the corresponding position in the second list becomes the value.
example:
string = ['a', 'b', 'c']
Squares_dict = {k: v**2 for (k, v) in zip(string,range(10))}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>>  937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





