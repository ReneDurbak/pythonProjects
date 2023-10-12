import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()




def collatz_calc():
    number = int(input("Enter a number: "))
    arrOfNumbers = []
    no_Of_iterations = 0

    while number!=1:
        if number > 1 and number < 1000:
            if (number % 2) == 0:
                number = int(number / 2)
                arrOfNumbers.append(number)
                print(number)
                no_Of_iterations += 1
            else:
                number = int(3 * number + 1)
                arrOfNumbers.append(number)
                print(number)
                no_Of_iterations += 1
    
    print("Number of iterations: ", no_Of_iterations)
    print(arrOfNumbers)

        

collatz_calc()