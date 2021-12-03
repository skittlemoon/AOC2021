#with open("data.txt") as file:
#    depth = [int(line) for line in file]

#count = 0
#for i in range(3, len(depth)):
#    if depth[i - 3] + depths[i - 2] + depth[i - 1] < depth[i - 2] + depth[i - 1] + depth[i]:
#        count += 1

#print(count)

from itertools import islice, tee

SlidingWindow = 3

with open("data.txt") as file:
   depth = (int(line) for line in file)

   prev_iter, iter = tee(depth, 2)    # Split iterator in two.
   next_iter = islice(iter, SlidingWindow, None)  # Skip window elements from this iterator. 

   count = 0
   for prev_, next_ in zip(prev_iter, next_iter):
    if prev_ < next_:
        count += 1

   print(count)

