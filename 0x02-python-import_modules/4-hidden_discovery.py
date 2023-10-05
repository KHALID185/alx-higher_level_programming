#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for n_f in dir(hidden_4):
        if n_f[:2] != "__":
            print(n_f)
