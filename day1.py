#Part 1
def main():
    i = 0 #Counter
    oldValue = 0
    with open('input.txt') as f:
        for line in f:
            if (int(line)) > oldValue:
               print("Increased")
               i = i + 1
            else:
                print("Decreased")
            oldValue = int(line)
    f.close()

    print("Total: " + str(i))

if __name__ == '__main__':
    main()
