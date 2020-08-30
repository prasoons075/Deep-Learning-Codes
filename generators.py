## Basic Code without using Generators ##
def square_numbers(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result

my_nums =square_numbers([1,2,3,4,5])
print(my_nums)

## Code using Generators ##
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums =square_numbers([1,2,3,4,5]) #gives the output in the form of Generator object 
print(my_nums)
print(next(my_nums)) #gives output of sqaure of only 1 when using "next()", so in Generator it calculates values one by one 
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

## We can also use list comprehension for generators
my_nums = (i*i for i in [1,2,3,4,5]) #but this will also return generator object, to see ouput we can use next() or convert the generator object to list().
print(my_nums)

## Why to use generators ?
## It uses less memory and less time
## For more see https://www.youtube.com/watch?v=bD05uGo_sVI