import collections
def uniques_only(k):
    seen = set()
    final = []
    for x in k:
        if not isinstance(x, collections.Hashable):
            if set(x) not in final:
                final.append(set(x))
                yield x
        elif x not in seen:
            seen.add(x)
            yield x

if __name__ == "__main__":
    print(list(uniques_only([['a', 'b'], ['a', 'c'], ['a', 'b']])))
