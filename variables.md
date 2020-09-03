# Background information: Variables

In this exercise you will learn about:

- The difference between variables in Math and CS
- Creating and naming a variable
- Assigning a value to a variable
- Getting user input for a variable

## What is a Variable?
In computer programming, a **variable** is a container that holds numbers, words, or other types of data to use in our program. Variables in programming are similar to the variables we use in math class, since they both represent a value. Unlike variables in math, variables in programming do not represent an "unknown", and hold values that can change as the program executes.

Another difference is in variable names. In math, variables are only one letter long, as in *x*, or *y*, or *n*. In most programming languages, variable names can be a single letter, a word or a phrase (as long as there are no spaces). In fact, it's considered good programming practice to use variable names that represent the data they are being used to store.

For instance, we might store a name in a variable `name`, and an age in a variable `age`. We can combine multiple words with underscores, such as `student_name`, and `teacher_name`. But if we create a variable name with a space in it, such as `student name`, our program won't understand what we want it to do!

## Defining a Variable
In the Python programming language, we have to create (or _declare_) a variable before we can use it. We do this by telling the program the name of our variable and setting it equal to something. The type of the variable (str, int, float, bool) will depend on the type we use to declare it.

```
name = 'Mateo'
age = 16
speed = 6.51
```

This defines the variable `name` a string (str), age as an integer (int), and speed as a float. 

The `=` sign here works differently than it does in your math class. In programming, `=` means assignment, not equality. It says to the computer: `age` gets 16.

Assignment always works from right to left. In other words, the value on the right side of the `=` is evaluated first and then stored in the variable whose name is on the left side of the `=`.

If you use a variable before defining it, you can generate errors or have unexpected results (depending on how you are attempting to use it).



One thing that look strange to most people who start programming for the first time, is an expression like:

```python
age = age + 1
```

In math class, we know this can never be true! How can age equal itself plus one?

But if we remember that the `=` represents assignment, and not equality, we can read this as: evaluate the result of adding one to the value stored in `age`, then reassign this new value to `age`.

Keep in mind when we write a statement like this, we must have already assigned an initial value to `age`. In other words:

```python
age = age + 1
```

will generate an error, because `age` has not yet been defined.

Instead, we'll assign a starting value to `age` and then increase it by one:

```python
age = 16
age = age + 1
```

Now, `age` will have a value of 17.

## Getting User Input

So we've seen how we can code values into a variable by typing them into our program, but what if we want a use a different value for a variable each time we run it?

In this case we can use Python's user input function (`input()`), to prompt for a value in the terminal.

```python
age = input("Enter Your Age: ")
```

Note that `input()` takes use input as a string type, no matter what the user types. If you ask for the user's age and they type `10 ` then Python will assign the string `"1-"` to `age`.

`age = "10"`
 If you want to store it differently, you need to tell Python what data type you want. For example:
 
 ```python
 age = int(input('Enter your age: ')`
 ```
 
 or
 ```python
 age = input('Enter your age: ')
 age = int(age)
 ```

The first example collects the input, converts it to an integer, and then assigns that value to `age`. The second collects the input as a string and assigns it to `age` without converting it. In the next line, the value of `age` is converted to an integer and the new type is reassigned to `age`.

Both examples are valid and have their uses.

