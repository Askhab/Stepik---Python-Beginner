# NUMERICAL GUESSING GAME
# Project description: The program generates a random number in the range from 11 to 100100 and asks the user to guess this number. If the user's guess is greater than the random number, then the program should display the message 'Too much, try again'. If the guess is less than the random number, then the program should display the message 'Too small, try again'. If the user guesses the number, then the program should congratulate him and display the message 'You guessed it, congratulations!'.

# Project components:

# - Integers (type int);
# - Variables;
# - Data input / output (functions input() and print());
# - Conditional statement (if/elif/else);
# - while() loop;
# - Endless cycle;
# - Statements break, continue;
# - Working with the random module to generate random numbers.


# OPTIMAL NUMBER GUESSING STRATEGY
# Guaranteed to guess the intended number from 11 to 100100 will require no more than 77 attempts.

# OPTIMAL GUESSING ALGORITHM: let left = 1 and right = 100.

# - We call the number equal to middle = (left + right) // 2;
# - If the number middle equal to the intended number, then we guessed it!;
# - If the number middle less than the intended number, then we put left = middle + 1 and continue the algorithm;
# - If the middle number greater than the intended number, then we set right = middle - 1 and continue the algorithm.

# Since at each iteration we discard half of the numbers, we are guaranteed to guess the intended number for a value equal to log_2 n (binary logarithm) rounded up to an integer. With n=100n=100 we get 77 attempts.

# Note 1.  The math module contains a function that calculates the binary logarithm.
