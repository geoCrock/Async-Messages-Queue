
async def count_x(message: str):

    # Разделение текста по переходам на новую строку
    lines = message.split('\n')

    # Подсчет количества вхождений буквы "X"
    count_of_X = sum(line.count('X') + line.count('x') for line in lines)
    average_of_X_per_line = count_of_X / len(lines) if len(lines) > 0 else 0

    # Вывод результатов
    return average_of_X_per_line
