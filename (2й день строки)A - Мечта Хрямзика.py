name = input()
fake_name = input()

if name == fake_name:
    print(0)
else:
    pos = (name + name).find(fake_name)
    if pos == -1:
        print(-1)
    else:
        print(len(name) - pos)
