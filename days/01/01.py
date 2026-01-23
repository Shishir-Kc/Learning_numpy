# 01 - >  introduction to Numpy !


import numpy as np 

"""

    Day 01 

    importing numpy as np well known among programmers 

    lets create a simple array  

    but first we need to know about numpy a little bit .

    numpy basically allows python to use ndarrays .

    now create a array 

    to create an array we will be using numpy`s built in function called array that takes array or elements as arguments 


"""

numbers = np.array([0,1,2,3,4,5,6,7,8,9])
print(numbers) # - > we get [0 1 2 3 4 5 6 7 8 9]

"""
    lets check its type !

"""

print(type(numbers)) # checking its type it gives us <class 'numpy.ndarray'>

"""
    FUN FACT : numpy can only store same data types i.e it is 100x faster then python normal list  ! 

"""

# Quick task : 01) create a 1d array from a list comprehension that produces the even integres from 2 through 20 

# code:

numbers = np.array([x for x in range(2,21,2)])
print(numbers) # -> [ 2  4  6  8 10 12 14 16 18 20]


"""
    Introducing multidimensional array 

"""

#example of multidimensional array - > 2x3

multidimesion = np.array([[1,2,3],
                         [4,5,6]])

print(multidimesion) 
""" |-- > [[1 2 3]
           [4 5 6]] """


# Quick challange : create a 2X5 array contaning teh even integers from 2 through 10 in first row and the odd integres form 1 through 9 in the second row 


# code

challange = np.array([[e for e in range(2,11,2)],[o for o in range(1,10,2)]])
print(challange)
""""

OUTPUT : -> [[ 2  4  6  8 10]
             [ 1  3  5  7  9]]

"""


"""

    from here we will learn to create arrays from scratch ! 

    
    To create an array from scratch, several functions are available in NumPy:

    np.zeros() and np.ones()
    np.arange() and np.linspace()
    np.random.rand() and np.random.randint()
    
    Let's start with np.zeros() and np.ones().

"""

# lets start by learning about np.zeros()


array1 =np.zeros(6) # - > here it takes an arg that determines number of element in the array 
print(array1) # - >  its output is [0. 0. 0. 0. 0. 0.]

# it returns the element in floating point not integer 

# lets look at np.ones()


array2 = np.ones(5) # Same as np.zeros() 
print(array2) # - > [1. 1. 1. 1. 1.]
# it also return as floating point same as np.zeros()


# lets move on to np.arange() it takes 3 args - > (start,stop,steps) lets look at it in action 

arrange = np.arange(0,20) # ->  without giving steps
print(arrange) # - > [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

arrange1 = np.arange(2,11,2) #- > gives arrays of even number , added steps 
print(arrange1) # - > [ 2  4  6  8 10]


# Array Creation Using np.linspace()
"""
    Here,

    start- the start value of the sequence, 0 by default
    stop- the end value of the sequence (inclusive)
    num(optional)- number of samples to generate (int)


"""
test = np.linspace(1,10,4) # -> it creats array between 1 -10 with 4 elements
print('-------------------------------------------------------------------------------------------------------------------------')


print(test)



"""
    Differences Between np.arange() and np.linspace()
    Both np.arange() and np.linspace() are NumPy functions used to generate numerical sequences, but they have some differences in their behavior.

    arange() generates a sequence of values from start to stop with a given step size whereas linspace generates a sequence of num evenly spaced values from start to stop
    arange() excludes stop value whereas linspace includes stop value unless specified


"""


# NumPy also provides several functions to create random arrays with different distributions.

# The random module provides different functions that allow us to generate random numbers.


#example code ;

random_number = np.random.randint(1,100) # generate number from range 1 - 100 
print(random_number) # - > 24 , 52 ,24, 54, 12, ...etc

# we can also determine the array size using random.randit

#example : 

random_again = np.random.randint(1,100,size=5) #-> size args determine the length of the array ! it can be 1d , 2d and 3d arrays! 
print(random_again) # - > [97 78 50 55  7]

"""
Array Creation Using np.random.rand()
NumPy has the function called np.random.rand() to create an array of random numbers between 0 and 1.

Let's see an example to create an array of 4 random numbers.


"""




# generate an array of 4 random numbers between 0 and 1
array1 = np.random.rand(4)

print(array1)


# Create Empty NumPy Array

empty_array = np.empty(5)

print("Empty Array:", empty_array)


# next lession : numpy arrays