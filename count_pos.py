for i in range(1,45):
    if i<10:
        i = f'0{i}'
    with open(f'brown/ca{i}',"r") as f:
        data = f.read().split()
        words = [w.split("/")[0] for w in data]
        pos = [w.split("/")[-1] for w in data]
        s = set(pos)
        if i==27:
            print(s)
        print(f'length of {i} pos -> {len(s)}')
