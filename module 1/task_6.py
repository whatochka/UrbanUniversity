my_dict = {"Kris": 20, "Pickachu": 30, "Nikita": 40}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict["Kris"]}")
print(f"Non existing value: {my_dict.get("not_existing")}")
my_dict["Kirill"] = 34
my_dict.update({"Polina": 88})
print(f"Deleted value: {my_dict.pop("Polina")}")
print(f"Modifed dictionary: {my_dict}")

my_set = {1, 2, 1, "Kirill", "Kirill", "Pasha"}
print(f"\nSet: {my_set}")
my_set.add(34)
my_set.update({"Banana"})
my_set.discard(2)
print(f"Modified set: {my_set}")
