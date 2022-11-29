def check(s, filename):
    s = list(s.split())
    for i in range(len(s)):
        s[i] = s[i].lower()
    dict = {}
    for f in s:
        if f not in dict:
            dict[f] = 1
        else:
            dict[f] += 1
    file = open(filename, "w")

    best_list = []
    for item, value in dict.items():
        best_list.append("{} {}\n".format(item, value))
    best_list.sort()
    # sorted(best_list, key=lambda x: x[0])
    print(best_list)
    for string in best_list:
        file.write(string)

    file.close()