lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500]
]

def find_max():
    results = []
    for index, lists_ in enumerate(lists, start=1):
        maxx = lists_[0]
        minn = lists_[0]
        for num in lists_:
            if num > maxx:
                maxx = num
            if num < minn:
                minn = num
        results.append((index, maxx, minn))
    for index, maxx, minn in results:
        print(f"Max of List{index}: {maxx}, Min of list{index}: {minn}")




def avrg(lists):
    results = []
    for index, lists_ in enumerate(lists, start=1):
        sums = 0
        for num in lists_:
            sums += num
        avg = sums / len(lists_)
        results.append((index, sums, avg))
    for index, sums, avg in results:
        print(f"Sum of List{index}: {sums}, Average of list{index}: {avg}")

avrg(lists)
find_max()
    
    