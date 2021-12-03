
def part1():
    gammaRate = 0
    epsilRate = 0

    n = 0 #Counter
    l = 0 #Line

    i = 0 #Positive bit
    k = 0 #Negative bit

    fString = ''    #Gamma rate
    with open('input.txt') as f:
        for line in f:
            if (line[n] == '\n'):
                f.close()
                break
                
            if line[n] == '1':
                i += 1
            else:
                k += 1

            l += 1
            if l == 1000:

                if i > k:
                    fString += str('1')
                else:
                    fString += str('0')

                #Step forward
                n += 1
                #Reset variables
                l = 0
                i = 0
                k = 0
                #Move pointer back to first line
                f.seek(0, 0)
 

        #Invert string
        iString = ''    #Epsilon rate
        for bit in fString:
            if bit == '1':
                iString += '0'
            elif bit == '0':
                iString += '1'

        bfString = '0b' + fString
        biString = '0b' + iString
        #Convert binary -> integer
        gammaRate = int(bfString, 2) 
        epsilRate = int(biString, 2)
        answer = gammaRate * epsilRate

        print(answer)

if __name__ == '__main__':
    part1()
