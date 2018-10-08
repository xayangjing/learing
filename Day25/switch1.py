def success(msg):
    print(msg)


def debug(msg):
    print(msg)


def error(msg):
    print(msg)


def warning(msg):
    print(msg)


def other(msg):
    print(msg)


def notify_result(num,msg):
    numbers = {
        0: success,
        1: debug,
        2: warning,
        3: error
    }

    method = numbers.get(num, msg)
    if method:
        method(msg)


if __name__ == "__main__":
    notify_result(0, "success")
