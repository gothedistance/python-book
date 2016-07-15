def get_sum(**kargs):
    start = kargs['start']
    end = kargs['end']
    result = 0
    for v in range(start,end + 1):
        result += v
    return result

val = get_sum(start=1,end=10)
print(val)
