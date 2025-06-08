##### ДЗ. Тема 4. Алгоритми сортування



### Завдання 1

'''
Додайте метод delete для видалення пар ключ-значення таблиці HashTable , яка реалізована в конспекті.

Критерії виконання:
Код виконується, і метод delete видаляє задану пару ключ-значення в таблиці HashTable.
'''

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(self.size)]

#     def hash_function(self, key):
#         return hash(key) % self.size         # (див. нижче) функція, яка приймає ключ і повертає індекс у хеш-таблиці. Він використовує вбудовану функцію hash Python, щоб отримати хеш ключа, а потім бере остачу від ділення цього хешу на розмір таблиці self.size. використовує вбудовану хеш-функцію Python для створення хешу ключа, атрибут size обмежує значення хешу розміром таблиці.

#     def insert(self, key, value):
#         key_hash = self.hash_function(key)
#         key_value = [key, value]

#         if self.table[key_hash] is None:
#             self.table[key_hash] = list([key_value])
#             return True
#         else:
#             for pair in self.table[key_hash]:
#                 if pair[0] == key:
#                     pair[1] = value
#                     return True
#             self.table[key_hash].append(key_value)
#             return True

#     def get(self, key):
#         key_hash = self.hash_function(key)
#         if self.table[key_hash] is not None:
#             for pair in self.table[key_hash]:
#                 if pair[0] == key:
#                     return pair[1]
#         return None
    
#     def delete(self, key):
#         key_hash = self.hash_function(key)
#         bucket = self.table[key_hash]      # Працює не з None, а з підсписком bucket, який завжди є списком (може бути порожній).
#         for i, pair in enumerate(bucket):
#             if pair[0] == key:             # Шукає потрібний ключ у цьому списку.
#                 del bucket[i]              # Видаляє лише пару [key, value], а не всю "комірку".
#                 return True
#         return False

    
# # Тестуємо нашу хеш-таблицю:
# H = HashTable(5)
# print(H.table)
# '''[[], [], [], [], []]'''

# H.insert("apple", 10)
# H.insert("orange", 20)
# H.insert("banana", 30)

# print(H.table)
# '''
# [[['banana', 30]], [], [['orange', 20]], [['apple', 10]], []]
# '''

# print(H.get("apple"))   # Виведе: 10
# print(H.get("orange"))  # Виведе: 20
# print(H.get("banana"))  # Виведе: 30

# H.delete("apple")
# H.delete("grape")
# print(H.table)

'''
[[['banana', 30]], [], [], [['orange', 20]], []]
'''



### Завдання 2

'''
Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами. 
Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. 
Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.

Критерії виконання:
Виконання коду повертає кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. 
Другим елементом є "верхня межа" (найменший елемент, який є більшим або рівним заданому значенню).
'''

# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     step = 0
#     upper_bound = None

#     while low <= high:
#         step += 1
#         mid = (low + high) // 2

#         if arr[mid] < x:
#             low = mid + 1
#         else:
#             # записуємо можливу верхню межу
#             upper_bound = arr[mid]
#             high = mid - 1

#     return (step, upper_bound)



# arr = [2.4, 3.1, 4.5, 10.6, 40.3]
# x = 11
# result = binary_search(arr, x)

# print(result)




### Завдання 3

'''
Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). 
Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: 
одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). 
На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.

Критерії прийняття:
Програмно реалізовано алгоритми пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа.
На основі виконання кожного з трьох алгоритмів визначено найшвидший алгоритм для кожного з двох текстів.
Зроблено висновки щодо швидкостей алгоритмів для кожного тексту окремо та в цілому. Висновки оформлено у вигляді документа формату markdown.
'''


## Алгоритм Кнута-Морріса-Пратта (КМП)

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

'''
raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."
pattern = "алг"
print(kmp_search(raw, pattern))
'''

## Алгоритм Боєра-Мура 

def build_shift_table(pattern):
  """Створити таблицю зсувів для алгоритму Боєра-Мура."""
  table = {}
  length = len(pattern)
  # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(text, pattern):
  # Створюємо таблицю зсувів для патерну (підрядка)
  shift_table = build_shift_table(pattern)
  i = 0 # Ініціалізуємо початковий індекс для основного тексту

  # Проходимо по основному тексту, порівнюючи з підрядком
  while i <= len(text) - len(pattern):
    j = len(pattern) - 1 # Починаємо з кінця підрядка

    # Порівнюємо символи від кінця підрядка до його початку
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1 # Зсуваємось до початку підрядка

    # Якщо весь підрядок збігається, повертаємо його позицію в тексті
    if j < 0:
      return i # Підрядок знайдено

    # Зсуваємо індекс i на основі таблиці зсувів
    # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  # Якщо підрядок не знайдено, повертаємо -1
  return -1

'''
text = "Being a developer is not easy"
pattern = "developer"

position = boyer_moore_search(text, pattern)
if position != -1:
  print(f"Substring found at index {position}")
else:
  print("Substring not found")
'''


##  Алгоритм Рабіна-Карпа

def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Базове число для хешування та модуль
    base = 256 
    modulus = 101  
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

'''
main_string = "Being a developer is not easy"
substring = "developer"

position = rabin_karp_search(main_string, substring)
if position != -1:
    print(f"Substring found at index {position}")
else:
    print("Substring not found")
'''



## Зчитування файлів для тесту

with open('стаття 1.txt', 'r') as file:
    text1 = file.read().lower()
    # print(text1)

with open('стаття 2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read().lower()
    # print(text2)

pattern_exist = 'алгоритм'
pattern_non_exist = 'заявка'



# kmp_search(main_string, pattern)
# boyer_moore_search(text, pattern)
# rabin_karp_search(main_string, substring)


# Замір часу виконання алгоритму

import timeit
import numpy as np

def measure_time(search_func, text, pattern):
    start_time = timeit.default_timer()
    search_data = search_func(text, pattern) # сортуємо не сам масив даних, а його копію, щоб початковий масив даних залишався незмінним при використанні інших методів сортування
    end_time = timeit.default_timer() - start_time
    return end_time

def main():
    print('EXISTING pattern measure time:')

    kmp_search_text1 = measure_time(kmp_search, text1, pattern_exist)
    kmp_search_text2 = measure_time(kmp_search, text2, pattern_exist)
    kmp_search_mean_time = np.average([kmp_search_text1, kmp_search_text2])
    print(2 * ' ' + f'{kmp_search_mean_time:.7f} kmp_search mean search time of existing pattern for 2 files')
    print(4 * ' ' + f'{kmp_search_text1:.7f} kmp_search_text1 search time of existing pattern for 1-st file')
    print(4 * ' ' + f'{kmp_search_text2:.7f} kmp_search_text1 search time of existing pattern for 2-nd file')

    boyer_moore_search_text1 = measure_time(boyer_moore_search, text1, pattern_exist)
    boyer_moore_search_text2 = measure_time(boyer_moore_search, text2, pattern_exist)
    boyer_moore_search_mean_time = np.average([boyer_moore_search_text1, boyer_moore_search_text2])
    print(2 * ' ' + f'{boyer_moore_search_mean_time:.7f} boyer_moore_search mean search time of existing pattern for 2 files')
    print(4 * ' ' + f'{boyer_moore_search_text1:.7f} boyer_moore_search_text1 search time of existing pattern for 1-st file')
    print(4 * ' ' + f'{boyer_moore_search_text2:.7f} boyer_moore_search_text1 search time of existing pattern for 2-nd file')

    rabin_karp_search_text1 = measure_time(rabin_karp_search, text1, pattern_exist)
    rabin_karp_search_text2 = measure_time(rabin_karp_search, text2, pattern_exist)
    rabin_karp_search_mean_time = np.average([rabin_karp_search_text1, rabin_karp_search_text2])
    print(2 * ' ' + f'{rabin_karp_search_mean_time:.7f} rabin_karp_search mean search time of existing pattern for 2 files')
    print(4 * ' ' + f'{rabin_karp_search_text1:.7f} rabin_karp_search_text1 search time of existing pattern for 1-st file')
    print(4 * ' ' + f'{rabin_karp_search_text2:.7f} rabin_karp_search_text1 search time of existing pattern for 2-nd file \n')
    

    print('NON-EXISTING pattern measure time:')
    
    kmp_search_text1_n = measure_time(kmp_search, text1, pattern_non_exist)
    kmp_search_text2_n = measure_time(kmp_search, text2, pattern_non_exist)
    kmp_search_mean_time_n = np.average([kmp_search_text1_n, kmp_search_text2_n])
    print(2 * ' ' + f'{kmp_search_mean_time_n:.7f} kmp_search mean search time of non-existing pattern for 2 files')
    print(4 * ' ' + f'{kmp_search_text1_n:.7f} kmp_search_text1 search time of non-existing pattern for 1-st file')
    print(4 * ' ' + f'{kmp_search_text2_n:.7f} kmp_search_text1 search time of non-existing pattern for 2-nd file')

    boyer_moore_search_text1_n = measure_time(boyer_moore_search, text1, pattern_non_exist)
    boyer_moore_search_text2_n = measure_time(boyer_moore_search, text2, pattern_non_exist)
    boyer_moore_search_mean_time_n = np.average([boyer_moore_search_text1_n, boyer_moore_search_text2_n])
    print(2 * ' ' + f'{boyer_moore_search_mean_time_n:.7f} boyer_moore_search mean search time of non-existing pattern for 2 files')
    print(4 * ' ' + f'{boyer_moore_search_text1_n:.7f} boyer_moore_search_text1 search time of non-existing pattern for 1-st file')
    print(4 * ' ' + f'{boyer_moore_search_text2_n:.7f} boyer_moore_search_text1 search time of non-existing pattern for 2-nd file')

    rabin_karp_search_text1_n = measure_time(rabin_karp_search, text1, pattern_non_exist)
    rabin_karp_search_text2_n = measure_time(rabin_karp_search, text2, pattern_non_exist)
    rabin_karp_search_mean_time_n = np.average([rabin_karp_search_text1_n, rabin_karp_search_text2_n])
    print(2 * ' ' + f'{rabin_karp_search_mean_time_n:.7f} rabin_karp_search mean search time of non-existing pattern for 2 files')
    print(4 * ' ' + f'{rabin_karp_search_text1_n:.7f} rabin_karp_search_text1 search time of non-existing pattern for 1-st file')
    print(4 * ' ' + f'{rabin_karp_search_text2_n:.7f} rabin_karp_search_text1 search time of non-existing pattern for 2-nd file \n')    


    print('Mean for EXISTING pattern and NON-EXISTING pattern measure time:')
    
    kmp_exs_n =          np.average([kmp_search_text1, kmp_search_text1_n])
    boyer_moore_exs_n =  np.average([boyer_moore_search_text1, boyer_moore_search_text1_n])
    rabin_karp_exs_n =   np.average([rabin_karp_search_text1, rabin_karp_search_text1_n])

    print(f'{kmp_exs_n:.7f} kmp_search mean search time of EXISTING pattern and NON-EXISTING pattern for 2 files')
    print(f'{boyer_moore_exs_n:.7f} boyer_moore_search mean search time of EXISTING pattern and NON-EXISTING pattern for 2 files')
    print(f'{rabin_karp_exs_n:.7f} rabin_karp_search mean search time of EXISTING pattern and NON-EXISTING pattern for 2 files')



if __name__ == "__main__":
    main()


### Висновки:
# У цілому беручи до уваги середній час пошуку як існуючого так і неіснуючого підрядка в 2-х файлах найефективнішим є алгоритм Боєра-Мура, на другому місці алгоритм Кнута-Морріса-Пратта, на третьому алгоритм Рабіна-Карпа
  # Таким чином для існуючого підрядку в цілому (середній час пошуку по 2-х файлах) найефективнішим алгоритмом пошуку виявився алгоритм Боєра-Мура, на другому місці алгоритм Рабіна-Карпа, на третьому алгоритм Кнута-Морріса-Пратта 
    # водночас для першого тексту у пошуку існуючого підрядку найшвидшим виявився алгоритм Боєра-Мура, на другому місці алгоритм Рабіна-Карпа, на третьому алгоритм Кнута-Морріса-Пратта
    # тоді як для другого тексту у пошуку існуючого підрядку найшвидшим виявився алгоритм Боєра-Мура, на другому місці алгоритм Рабіна-Карпа, на третьому алгоритм Кнута-Морріса-Пратта
  # У той же час для неіснуючого підрядку в цілому (середній час пошуку по 2-х файлах) найефективнішим алгоритмом пошуку виявився алгоритм Боєра-Мура, на другому місці алгоритм Кнута-Морріса-Пратта, на третьому алгоритм Рабіна-Карпа
    # водночас для першого тексту у пошуку неіснуючого підрядку найшвидшим виявився алгоритм Боєра-Мура, на другому місці алгоритм Кнута-Морріса-Пратта, на третьому алгоритм Рабіна-Карпа
    # тоді як для другого тексту у пошуку неіснуючого підрядку найшвидшим виявився алгоритм Боєра-Мура, на другому місці алгоритм Кнута-Морріса-Пратта, на третьому алгоритм Рабіна-Карпа
