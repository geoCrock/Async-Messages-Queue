async def count_x(message: str):

    # Splitting text using newlines
    lines = message.split('\n')

    # Counting the number of occurrences of the letter "X"
    count_of_X = sum(line.count('X') + line.count('x') for line in lines)
    average_of_X_per_line = count_of_X / len(lines) if len(lines) > 0 else 0

    # Output of results
    return average_of_X_per_line
