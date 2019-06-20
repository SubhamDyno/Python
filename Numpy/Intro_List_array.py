#importing the numpy 
import numpy as np

list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]

array1 = np.array(list1)

print(f"\nArray1(1-dimensional):\n-------------------\n {array1}");
print(array1.shape)

list3 = [list1,list2];
array2 = np.array(list3)

print(f"\nArray2:(Multi-dimensional)\n--------------------\n {array2}");
print(array2.shape)

list4 = [90, 100]
list5 = [list2, list4]

array3 = np.array(list5)
print(f"\nArray3:(Multi-dimensional List)\n------------------------\n {array3}")
print(array3.shape);


print("np.zeros(3):\n----------------\n " , np.zeros(3))
print("np.ones(5):\n----------------\n " , np.ones(5))
print("np.ones(3,4):\n----------------\n " , np.ones([3,4]))

print("np.eye(3):\n----------------\n" , np.eye(3))

print("np.arange(5):\n----------------\n" , np.arange(5))
print("np.arange(5,10):\n----------------\n" , np.arange(5,10))
print("np.arange(strat=5,end=20,step=3):\n----------------\n" , np.arange(5,20,3))

print("---------Array Operations-------------")
array5 = np.array([list1, [90,100,120,250]]);

print(array2,"\n" ,array5);

print(" Array addition:\n", array1+array5)
print("Array division:\n", array2/array5)

