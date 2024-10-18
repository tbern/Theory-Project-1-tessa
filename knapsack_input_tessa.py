import random;
from datetime import datetime
def main():
    # create inputs with variable numbers from 1 to 20
    for i in range(1, 20):
        num_vars = i
        with open(f"{num_vars}_coins.txt", "w") as file:
            testcaseTotalValueRange = [[0, 100], [100, 1000], [1000, 10000]]
        # convert float values to ints
            testcaseTotalValueRange = [[int(x[0]), int(x[1])] for x in testcaseTotalValueRange]
        # Set the maximum coin value for the small, medium, and large test cases
        # Default is [25, 25, 25] to make them all 25 cents, but could be changed
            testcaseMaxCoinValue = [25, 25, 25]
        # Set the number of coin values to generate (default is 4)
            numCoins = num_vars
        # Set randomization seed
            random.seed(datetime.now().timestamp())
            for testSize, vals in enumerate(testcaseTotalValueRange):
                for _testcase in range(num_vars):
                    file.write(f"{random.randint(testcaseTotalValueRange[testSize][0], testcaseTotalValueRange[testSize][1])}")
                    for coin in range(numCoins):
                        file.write(f",{random.randint(1, testcaseMaxCoinValue[testSize])}")
                    file.write("\n")
        # Close the file once we are done
            file.close()
if __name__ == '__main__':
    main()
