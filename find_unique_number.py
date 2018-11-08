def find_uniq(arr):
    unique_number = [float(x) for x in arr if arr.count(x) == 1]
    return round(float(unique_number[0]),2)

print(find_uniq(([ 1, 1, 1, 2, 1, 1 ])))
find_uniq([ 0, 0, 0.55, 0, 0 ])
