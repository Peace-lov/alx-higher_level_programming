#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    #print sorted name(n) from directory
    for n in sorted(dir(hidden_4)):
        #print only name(n) that do not start with _
        if n[:2] != '_':
            print("{}".format(n))

