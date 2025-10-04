"""
We have an array in python that we are trying to reach the end. We have negative numbers,
which take us back a few steps (however many the value says). We change the value of that
index to positive before going back. We should not go back beyond 0. Every step counts as 1, 
regardless if the value is positive or negative. Write python function that calculates total 
steps required to reach end, with example.
"""

# solution 1

def count_steps_to_end(arr):
    current_index = 0
    steps = 0
    n = len(arr)

    while current_index < n:
        steps += 1  # Step count for moving to this index
        value = arr[current_index]

        if value < 0:
            # Calculate new index to move back
            move_back = -value
            new_index = max(0, current_index - move_back)  # Ensure not going below 0
            arr[current_index] = -value  # Change to positive
            current_index = new_index  # Move back
        else:
            # Move to the next index
            current_index += 1

    return steps

# Example
example_array = [3, -1, 4, -2, 1]
total_steps = count_steps_to_end(example_array)
print("Total steps to reach the end:", total_steps)

# solution 2

def calculate_steps_to_reach_end(arr):
  """
  Calculates the total steps required to reach the end of an array,
  considering negative numbers as backward steps.

  Args:
    arr: A list of integers representing the array.

  Returns:
    The total steps required to reach the end of the array.
  """
  current_index = 0
  total_steps = 0
  while current_index < len(arr) - 1:
    next_index = current_index + arr[current_index]
    if arr[current_index] < 0:
      arr[current_index] = abs(arr[current_index])
    if next_index < 0:
      next_index = 0

    total_steps += 1
    current_index = next_index
  return total_steps

# Example usage:
arr = [3, -1, 4, -2, 1]
steps = calculate_steps_to_reach_end(arr)
print(f"Total steps required to reach the end: {steps}")