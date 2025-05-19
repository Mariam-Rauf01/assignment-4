def get_input(prompt):
    return input(prompt)

def main():
    print("\n🌟✨ Welcome to 'The Mysterious Quest of Wonderville' ✨🌟\n")
    print("Get ready to enter a world of magic, mystery, and unexpected twists!\n")

    # Collecting user input
    name = get_input("🧑 What is your name, brave adventurer? ")
    object_name = get_input("🔮 Name a magical object: ")
    place = get_input("🏰 Name a mysterious place: ")
    color = get_input("🎨 What is your favorite color? ")
    animal = get_input("🐾 Name a wild animal: ")
    funny_phrase = get_input("😹 Say a funny phrase: ")
    huge_object = get_input("🗿 Name something enormous: ")
    action_verb = get_input("🏃 Enter an action verb: ")
    adjective = get_input("🌈 Describe something with an adjective: ")
    creature = get_input("👹 Name a strange creature or person: ")
    dialogue = get_input("💬 Say something dramatic: ")
    past_verb = get_input("🔙 Enter a past tense verb: ")

    # Story begins
    print("\n📜 --- The Enchanted Journey of " + name + " --- 📜\n")
    print(f"In the quiet village of {place}, there lived a curious soul named {name}.")
    print(f"One foggy morning, {name} found a dusty old chest containing a glowing {object_name}.")
    print(f"Suddenly, a {color} {animal} leapt out of the shadows and yelled, '{funny_phrase}!'")

    print(f"\nWithout a second thought, {name} grabbed the {object_name} and began to {action_verb}.")
    print(f"Through thorny woods and over whispering rivers, they arrived at a cliff where a giant {huge_object} loomed.")
    print(f"With a deep breath and a {adjective} heart, {name} approached it.")

    print(f"\nOut of nowhere, a wild {creature} appeared and cried out, '{dialogue}!'")
    print(f"Everything around began to shimmer and shake...")

    print(f"\nIn a dazzling flash of light, the {object_name} lifted {name} into the air!")
    print(f"And just like that, they {past_verb} into legend, their story told across every corner of {place}.")

    print(f"\n✨ The End ✨\n")
    print("Thank you for playing, brave adventurer!\n")

if __name__ == "__main__":
    main()
