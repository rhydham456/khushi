# %% [markdown]
# **Percentage Calculator using advanced modules**
# 

# %%
import numpy as np

# %% [markdown]
# **Creating a program to find percetage of 3 students at once**

# %%
emptyArray = np.empty((3,3))
for arrayindex in range(0,len(emptyArray)):
    for itemindex in range(0,len(emptyArray[arrayindex])):
        emptyArray[arrayindex,itemindex] = int(input(f'enter the marks of student {arrayindex} in subject {itemindex}:'))

# %%
print(emptyArray)
sumArray = emptyArray.sum(axis = 1)
for sumOfNumbers in sumArray:
    print((sumOfNumbers/240)*100)


