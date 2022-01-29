import sys


def generate_card_stack_arr():
    stack = []


    # Normal
    colours = ["red", "green", "yellow", "blue"]
    for colour in colours:

        for x in range(10):
            sys.stdout.write( f"NormalCard(\"{colour}\", {x}), " )

        for x in range(1,10):
            sys.stdout.write( f"NormalCard(\"{colour}\", {x}), " )

    # Reverse
    for colour in colours:
        sys.stdout.write( f"ReverseCard(\"{colour}\"), " )
        sys.stdout.write( f"ReverseCard(\"{colour}\"), " )

    # Pick 2
    for colour in colours:
        sys.stdout.write(f"Pick2Card(\"{colour}\"), ")
        sys.stdout.write(f"Pick2Card(\"{colour}\"), ")

    # Null Cards
    for colour in colours:
        sys.stdout.write(f"NullCard(\"{colour}\"), ")
        sys.stdout.write(f"NullCard(\"{colour}\"), ")

    # Wilds
    for x in range(4):
        sys.stdout.write("WildCard(), ")
        sys.stdout.write("Wild4Card(), ")


generate_card_stack_arr()
