with open("data/input5-rules.txt", "r") as file:
    rules = file.read().split('\n')[:-1]

with open("data/input5-updates.txt", "r") as file:
    updates = file.read().split('\n')[:-1]


def valid_updates(rules, updates):
    """Create an adjecency list using a hash map where we'll store the small numbers as keys
    and their greater numbers in a hash set as their values"""
    adj_list = {}
    
    # create adjecency list
    for r in rules:
        src, dst = r.split("|")
        src = int(src)
        dst = int(dst)

        if src not in adj_list:
            adj_list[src] = set() 
        if dst not in adj_list:
            adj_list[dst] = set() 
        adj_list[src].add(dst)

    updates = [u.split(",") for u in updates] # 
    updates = [list(map(int, u)) for u in updates] # convert all elements to ints 
    # check which updates are valid
    res = 0
    for u in updates:
        for i in range(len(u) - 1):
            page = u[i]
            adj_page = u[i + 1]

            if adj_page not in adj_list[page]:
                break

        else:
            mid = len(u) // 2
            res += u[mid]

    return res

print(valid_updates(rules, updates))
