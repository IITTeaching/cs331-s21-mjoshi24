import urllib
import urllib.request
import queue
import unittest


def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    return radix(book_to_words())

def itemToQ(nums, k, maxlen):
    queue = [ [] for i in range(256) ]
    for j in range(0,len(nums)):
        pos = getDigit(nums[j], k, maxlen)
        queue[pos].append(nums[j])
    return queue

#similar to book, except from strings instead (will help with each individual)
def split_individual(lst):
    encoded = lst.encode('ascii', 'replace')
    arr = encoded.split()
    find = radix(arr)
    return helper(find)

#helper for individuals
def helper(arr):
    s = []
    for i in range(len(arr)):
        s.append(arr[i].decode('ascii'))
    return s

#converts the queue to an array
def qToArr(queue, num):
    arr = [ [] for i in range(num) ]
    index = 0
    for i in range(0, len(queue)):
        current = queue[i]
        while len(current) > 0:
            arr[index] = current.pop(0)
            index += 1
    return arr

# MAIN RADIX SORT
def radix(lst):
    maxlen = findmax(lst)
    for i in range(0, maxlen):
        lst = qToArr(itemToQ(lst, i, maxlen), len(lst))
    return lst

def findmax(arr):
    maxlen = len(arr[0])
    for i in range(1, len(arr)):
        if len(arr[i]) > maxlen:
            maxlen = len(arr[i])
    return maxlen

def getDigit(word, k, maxlen):
    digit = maxlen - k - 1
    if digit >= len(word):
        return 0
    else:
        return word[digit]

################################################################################
# TEST CASES
################################################################################
def test1():
    tc = unittest.TestCase()
    book_url='https://www.gutenberg.org/files/84/84-0.txt'
   # booktxt = urllib.request.urlopen(book_url).read().decode()
   # bookascii = booktxt.encode('ascii','replace')
    words = book_to_words()
    radix, sort = radix_a_book(), sorted(words)
    test_book(radix, sort)
    say_success()

def test2():
    print("\words")
    words = "hello hey hi my name is how are you today"
    ans = split_individual(words)
    for i in range(len(ans)-1):
        assert(ans[i] < ans[i+1])
    say_success()

    print("\letters")
    words = "j l p m n o k t"
    ans = split_individual(words)
    for i in range(len(ans)-1):
        assert(ans[i] < ans[i+1])
    say_success()

def test_book(radix, sort):
    print("\tentire book sort")
    tc = unittest.TestCase()
    tc.assertTrue(radix == sort)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    test1()
    test2()
    print(80 * "#" + "\nentire book sorted SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
