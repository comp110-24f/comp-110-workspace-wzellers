"""CQ00"""

__author__ = 730736640


def mimic(message: str) -> str:
    """repeat input back to me"""
    return message


def main() -> None:
    """print mimic output"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
