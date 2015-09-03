import timeit

s_list_map = {
    'stmt': 'list(map(hex, range(10000)))'
}

s_list_comp = {
    'stmt': '[hex(x) for x in range(10000)]'
}

s_list_map_lambda = {
    'stmt': 'list(map(lambda x: x+2, range(10000)))'
}

s_list_comp_lambda = {
    'stmt': '[x+2 for x in range(10000)]'
}

s_list_filter_mod_lambda = {
    'stmt': 'list(filter(lambda x: x%2, range(10000)))'
}

s_list_comp_mod = {
    'stmt': '[x for x in range(10000) if x%2]'
}

s_append = {
    'setup': 'l = []',
    'stmt': 'l.append(1); l.append(1)'
}

s_extend = {
    'setup': 'l = []',
    'stmt': 'l.extend([1, 1])'
}

s_extend_plus = {
    'setup': 'l = []',
    'stmt': 'l += [1, 1]'
}

if __name__ == '__main__':

    extra_params = {'number': 1000000}

    s1 = s_extend
    s2 = s_extend_plus

    s1.update(extra_params)
    s2.update(extra_params)

    name1 = next(filter(lambda i: s1 is i[1] and i[0] is not 's1', locals().items()))[0]
    name2 = next(filter(lambda i: s2 is i[1] and i[0] is not 's2', locals().items()))[0]

    t1 = timeit.timeit(**s1)
    t2 = timeit.timeit(**s2)

    print('{} took {}'.format(name1, t1))
    print('{} took {}'.format(name2, t2))