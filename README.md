# KirboSmash
-A very simplified programming language written in python imitating voices of the famous nintendo character named Kirby!
<br>-Now supports Shell and Scripting both!! POYO!! (Interpreter based model)
<br>-I know; an interpreter inside an interpreter, might be slow and not too efficient but its something I made for fun!

# How to Run Interpreter
Open any code editor or python IDE and then run `shell.py`
# Syntax

The Syntax is based on kirby noises but mixed with english. 

# Keywords
  `letyo`, <br />
  `andpo`, <br />
  `orpo`,<br />
  `nopo`,<br />
  `ifyo`,<br />
  `butpoyo`,<br />
  `elseyo`,<br />
  `foryo`,<br />
  `po`,<br />
  `stepo`,<br />
  `whileyo`,<br />
  `power`,<br />
  `thenpo`,<br />
  `over`,<br />
  `getpo`,<br />
  `cmon`,<br />
  `die`,<br />
  `false`, <br />
  `true`, <br />
  `math_pi`, (pi value)<br />
`say`, BuiltInFunction print<br />
`say_ret`, BuiltInFunction print_ret<br />
`tellme`, BuiltInFunction for input<br />
`tellme_int`, BuiltInFunction for input in integer<br />
`boom`, BuiltInFunction for clear (terminal)<br />
`booms`, BuiltInFunction for mass clear (terminal)<br />
`is_numpo`, BuiltInFunction for checking if number<br />
`is_stringpo`, BuiltInFunction for checking if string<br />
`is_listpo`, BuiltInFunction for checking if list<br />
`is_power`, BuiltInFunction for checking if function exists<br />
`join`, BuiltInFunction for appending<br />
`explode`, BuiltInFunction for pop (stack/list)<br />
`stretch`, BuiltInFunction for extending (arrays or stack)<br />
`len`, BuiltInFunction for length<br />
`go`, BuiltInFunction for running a file<br />

# Comparison Operators

not equal to : `!=`
equals to : `==`
<br /> less than : `<`
<br /> greater than : `>`
<br /> greater than or equal to : `>=`
<br /> less than or equal to : `<=`
<br /> and : `andpo`
<br /> or : `orpo`
<br /> not : `nopo`

# Variable Declaration

`letyo <var_name> = <value>`
<br /><br />
A variable can be declared while performing an operation too, for exmaple:<br />
<br />`poyo> 5 + letyo a = 6`
<br />`11`
<br /> `poyo> a`
<br /> `6`

# If - Else statments 
keywords: `ifyo`, `thenpo`, `elseyo`
<br />
`ifyo <condition> thenpo <process> elseyo <process>`
<br />
<br />
--For Else if statements:
<br />
<br /> keyword: `butpoyo <condition>`
<br /> `ifyo <condition> thenpo <process> butpoyo <condition> thenpo <process> elseyo <process>`

--For blocks of if statements:
<br />
`ifyo <condition> thenpo` <br />
&emsp; `<your_code>` <br />
`over`




# Built-in Functions

Below are the built-in functions available in KirboSmash, along with their syntax and descriptions:

| Function      | Syntax Example                | Description                                                                 |
|---------------|------------------------------|-----------------------------------------------------------------------------|
| `say`         | `say "Hello, Poyo!"`         | Prints the given value to the console.                                      |
| `say_ret`     | `say_ret "Hello, Poyo!"`     | Prints the given value to the console and returns it.                       |
| `tellme`      | `letyo name = tellme{}`      | Prompts the user for input as a string.                                     |
| `tellme_int`  | `letyo age = tellme_int{}`   | Prompts the user for input and converts it to an integer.                   |
| `boom`        | `boom{}`                     | Clears the terminal screen.                                                 |
| `booms`       | `booms{}`                    | Clears the terminal screen multiple times (mass clear).                     |
| `is_numpo`    | `is_numpo{5}`                | Returns `true` if the argument is a number, else `false`.                   |
| `is_stringpo` | `is_stringpo{"kirby"}`       | Returns `true` if the argument is a string, else `false`.                   |
| `is_listpo`   | `is_listpo{[1,2,3]}`         | Returns `true` if the argument is a list, else `false`.                     |
| `is_power`    | `is_power{"myfunc"}`         | Returns `true` if a function with the given name exists, else `false`.      |
| `join`        | `join{[1,2], 3}`             | Appends the second argument to the list (first argument).                   |
| `explode`     | `explode{[1,2,3]}`           | Removes and returns the last element from the list (like pop).              |
| `stretch`     | `stretch{[1,2], [3,4]}`      | Extends the first list with elements from the second list.                  |
| `len`         | `len{[1,2,3]}`               | Returns the length of the list or string.                                   |
| `go`          | `go{"myscript.kirbo"}`       | Runs another KirboSmash script file.                                        |

**Note:** All built-in functions are called directly by their names as shown above. Arguments are provided in parentheses, and return values depend on the function.

# The list is still under progress (sorry hehe)

