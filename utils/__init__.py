from termcolor import colored

def pprint(l: list):
    for i, q in enumerate(l):
        print(
            colored(i, "magenta"),
            colored("->", "yellow", attrs=["dark"]),
            colored(q, "green", attrs=["dark"])
            )