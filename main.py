# Main file to call the program

import fibonacci

def main():
    # Gets user input from the command line and converts it to an int
    # Needs error checking here
    n = int(raw_input("Please chose which Fibonacci Number you would like to see: "))

    # Fibo function called and printed here
    print fibonacci.fibo(n)

main()
