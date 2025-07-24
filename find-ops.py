import pandas as pd
import random
import time
import sys
import itertools

def find_combination_randomized(csv_path, target_sum, num_operations, timeout=60.0):

    df = pd.read_csv(csv_path)

    if 'id' not in df.columns or 'amount' not in df.columns:
        raise ValueError("CSV must contain 'id' and 'amount' columns")

    # округлим суммы до копеек
    # df['amount'] = df['amount'].round(2)
    # df['amount'] = df['amount'].astype(float).round(2)
    df['amount'] = df['amount'].astype(int)

    records = df.to_dict('records')

    n = len(records)
    print("records", n)

    if n < num_operations:
        print("Record count not enough")
        return None

    start_time = time.time()
    attempts = 0

    # 🔍 Если данных мало — делаем полный перебор
    if n <= 500:  # регулируй по необходимости
        for combo in itertools.combinations(records, num_operations):
            attempts += 1
            if time.time() - start_time > timeout:
                print(f"Не удалось найти комбинацию за {attempts} попыток и {timeout} сек.")
                break
            # total = round(sum(item['amount'] for item in combo), 2)
            total = sum(item['amount'] for item in combo)
            # if total == round(target_sum, 2):
            # if abs(total - target_sum) < 0.01:
            if total == target_sum:
                return [item['id'] for item in combo]
        return None

    # 🔄 Random Sampling (если данных много)
    while time.time() - start_time < timeout:
        attempts += 1
        sample = random.sample(records, num_operations)
        # total = round(sum(item['amount'] for item in sample), 2)
        total = sum(item['amount'] for item in sample)
        # if total == round(target_sum, 2):
        # if abs(total - target_sum) < 0.01:
        if total == target_sum:
            print(f"Найдено за {attempts} попыток")
            return [item['id'] for item in sample]

    print(f"Не удалось найти комбинацию за {attempts} попыток и {timeout} сек.")
    return None


def get_arg(num):
    if len(sys.argv) > num:
        return sys.argv[num]
    return None


if __name__ == "__main__":
    csv_file = get_arg(1)              # путь к CSV-файлу
    target = float(get_arg(2))         # целевая сумма
    count = int(get_arg(3))            # нужное количество 

    result = find_combination_randomized(csv_file, target, count, 120)

    if result:
        print("ID подходящих операций:", result)
    else:
        print("Комбинация не найдена.")
