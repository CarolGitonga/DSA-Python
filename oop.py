# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# In CreditCard class, there are different CreditCard instances, and each must maintain its own balance, its own credit limit, and so on.
# Therefore, each instance stores its own instance variables to reflect its current state.

# %%
class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        return self._customer # return name of the customer
    def get_bank(self):
        return self._bank  # return the bank's name
    def get_account(self):
        return self.account # return the card identifying number (typically stored as a string)
    def get_limit(self):
        return self._limit  # return current credit limit
    def get_balance(self):
        return self._balance # return current balance
    def charge(self, price):
        if price + self._balance > self._limit: # if the charge exceeds
            return False # canot accept the charge
        else:
            self._balance += price
            return True # return true if charge was processed
    def make_payment(self, amount):
        self._balance -= amount # process customer payment that reduces balance

if __name__ ==' __main__' :
    wallet = [ ]
    wallet.append(CreditCard( 'John Bowman' ,'California Savings' ,'5391 0375 9387 5309' , '2500') )
    wallet.append(CreditCard( 'John Bowman' ,'California Federal' , '3485 0399 3395 1954' , '3500') )
    wallet.append(CreditCard( 'John Bowman' ,'California Finance' , '5391 0375 9387 5309' , '5000') )
    for val in range(1, 17):
      wallet[0].charge(val)
      wallet[1].charge(2*val)
      wallet[2].charge(3*val)
    for c in range(3):
      print( 'Customer =' , wallet[c].get_customer())
      print( 'Bank =' , wallet[c].get_bank())
      print(' Account = ', wallet[c].get_account())
      print( 'Limit = ', wallet[c].get_limit())
      print( 'Balance = ', wallet[c].get_balance())
      while wallet[c].get_balance( ) > 100:
        wallet[c].make_payment(100)
        print( 'New balance = ', wallet[c].get_balance())
    print()


# %%
class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        return self._customer # return name of the customer
    def get_bank(self):
        return self._bank  # return the bank's name
    def get_account(self):
        return self._account # return the card identifying number (typically stored as a string)
    def get_limit(self):
        return self._limit  # return current credit limit
    def get_balance(self):
        return self._balance # return current balance
    def charge(self, price):
        if price + self._balance > self._limit: # if the charge exceeds
            return False # canot accept the charge
        else:
            self._balance += price
            return True # return true if charge was processed
    def make_payment(self, amount):
        self._balance -= amount # process customer payment that reduces balance
# Create a CreditCard instance
my_card = CreditCard('Carol Gitonga', 'Equity Bank', '123456789', 500)
#my_card = CreditCard('John Doe', 'ABC Bank', '123456789', 1000)

# Test the get methods
print(my_card.get_customer())  # Should print 'John Doe'
print(my_card.get_bank())  # Should print 'ABC Bank'
print(my_card.get_account())  # Should print '123456789'
print(my_card.get_limit())  # Should print 1000
print(my_card.get_balance())  # Should print 0

# Test the charge method
print(my_card.charge(250))  # Should print True
print(my_card.get_balance())  # Should print 500
print(my_card.charge(600))  # Should print False since the limit is exceeded

# Test the make_payment method
my_card.make_payment(200)
print(my_card.get_balance())  # Should print 300


# %%
Vector class provides functionality for creating, manipulating, and performing operations on vectors in a multidimensional space, such as addition,
comparison, and string representation.


# %%
class Vector: #a vector in a multidemesional space
    def __init__(self, d):
        self._coords = [0] * d # create a dimensional vector of zeros
    def __len__(self):
        return len(self._coords) # return the dimension of the vector
    def __getitem__ (self, j):
        return self._coords[j] # return jth coordinate of the vector
    def __setitem__ (self, j, val):
        self._coords[j] = val # set the jth coordinate of the vector to a given value
    def __add__(self, other):
        #return sum of two vectors
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other [j]
        return result
    def __eq__(self, other):
        return self._coords == other._coords # return True if vector has same cooordinates as other
    def __ne__(self, other):
        return not self == other # return true if vector differs from other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>' # produce a string representation of vector
        
# Create vectors for testing
v1 = Vector(3)  # Dimension 3
v2 = Vector(3)
v3 = Vector(4)  # Dimension 4

# Test vector initialization and length
assert len(v1) == 3
assert len(v2) == 3
assert len(v3) == 4

# Test setting and getting coordinates
v1[0] = 1
v1[1] = 2
v1[2] = 3
assert v1[0] == 1
assert v1[1] == 2
assert v1[2] == 3

# Test vector addition
v2[0] = 2
v2[1] = 4
v2[2] = 6
result = v1 + v2
assert result[0] == 3
assert result[1] == 6
assert result[2] == 9

# Test vector equality
#assert v1 == Vector(3)()  # Equal vectors
#assert not v1 == v2  # Different vectors
# Test vector inequality
#assert v1 != v2  # Different vectors
#assert not v1 != Vector(3).coords  # Equal vectors

# Test string representation
assert str(v1) == "<1, 2, 3>"

print("All test cases passed successfully.")   

# %%
Iterators are fundamental in Python for efficient and flexible iteration over sequences of data,lazy evaluation, memory optimization, 
and handling large data sets or infinite sequences.


# %%
class SequenceIterator: # an iterator for any python's sequence types
    def __init__(self, sequence):
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on the first call to next
    def __next__(self):
        self._k += 1 # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k]) # return the data element
        else:
            raise StopIteration() # there are no more elements
    def __iter__(self):
        return self # an iterator must return itself as an iterator
# Define a list and a string for testing
test_list = [1, 2, 3, 4, 5]
test_string = "Hello"

# Test iterating over a list using SequenceIterator
list_iterator = SequenceIterator(test_list)
for item in list_iterator:
    print(item)  # Should print each element of the list

# Test iterating over a string using SequenceIterator
string_iterator = SequenceIterator(test_string)
for char in string_iterator:
    print(char)  # Should print each character of the string

# Test iterating manually using next() function
manual_iterator = SequenceIterator(test_list)
print(next(manual_iterator))  # Should print the first element (1)
print(next(manual_iterator))  # Should print the second element (2)
print(next(manual_iterator))  # Should print the third element (3)
print(next(manual_iterator))  # Should print the fourth element (4)
print(next(manual_iterator))  # Should print the fifth element (5)
try:
    print(next(manual_iterator))  # Should raise StopIteration
except StopIteration:
    print("Reached end of sequence")

# Test iterating over an empty sequence
empty_iterator = SequenceIterator([])
try:
    print(next(empty_iterator))  # Should raise StopIteration immediately
except StopIteration:
    print("Reached end of empty sequence")          

# %%
Range class calculates the length of the range, allowing indexing and element access, and supporting iteration
to generate the desired sequence of numbers according to the specified parameters (start, stop, step).


# %%
class Range: # mimics the built-in range class
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        self._length = max(0, (stop - start + step - 1) // step) # calculate the effective length once
        self._start = start
        self._step = step
    def __len__(self):
        return self._length # return number of entries in the range
    def __getitem__(self, k):
        if k < 0:
            k +=len(self)
        if not 0 <= k < self._length:
            raise IndexError('index is out of range')
        return self._start + k * self._step
# Create a Range object
my_range = Range(1, 10, 2)

# Print the length of the range
print(len(my_range))  # Output: 5

# Access elements of the range using indexing
print(my_range[0])  # Output: 1
print(my_range[2])  # Output: 5

# Iterate over the range
for num in my_range:
    print(num)  # Output: 1, 3, 5, 7, 9


# %%
class Progression: #generic progression
    def __init__(self, start=0):
        self._current = start #initial current to the first value of progression
    def _advance(self): 
        self._current += 1 # update the current value to a new value
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current # record the current value
            self._advance() #advance to prepare for the next value
            return answer
    def __iter__(self):
        return self # an iterator ust return itself
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))
class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0): # create a new arithmetic progression
        super(). __init__(start) # initiaize the base class
        self._increment = increment # update current value by adding the fixed increment
    def _advance(self):
        self._current += self._increment
class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super(). __init__(start)
        self._base = base # update the current value by multiplying it by the base vale
    def _advance(self):
        self._current *= self._base
class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first) # start progression at first
        self._prev = second - first # ficitious value preceding the first
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current # update the current value by taknig sum of the previous two
        
if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)
    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)
    print( 'Arithmetic progression with increment 5 and start 2:' )
    ArithmeticProgression(5, 2).print_progression(10)
    print( 'Geometric progression with default base:' )
    GeometricProgression().print_progression(10)
    print( 'Geometric progression with base 3:' )
    GeometricProgression(3).print_progression(10)
    print( 'Fibonacci progression with default start values:' )
    FibonacciProgression().print_progression(10)
    print( 'Fibonacci progression with start values 4 and 6: ')
    FibonacciProgression(4, 6).print_progression(10)


# %%
from abc import ABCMeta, abstractmethod
class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        pass
    @abstractmethod
    def __getitem__(self, j):
        pass
    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')
    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
# Define a concrete implementation of Sequence for testing
class MySequence(Sequence):
    def __init__(self, items):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, j):
        return self._items[j]
# Test cases
def test_sequence_operations():
    seq = MySequence([1, 2, 3, 4, 5])

    # Test __len__
    assert len(seq) == 5

    # Test __getitem__
    assert seq[0] == 1
    assert seq[2] == 3
    assert seq[-1] == 5

    # Test __contains__
    assert 3 in seq
    assert 6 not in seq

    # Test index
    assert seq.index(4) == 3

    # Test count
    assert seq.count(2) == 1
    assert seq.count(6) == 0

    print("All test cases passed successfully!")

# Run the test cases
test_sequence_operations()


# %%
