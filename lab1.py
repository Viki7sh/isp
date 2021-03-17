#!usr/bin/env python3
# Output of the word the number of times we input
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def printf(word, num):
    logging.info(word * num)


def main():
    logging.info("Enter your word: ")
    a = input()

    while True:
        try:
            b = int(input("Enter your number: "))
            break
        except ValueError:
            logging.info("InterruptError")
    printf(a, b)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("KeybordInputError")
