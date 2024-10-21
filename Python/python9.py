a=int(input("Enter the amount:\t"))
n_500=a//500
r_500=a%500

n_200=r_500//200
r_200=r_500%200

n_100=r_200//100
r_100=r_200%100

n_50=r_100//50
r_50=r_100%50

n_20=r_50//20
r_20=r_50%20

n_10=r_20//10
r_10=r_20%10

n_5=r_10//5
r_5=r_10%5

n_1=r_5//1
print("No.of 500 notes are {}" .format(n_500))
print("No.of 200 notes are {}" .format(n_200))
print("No.of 100 notes are {}" .format(n_100))
print("No.of 50 notes are {}" .format(n_50))
print("No.of 20 notes are {}" .format(n_20))
print("No.of 10 notes are {}" .format(n_10))
print("No.of 5 notes are {}" .format(n_5))
print("No.of 1 notes are {}" .format(n_1))