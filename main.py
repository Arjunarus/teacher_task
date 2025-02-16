from __future__ import annotations

AGE_RANGE = range(2, 100)
ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"


def _is_simple(x: int) -> bool:
    if x == 1:
        return False

    for divider in range(2, x//2 + 1):
        if x % divider == 0:
            return False
    return True


def _get_not_simple_dividers(age: int) -> list[int]:
    res = []
    for divider in range(1, age + 1):
        if age % divider != 0:
            continue

        if _is_simple(divider):
            continue

        res.append(divider)

    return res


def _get_possible_names(number_value: int) -> list[str]:
    res = []
    for letter_number_size in (1, 2):
        k = 10 ** letter_number_size
        last_letter_number = number_value % k - 1
        if last_letter_number not in range(len(ALPHABET)):
            continue

        last_letter = ALPHABET[last_letter_number]
        if number_value // k == 0:
            res.append(last_letter)
            return res

        prefixes = _get_possible_names(number_value // k)
        for name in prefixes:
            res.append(name + last_letter)

    return res


def main():
    for age in AGE_RANGE:
        not_simple_dividers = _get_not_simple_dividers(age)
        if len(not_simple_dividers) == 0:
            continue

        sum_of_cubes = sum(map(lambda x: x ** 3, not_simple_dividers))
        names = _get_possible_names(sum_of_cubes)
        if not names:
            continue

        print(f"Age {age}, dividers {not_simple_dividers}, sum of cubes {sum_of_cubes}, names: {names}")


if __name__ == "__main__":
    main()
