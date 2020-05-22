'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

""" def count_th(word):
    th = "th"
    count = word.count(th)
    return count

count_th("ththhe") """

def count_th(word, count=0): #initialize count at 0
    th = "th" #I want to find this
    index = word.find(th)  #index is equal to the index that is returned when i find th in word
    # in this case is at zero 
    if index == -1: #if we're out of range, return the count
        return count
    else: #else prepare another call with word now being sliced
        word = word[(index + len(th) - 1):] #word is now from index -> index where it was found the "th" (0) + length of the word we want to find - 2  minus 1 to target last element
        count += 1 #increment count!
        return count_th(word,count) #recurse with updated word and count


count_th("thkjskjdthjjdkjth")
