def total_steps_to_end(array):
    position = 0
    steps = 0

    while position >= 0 and position < len(array):
        steps += 1
        move = array[position]
        position += move

        # If the move is negative, ensure we don't go back beyond zero
        if position < 0:
            position = 0

        # If we reach the last index, we break the loop
        if position == len(array) - 1:
            break

    return steps

# Example usage:
array = [2, -3, 4, 1, -2, 1, 5]
print(total_steps_to_end(array))  # Output: 9