import sys

class processor():
    class food():
        def __init__(self, w, l, a):
            self.lysine = float(l)
            self.argenine = float(a)
            self.weight = float(w)


    def doStuff(self):
        myFood=dict()
        data = open("data.txt", "r")
        lines = data.readlines()
        print("Available Food:")
        for line in lines:
            temp = line.split(",")
            print(temp[0])
            myFood[temp[0]] = processor.food(temp[1], temp[2], temp[3])

        lys = 0
        arg = 0

        try:
           while True: 
                print("\nEnter valid food, or anything else to finish:")
                temp = myFood[input()]
                print("Enter weight in grams (1 serving is: " + str(temp.weight) + "):")
                temp2 = float(input())
                lys += temp.lysine * (temp2/temp.weight)
                arg += temp.argenine * (temp2/temp.weight)
        except KeyError:
            print("Ratio of Lysine to Argenine: " + str(lys/arg))
            if lys/arg > 1:
                print("Ratio > 1 is OK for health")
            else:
                print("Ration < 1 is not good")

if __name__ == "__main__":
    worker = processor()
    worker.doStuff()
