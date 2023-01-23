def info(**students):
    print("This year students info:")
    for name, major in students.items():
        print(f"- {name}: {major}")
    print("\n")

#info(Alice="Physics", Bob="Maths")

info(Alice="Apploes Physics", Bob="Maths",
      Charlie="Pharmaseutics", David="F;uid Mechanics")
