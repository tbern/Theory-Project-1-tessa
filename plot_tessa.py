import matplotlib.pyplot as plot
import csv

# lists to store data
num_vars = []
times_sat = []
times_unsat = []

# open and read the CSV file
with open('output_tessa.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        # get data from each row
        result = row[0]
        exec_time = float(row[1])
        num_var = int(row[2]) 
        
        num_vars.append(num_var)
        
        # add x,y pairs to the list based on if satisfiable or unsatisfiable
        if result == "Satisfiable":
            times_sat.append((num_var, exec_time))
        else:
            times_unsat.append((num_var, exec_time))

# create  plot
plot.figure(figsize=(10, 6))

# plot satisfiable
plot.scatter(*zip(*times_sat), color='green', marker='o', label="Satisfiable")

# plot unsatisfiable
plot.scatter(*zip(*times_unsat), color='red', marker='x', label="Unsatisfiable")

# add labels and title
plot.xlabel('Number of Variables')
plot.ylabel('Execution Time (seconds)')
plot.title('Execution Time vs Number of Variables')

# add legend
plot.legend()

# display  plot
plot.show()
