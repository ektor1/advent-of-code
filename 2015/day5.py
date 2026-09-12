import itertools

def nice_counter(day5_input) -> int:
    n_nice = 0
    vowels = {"a", "e", "i", "o", "u"}
    bad_strings = {"ab", "cd", "pq", "xy"}

    for s in day5_input:
        num_vowels = 0
        no_bad_str = True
        is_twice_letter = False

        for pair in itertools.pairwise(s):
            if pair[0] in vowels:
                num_vowels += 1
            if pair[0] == pair[1]:
                is_twice_letter = True
            if "".join(pair) in bad_strings:
                no_bad_str = False
                break

        if s[-1] in vowels: num_vowels += 1 
        if num_vowels >= 3 and is_twice_letter and no_bad_str:
            n_nice += 1

    return n_nice


def nice_counter_2(day5_input):
    n_nice = 0
    for s in day5_input:
        has_pair = False
        has_repetition = False
        first_pair = {} # {"pair": first pair start index}

        for i in range(len(s) - 1):
            pair = s[i : i+2]
            if pair in first_pair and i - first_pair[pair] >= 2:
                has_pair = True
                break
            elif pair not in first_pair:
                first_pair[pair] = i
            
        for i in range(len(s) - 2):
            beg, eng = s[i], s[i + 2]
            if beg == eng:
                has_repetition = True
                break

        if has_pair and has_repetition:
            n_nice += 1

    return n_nice


def main(data):
    return nice_counter(data), nice_counter_2(data)
