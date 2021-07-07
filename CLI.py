from controller import Controller


def main():
    while True:
        print("> cmd >>>", end="")
        cmd_input = input()
        words = cmd_input.split(" ", 1)
        controller = Controller(words[0], words[1])
        controller.execute_command()







if __name__ == '__main__':
    main()

