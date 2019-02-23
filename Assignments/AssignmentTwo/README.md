# Assignment Two
>Something something sorting something something searching something something salted

## Goals
To implement sorting, searching, and hashing, and to understand their performance.

## Requirements
- Develop my own implementation of selection sort, insertion sort, merge sort, and quick sort
- Sort using your selection sort. Print the number of swaps.
- Sort using your insertion	sort. Print	the	number of swaps.
- Sort using your merge sort. Print	the	number of swaps.	
- Sort using your quick sort. Print	the	number of swaps.	
- Record your results in a LaTeX document and include the asymptotic running time of each sort and 
explain why it is that way.

&nbsp;

- Develop your own implementation of linear and binary search.	
- Randomly select 42 items.	
- Perform a	linear	search on the sorted array for each	of those randomly	
selected items.	Print the number of comparisons for	each search	and	
compute	the	overall	average.	
- Perform a	binary search on the sorted	array for the same randomly	
selected items.	Print the number of	comparisons	for	each search	and	
compute	the	overall	average.	
- Add your results	to the	LaTeX document,	including the asymptotic	
running	time of	each search	and	why	it is that way.	

&nbsp;

- Develop your own	implementation of a	hash table with chaining.	
- Load the hash table with the items either from the Aile or from your	
array.	
- Retrieve the same	42 randomly	selected items as before from the hash	
table. Print the number	of “search” (get/lookup) calls for each and	
compute	the	overall	average.	
- Add your results to the LaTeX document, including	the	asymptotic	
running	time of	hashing	with chaining and why it is	that way

## Runtime Instructions
One possible issue with how my project is set up (Its a feature, not a bug, I swear) is that some
file paths may not want to cooperate in all environments. In order to fix that the end user (you)
must either do the following two imports at the beginning of the main file:
```python
import sys
sys.path.append("..")
```
and/or remove the paths set up by the file, so change this:
```python
from Assignments.AssignmentTwo.Swap import swap
```
into this:
```python
from Swap import swap
```