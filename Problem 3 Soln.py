names = ['dog','dear','deal']
pre_names = list()
prefix = input()
for name in names:
    if name.startswith(prefix):
        pre_names.append(name)
print(pre_names)
