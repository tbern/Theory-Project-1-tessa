# Theory-Project-1
Team name: tessa

Names of all team members: Tessa Berning

Link to github repository: https://github.com/tbern/Theory-Project-1-tessa/tree/main

Which project options were attempted: knapsack coin problem - develop an equivalent of DumbSAT for the coin problem

Approximately total time spent on project: ~5-6 hours

The language you used, and a list of libraries you invoked: python, time, csv, itertools,     matplotlib.pyplot, random, datetime

How would a TA run your program (did you provide a script to run a test case?): run knapsack_input.py to create input files. Then run knapsack.py to create output.csv file (I just included the output.csv file that led to the graph I included but running knapsack.py will rewrite over that one or create a new one). Then run plot.py to create the graph. I don’t have matplotlib installed on my computer with the student machines so I put this into Google Colab and ran it from there. I just had to upload the output.csv file to Colab

A brief description of the key data structures you used, and how the program functioned: 
***************************************************************************************************************

A discussion as to what test cases you added and why you decided to add them (what did they tell you about the correctness of your code). Where did the data come from? (course website, handcrafted, a data generator, other): The data came from a data generator provided by another student in the class and then edited to have a slightly different input that makes more sense with my program

An analysis of the results, such as if timings were called for, which plots showed what? What was the approximate complexity of your program? 
<img width="611" alt="Screen Shot 2024-10-18 at 11 48 37 AM" src="https://github.com/user-attachments/assets/8f05aea4-34e6-4dbf-b691-adb7a120dbab">

The plot shows an exponential graph between the number of variables and the microseconds that it takes to find the result. The approximate time complexity of my program is 2^n

A description of how you managed the code development and testing: 
***************************************************************************************************************

Did you do any extra programs, or attempted any extra test cases: I did a couple of test cases in the main section of knapsack.py
