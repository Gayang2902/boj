N = int(input())

cnt = 0
movie = 666
while True:
    if '666' in str(movie):
        cnt += 1
    if cnt == N:
        print(movie)
        break
    movie +=1 
