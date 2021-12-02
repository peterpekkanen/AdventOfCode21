def part1 ():
    depth = 0
    horizontal = 0

    with open('input.txt') as f:
        for line in f:

            string, value = line.split(' ') #Splits string
            value = int(value)

            if string == 'forward':
                horizontal = horizontal + value
            elif string == 'up':
                depth = depth - value
            elif string == 'down':
                depth = depth + value
            else:
                print("ERROR")

        f.close()
        
    answer = depth * horizontal
    print("Final depth: " + str(answer))
    
def part2 ():

    depth = 0
    horizontal = 0
    aim = 0

    with open('input.txt') as f:
        for line in f:

            string, value = line.split(' ') #Splits string
            value = int(value)

            if string == 'down':
                aim += value
            elif string == 'up':
                aim -= value
            elif string == 'forward':
                horizontal += value
                depth += (aim * value)
            else:
                print("ERROR")

        f.close()
        
    answer = depth * horizontal
    print("Final depth: " + str(answer))
    
if __name__ == '__main__':
    part1()
    part2()
