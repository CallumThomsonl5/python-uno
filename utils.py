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

generate_card_stack_arr()
