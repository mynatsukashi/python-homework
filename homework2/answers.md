Homework #2 
1. What does the input() function do? What data type does it always return — even if the user types 42?
Input() function asks the question and expects the output. It always returns string data, even if the user types numeric value. 
2. Why do we often wrap input() in int(...) or float(...)? What goes wrong if we forget to?
We do it because input() by default returns only string values, and if we want to get only numbers or decimal, we need to wrap input() in it. If we forget to wrap it, our data might be inaccurate due to mistakes that users will make. For example, typing letter in input for age. 
3. What does the type() function tell you, and why is it handy when something is not behaving the way you expect?
Type() helps to identify the data type, and it's useful for the cases when we get an error in the output. 
4. What do the string methods .upper(), .lower(), and .strip() each do? Give a short example for one of them.
.upper() returns words in uppercase (NATALI NASIDZE),
.lower() returns words in lowercase (natali nasidze),
.title() returns a book-style output (Natali Nasidze).
5. What do the escape sequences \n and \t mean inside a string?
\n - in the newline escape character.
\t - tab space.
6. A comparison like age >= 18 produces a value. What data type is that value?
That value is boolean, either "True" or "False"
7. Why is bool("") False, but bool("0") and bool(" ") are both True? (Hint: think about empty versus not empty.)
bool("") is false because it has no value in it, meanwhile other option have values like "0"(str), " "(space).
8. Why does 0.1 + 0.2 == 0.3 print False? What is round() useful for here?
Because Python struggles working with decimal numbers, as it stores numbers in bytes. Round helps to cut the number like this: 0.33333333334 => 0.3
9. Some programmers write names like MAX_SCORE in ALL_CAPS. What does that naming convention signal to other programmers, and why shouldn't you change such a value later?
CAPS variables are constant and it's not recommended to change it. You can change the primary value, however changing constant later considered as a mistake. 