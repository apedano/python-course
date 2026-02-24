# 🐍 Lists

| Collection Type | Ordered | Mutable | Allows Duplicates | Indexed Access | Key-Value | Syntax Example | Notes                                      |
|-----------------|---------|---------|-------------------|----------------|-----------|----------------|--------------------------------------------|
| list            | Yes     | Yes     | Yes               | Yes            | No        | [1, 2, 3]      | Dynamic array, most commonly used sequence |

## Initialization

```python
# Size of the list
n = 5

# Creating a list of size n filled with 0
a = [""] * n
```

```python

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
```

## Indexing

```python
print(states_of_america[0])  # Delaware
print(states_of_america[-1])  # Hawaay
```

## Modification

```python
states_of_america[1] = "Pencilvania"
```

## Addition

```python
# Append element
states_of_america.append("Angelaland")
print(states_of_america)

# Add a list

states_of_america.extend(["Groenland", "Sicily"])

```
## Slicing

```python

list[start:stop:step]

```

`start` → index to begin (**inclusive**)

`stop` → index to end (**exclusive**)

`step` → how many steps to move

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4]) #[20, 30, 40]
```
```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])   # From start to index 2
print(numbers[2:])   # From index 2 to end
print(numbers[:])    # Whole list copy
```
```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2]) #[10, 30, 50]
```

```python
numbers = [10, 20, 30, 40, 50]

#Counts from the end.
print(numbers[-3:]) #[30, 40, 50]
```

```python
numbers = [1, 2, 3, 4, 5]

#reverse list
print(numbers[::-1]) #[5, 4, 3, 2, 1] 
```

## Merging

```python
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
other_friends = ["Ciccio", "Pasticcio"]
all_friends = friends + other_friends
```

## Presence check

```python
[player_choice, computer_choice] in wins
```

```python
options = [rock, paper, scissors]
wins = [[rock, scissors], [paper, rock], [scissors, paper]]

player_choice_index = int(input("What is your choice [1=rock, 2=paper, 3=scissors]? ]?")) - 1
player_choice = options[player_choice_index]
computer_choice = random.choice(options)

print(f"Your choice is {player_choice}, computer choice is {computer_choice}")

if player_choice == computer_choice:
    print("It's a draw. No one wins!")
elif [player_choice, computer_choice] in wins:
    print("You win!")
else:
    print("Computer wins!")
```

## Join

```python
letters = ["a", "b", "c"]

delimiter = " "

string = "".join(letters)  # a b c

```

| Function       | Description |
|----------------|-------------|
| `len(friends)` | Size        |

## Additional functions

[Documentation on list functions](https://docs.python.org/3/tutorial/datastructures.html)

## Nesting lists 

```python
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1]) #D
```

