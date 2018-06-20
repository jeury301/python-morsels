def with_previous_s0(iterable):
    """Provide each sequence item with item before it
    
    Comments:
        This solution has several issues:
            1. The use of range(len(sequenece)) to obtain the index.
            We should always use enumerate(sequence) to obtain the index

            2. We should avoid obtaining the index altogether. One solution is
            to keep track of the previous item (in this particular case)
        Solution fails all bonuses
    """
    items = []
    for i in range(len(iterable)):
        if i == 0:
            items.append((iterable[i], None))
        else:
            items.append((iterable[i], iterable[i-1]))
    return items

def with_previous_s1(iterable):
    """Provide each sequence item with item before it
    
    Comments:
        This is an improvement over the previous solution:
            1. We are now keeping track of the previous item
            2. We are avoiding indexes.
        Solution passes 1 bonus
    """
    prev = None
    items = []
    for item in iterable:
        items.append((item, prev))
        prev = item
    return items

def with_previous_s2(sequence):
    """Provide each sequence item with item before it

    Comments:
        Solution using the zip function
        Solution fails all bonuses
    """
    items = []
    for curr, prev in zip(sequence, [None] + list(sequence)):
        items.append((curr, prev))
    return items

def with_previous_s3(sequence):
    """Provide each sequence item with item before it
    
    Comments: 
        Zip returns an iterable. The zip function returns
        an iterable containing a tuple of the following format:
        for seq1 and seq2, let item-n-seq-m be the nth item of the mth sequence

        so for seq1, item-1-seq-1 is the first item of the sequence 1.

        zip then returns the following sequence:

        final_seq = zip(seq1, seq2)
        final_seq = ((item-1-seq1, item-1-seq-2), (item-2-seq1, item-2-seq2), 
                    ...)
    """
    return zip(sequence, [None] + list(sequence))

def with_previous_s4(iterable):
    """Provide each sequence item with item before it
    
    Comments:
        Solution passes the first bonus i.e.: the solution works
        not only with lists, but also with tuples, and strings.
    """
    previous = None
    items = []
    for item in iterable:
        items.append((item, previous))
        previous = item
    return items

def with_previous_s5(iterable):
    """Provide each sequence item with item before it
    
    Comments:
        Solution passes the first two bonuses:
        1. First bonus: not using indeces
        2. Second bonus: returing a lazy iterable - generator by using
        the 'yield' keyword instead of appending the values
    """
    previous = None
    for item in iterable:
        yield (item, previous)
        previous = item

def with_previous_s6(iterable):
    """Provide each sequence item with item before it
    
    Comments:
        The 'tee' function creates two independent iterators
        from the passed iterator

        The 'chain' function creates a new iterator combining the 
        passed sequences, in a memory efficient way - it only caches one
        item at a time

        The 'zip' function returns a list of tuples, where the first item of each
        tuple is the first item of the first iterator, and the second item of the 
        tuple is the first item of the second iterator.

        The final result is like this:
            [(item1, prev1), (item2, item1), ...]
    """
    from itertools import tee, chain

    i1, i2 = tee(iterable)
    return zip(i1, chain([None], i2))

try:
    def with_previous(iterable, *, fillvalue=None):
        """Provide each sequence item with item before it
        
        Comments:
            The * indicates that every argument after it, its a keyword
            argument. This is a python3 feature

            This solution passes all 3 bonunes
        """
        previous = fillvalue
        for item in iterable:
            yield item, previous
            previous = item
except SyntaxError as e:
    def with_previous(iterable, **kwargs):
        """Provide each sequence item with item before it
        
        Comments:
            This is the python 2 version of the previous code
        """
        previous = kwargs.get('fillvalue')
        for item in iterable:
            yield item, previous
            previous = item

def test_with_previous(func):
    test_data = [0, 1, 2, 3, 4, 5]
    gen = func(test_data)
    
    while True:
        try:
            print(next(gen))
        except StopIteration:
            break


test_with_previous(with_previous)



