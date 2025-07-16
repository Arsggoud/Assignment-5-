List = [1,2,3,4,5,6,7,8,10]
List2 = List[0:5]
List2.sort(reverse=True)
print(f"Original List: {List}")
print(f"Extracted first five elements {List2}")
print(f"Reversed extracted elements: {List2}")