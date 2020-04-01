def flatten_helper(d, flat_d, path):
    if not str(type(d)) == "<class 'dict'>":
        flat_d[path] = d
        return

    for key in d:
        new_keypath = "{}.{}".format(path, key) if path else key
        flatten_helper(d[key], flat_d, new_keypath)


def flatten(d):
    flat_d = dict()
    flatten_helper(d, flat_d, "")
    return flat_d

nest_dict = eval(input())
print(flatten(nest_dict))
