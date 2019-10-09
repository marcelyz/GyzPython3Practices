from collections import defaultdict, OrderedDict, Counter, namedtuple, deque


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
    dd = get_count2(strs)
    print(dd)
    print(isinstance(dd, defaultdict), isinstance(dd, dict))  # defaultdict是dict的一个子类

    # OrderedDict:有序dict
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)
    print(isinstance(od, OrderedDict), isinstance(od, dict))  # OrderedDict是dict的一个子类

    # Counter的应用，不用自己对字典排序，代码更简洁
    letter_count_dict = Counter(strs)
    print(isinstance(letter_count_dict, Counter), isinstance(letter_count_dict, dict))  # Counter是dict的一个子类
    strs_count_dict = get_count2(strs)
    print(top_counts(strs_count_dict, 2))
    print(letter_count_dict.most_common(2))

    # namedtuple具备tuple的不变性，又可以根据属性来引用
    Point = namedtuple('Circle', ['x', 'y', 'r'])
    p = Point(1, 2, 5)
    print(p.x, p.y, p.r)
    print(isinstance(p, Point), isinstance(p, tuple))  # namedtuple是tuple的一个子类

    # deque：高效实现插入和删除操作的双向列表; list线性存储，访问快，插入和删除效率低
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)
    q.popleft()
    q.pop()
    print(q)
