''' Startswith & Endswith '''
# l1 = ["Carl", "Sohan", "Sachin", "Rahul"]
#
# for name in l1:
#     if name.startswith("S"):
#         print(f"Hello {name}. Your Name Start With 'S'.")
#
#     if name.endswith("l"):
#         print(f"Hello {name}. Your Name Ends With 'l'.")

"""Separate A list with 2 categories"""
l2 = ["Md. Carl", "Rony Islam", "Md. Sohan", "hoi hoi Islam"]
md = []
islam = []

for i in l2:
    if i.startswith('Md'):
        md.append(i)
    if i.endswith('Islam'):
        islam.append(i)
else:
    print("Separation Completed")
    print('Start with MD list: ', md)
    print('Ends with Islam list: ', islam)
