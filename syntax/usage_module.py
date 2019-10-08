from collections import defaultdict, Counter


def get_count(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_count2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n=10):
    return sorted(list(count_dict.items()), key=lambda x: x[1], reverse=True)[:n]


if __name__ == "__main__":
    # defaultdict的应用，不用考虑key不存在的情况，代码更简洁
    strs = ['a', 'b', 'a', 'c', 'a', 'c', 'a', 'd']
    print(get_count(strs))
    print(get_count2(strs))

    # Counter的应用，不用自己对字典排序，代码更简洁
    letter_count_dcit = Counter(strs)
    strs_count_dict = get_count2(strs)
    print(top_counts(strs_count_dict, 2))
    print(letter_count_dcit.most_common(2))



