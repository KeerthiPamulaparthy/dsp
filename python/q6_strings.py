# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count < 10:
        print "'Number of donuts: %d'" %count
    else:
        print "'Number of donuts: many'"

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
   


def both_ends(s):
    if len(s) >= 2:
        print s[:2]+s[-2:]
    else:
        print "''"
        

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
   



def fix_start(s):
    s = list(s)
    first_char = s[0]
    second_part = []
    for i in s[1:]:
        if i == first_char:
            i = '*'
        second_part.append(i)
    new_word = first_char + "".join(second_part)
    print new_word

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    
    raise NotImplementedError


def mix_up(a, b):
    new_word = b[:2]+a[2:]+' '+a[:2]+b[2:]
    print new_word
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    if len(s) >= 3 and s[-3:] == 'ing':
        new_word = s + 'ly'
        print new_word
    elif len(s) >= 3 and s[-3:] != 'ing':
        new_word = s + 'ing'
        print new_word
    else:
        print s
    
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):
    s.split(" ")
    if s.find('not') < s.find('bad'):
        first_part = s[:s.find('not')]
        new_line = first_part + 'good'
        print new_line
    else:
        print s
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):
     if len(a)%2 == 0 and len(b)%2 == 0:
        word1_first = a[:len(a)/2]
        word1_second = a[len(a)/2:]
        word2_first = b[:len(b)/2]
        word2_second = b[len(b)/2:]
        new_word = word1_first + word2_first + word1_second + word2_second
        print new_word
    elif len(a)%2 != 0 and len(b)%2 == 0:
        word1_first = a[:(len(a)/2)+1]
        word1_second = a[(len(a)/2)+1:]
        word2_first = b[:len(b)/2]
        word2_second = b[len(b)/2:]
        new_word = word1_first + word2_first + word1_second + word2_second
        print new_word
    elif len(a)%2 == 0 and len(b)%2 != 0:
        word1_first = a[:(len(a)/2)]
        word1_second = a[(len(a)/2):]
        word2_first = b[:len(b)/2+1]
        word2_second = b[len(b)/2+1:]
        new_word = word1_first + word2_first + word1_second + word2_second
        print new_word
    else:
        word1_first = a[:(len(a)/2)+1]
        word1_second = a[(len(a)/2)+1:]
        word2_first = b[:len(b)/2+1]
        word2_second = b[len(b)/2+1:]
        new_word = word1_first + word2_first + word1_second + word2_second
        print new_word
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
