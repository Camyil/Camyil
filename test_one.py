import time


class Var:
    first_out = 0
    second_out = 0
    third_out = 0

    number_test = 3
    time_stop = 0
    time_in = 0
    stop = 0


def first_test():
    x = 0
    start_time = time.time()
    for i in range(1000000):
        x += i
    Var.first_out += time.time() - start_time
    print("time elapsed: {:.7f}s".format(time.time() - start_time))


def second_test():
    x = 0
    start_time = time.time()
    for i in range(10000000):
        x += i
    Var.second_out += time.time() - start_time
    print("time elapsed: {:.7f}s".format(time.time() - start_time))


def third_test():
    x = 0
    start_time = time.time()
    for i in range(50000000):
        x += i
    Var.third_out += time.time() - start_time
    print("time elapsed: {:.7f}s".format(time.time() - start_time))


def load():
    file = open("assets/test_out/time", "r")
    Var.time_stop = file.read()
    file.close()


def save():
    one = Var.first_out / Var.number_test
    two = Var.second_out / Var.number_test
    three = Var.third_out / Var.number_test

    file = open("assets/test_out/first_out", "w")
    file.write(str("{:.7f}s".format(one)))
    file.close()
    file = open("assets/test_out/second_out", "w")
    file.write(str("{:.7f}s".format(two)))
    file.close()
    file = open("assets/test_out/third_out", "w")
    file.write(str("{:.7f}s".format(three)))
    file.close()


def save_exit():
    file = open("assets/test_out/time", "w")
    file.write(str(0))
    file.close()


def main():
    while True:
        for i in range(Var.number_test):
            first_test()
            load()
            if Var.time_in >= float(Var.time_stop * 3):
                Var.stop = 1
                break
        if Var.stop == 1:
            break
        save()
        print()
        for i in range(Var.number_test):
            second_test()
            load()
            if Var.time_in >= float(Var.time_stop * 3):
                Var.stop = 1
                break
        if Var.stop == 1:
            break
        save()
        print()
        for i in range(Var.number_test):
            third_test()
            load()
            if Var.time_in >= float(Var.time_stop * 3):
                Var.stop = 1
                break
        if Var.stop == 1:
            break
        save()
        save_exit()
        break


main()
