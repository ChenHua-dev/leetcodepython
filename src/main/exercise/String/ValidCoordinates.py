import sys
import re

sys.stdin = open('input.txt', 'r')


# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem
def validCoordinates(inputStr) -> str:
    patternLat = '[\+\-]?(\d(\.\d+)?|[1-8]\d(\.\d+)?|90(\.0+)?)'
    patternLon = '[\+\-]?(\d{1,2}(\.\d+)?|1[0-7]\d(\.\d+)?|180(\.0+)?)'
    pattern = '^[(]' + patternLat + ',\s*' + patternLon +'[)]$'
    # pattern = '^[(]' + patternLat + ',\s+' + patternLon +'[)]$'
    isMatched = re.match(pattern, inputStr)
    return "Valid" if isMatched else "Invalid"


def main():
    # input for inputStr
    inputStr_size = int(input())
    result = []
    for _ in range(inputStr_size):
        inputStr = input()
        result.append(validCoordinates(inputStr))
    print("\n".join([str(res) for res in result]))


if __name__ == '__main__':
    main()
