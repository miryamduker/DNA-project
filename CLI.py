from controllers.controller import Controller


def main():
    while True:
        try:
            print("> cmd >>>", end="")
            cmd_input = input()
            words = cmd_input.split(" ", 1)
            if len(words) == 1:
                controller = Controller(words[0], None)
            else:
                controller = Controller(words[0], words[1])
            controller.execute_command()
        except:
            print("Command not valid")


if __name__ == '__main__':
    main()
