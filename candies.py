N=10
K=int(input())
if(K<=0):
    print("INVALID INPUT")
    print("NUMBER OF AVAILABLE CANDIES:",K)
else:
    print("NUMBER OF CANDIES SOLD:",K)
    print("NUMBER OF AVAILABLE CANDIES:",N-K)
