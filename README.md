# MSCS532A6- Medians and Order Statistics & Elementary Data Structures
Umesh Dhakal <br />
MSCS532A6 <br /> 
<br />
This repository contains two Python files: <br />
MSCS532A6PART1.py <br />
This file includes the implementation of the Randomized Quickselect algorithm and the Deterministic Median-of-Medians selection algorithm.<br />
The program also measures the execution time and memory usage for four different datasets, like Sorted Data, Reverse Data, and Random Data , Repeated Data <br /><br />
MSCS532A6PART2.py<br />
This file includes the implementation of the basic data structures such as Arrays, Matrices, Stacks, Queues, and Singly Linked Lists.<br /><br />
Output is included in the pdf file. <br />
For both the implementation, I use Visual Studio Code <br />
For part 1 <br />
python MSCS532A6PART1.py <br />
It executes both the randomized selection and deterministic selection algorithms on all four datasets and prints the running time and memory usage for each dataset.<br /><br />
For Part 2 <br />
python MSCS532A6PART2.py <br />
It runs a short demo of all the data structures and prints the all the results as shown in the pdf file.<br /> <br />
Summary of Findings<br />
From the result analysis of randomized and deterministic algorithm both selection algorithms showed efficient performance. The deterministic Median-of-Medians algorithm was more stable and gave predictable results across all datasets because it always chooses a safe pivot.
The randomized Quickselect algorithm also performed very well and was fastest on random and repeated data, but sometimes took slightly longer depending on the pivot it choose. <br /><br />
In Part 2, we built arrays, matrices, stacks, queues, and linked lists from scratch. For direct access Array were fast, stacks on arrays performed well, queues on arrays were slower for removals, and linked lists were helpful when inserting and deleting often. Each structure has strengths depending on how the data is used.
