#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    my_list = dir(hidden_4)
    for x in my_list:
        if x[1] != '_':
            print(x)
