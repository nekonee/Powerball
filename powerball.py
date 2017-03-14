import random


def powerball():

    a=[random.randrange(1,60) for i in range(0,5)]

    print "Today's numbers are: "
    for i in range(0,5):
        print "%d\t" % (a[i])


    p=random.randrange(1,36)

    print "Powerball number is %d" %(p)

    for i in range(0,5):
        if a[i] == p :
            print "Player %d has won!" %(a)

    else:
        print "No winner this time"


powerball()

