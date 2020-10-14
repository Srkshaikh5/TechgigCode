''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
#Q1.)
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    nIngr = input()
    nReq = input().split()
    nAvail = input().split()
    
    results = []
    for i in range(0,int(nIngr)):
        results.append(int(nAvail[i])/int(nReq[i]))
        
    print(int(min(results)))

main()


# Q.2)
def main(): 
    T = int(input()) 
    while(T>0): 
        T -= 1 
        N = int(input()) 
        teamGR = [int(integer) for integer in input().split()] 
        teamAS = [int(integer) for integer in input().split()]
        teamGR.sort()
        teamAS.sort()

        winCount = 0 
        for i in range(N): 
            for j in range(winCount,N): 
                if(teamGR[i]>teamAS[j]): 
                    winCount +=1 
                    break 
                else : 
                    break 
        print(winCount)
		
		
main()
