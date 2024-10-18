import time
import csv
import itertools

def tester():
# reads the input from the text file, calls can_make_amount, writes to the output file
    coins = []
    with open("output.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        # cycle through 1 to 20 variables
        for i in range(1, 20):
            num_vars = i
            # open the associated text file
            with open(f"{num_vars}_coins.txt", "r") as file:
                for line in file:
                    # read in the target number and the coins
                    values = line.strip().split(',')
                    target = int(values[0])
                    coins = list(map(int, values[1:]))
                    # take the start time before running the function
                    start_time = time.time()
                    #run the function that finds if the coins can add up to a certain amount
                    result = can_make_amount(coins, target)
                    # take the end time
                    end_time = time.time()
                    # find the total time (in microseconds)
                    total_time = int((end_time - start_time)*1e6)
                    # assign satisfiable or unsatisfiable
                    if result:
                        sat = "Satisfiable"
                    else:
                        sat = "Unsatisfiable"

                    # write to output file
                    writer.writerow([sat, total_time, num_vars])
            # close the files
            file.close()
        csvfile.close()


def can_make_amount(coins, target):
    # find all of the possible combinations of all possible lengths of the coins
    for r in range(len(coins) + 1):
        for option in itertools.combinations(coins, r):
            # sum up the combination and see if it equals the target
            if sum(option) == target:
                # if it does, return true. if not, move on to the next combination
                print(option)
                return True
    # if we have tried all combinations and it doesn't work, return false
    print("no possible combination")
    return False

if __name__ == '__main__':
    # coins = [3, 5, 8, 11]
    # target = 16
    # print(can_make_amount(coins, target))
    # # returns True
    # target = 30
    # print(can_make_amount(coins, target))
    # # returns False
    tester()
