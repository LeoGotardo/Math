# Number Multiplication with Regular Expression - Documentation

## Introduction

This Python program allows users to input a sequence of numbers, with or without characters between them, and calculates the multiplication of those numbers using regular expressions.

## How to Use

1. Run the program in your preferred Python environment.
2. Enter the sequence of numbers you want to multiply when prompted by the application. You can include characters between the numbers if you prefer.
3. The program will use regular expressions to extract the numeric values and calculate their multiplication.

## Program Logic

- The program consists of two functions:

### 1. `calc(pri)`

- This function takes a list of strings (`pri`) as input and calculates the multiplication of its numeric elements.
- It starts by initializing variables `n` and `result`, where `n` is the index of the list and `result` holds the cumulative multiplication.
- The function then enters a while loop that iterates over each element of the list.
- If the element is a string containing only digits, it is considered a numeric value, and a nested while loop is entered.
- The nested loop continues until a non-numeric value is encountered or the end of the list is reached. During this loop, the consecutive numeric characters are concatenated to form a full number string.
- The full number string is then converted to an integer, and the multiplication with `result` is performed.
- If the element is not a numeric value, the loop continues without affecting the `result`.
- The loop continues until all elements of the list have been processed.
- The function returns the final `result` after the multiplication is completed.

### 2. `main()`

- This is the main function that interacts with the user and manages the overall flow of the program.
- The user is prompted to enter a sequence of numbers when running the program.
- The program uses regular expressions (`re.findall()`) to find all contiguous numeric substrings in the input. These substrings are stored in the `num_list` variable.
- The program then calls the `calc` function, passing the `num_list` as an argument, to calculate the multiplication.
- Finally, the result of the multiplication is displayed.

## Example Usage

```
Digite os numeros da multipliacao: 1, 2, 3, 4
['1', '2', '3', '4']
24
```

```
Digite os numeros da multipliacao: 5 - 10 - 2
['5', '10', '2']
100
```

## Note

- The program demonstrates a simple number multiplication application that handles numeric inputs with or without characters between them using regular expressions.
- Regular expressions allow for more flexibility in finding numeric substrings in the input, making the program more robust to handle various input formats.