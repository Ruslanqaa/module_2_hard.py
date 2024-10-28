def generate_password(n):
    result = ""

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"

    return result


# Пример использования
n = 9  # Замените это число на желаемое (от 3 до 20)
password = generate_password(n)
print(f"Пароль для числа {n}: {password}")