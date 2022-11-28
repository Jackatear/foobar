def main():
    print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))

def solution(x):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = a[::-1]
    input = x
    output = []
    
    for c in input:
        try:
            if c in b:
                pos = b.find(c)
                output.append(a[pos])
            else:
                raise
        except:
            output.append(c)
            
    return(''.join(output))
            
            
        
    
if __name__ == "__main__":
    main()