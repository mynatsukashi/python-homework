shopping_list = ['lettuce','egg','tomato','cucumber','oil', 'oil']

word = input("Choose: ").strip().lower()

if word in shopping_list:
    print(f"Yes - {word} is on the list ({shopping_list.count(word)} times)")
else:
    print(f"No - {word} is not on the list")
