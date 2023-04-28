"""DataSpike"""
def main():
    """DataSpike"""
    data1 = int(input())
    data2 = int(input())
    data3 = int(input())
    data4 = int(input())
    data5 = int(input())
    data6 = int(input())
    data7 = int(input())
    data8 = int(input())
    if data1 > data2 and data1 > data3 and data1 > data4 and \
        data1 > data5 and data1 > data6 and data1 > data7 and data1 > data8:
        print(data1)
    if data2 > data1 and data2 > data3 and data2 > data4 and \
        data2 > data5 and data2 > data6 and data2 > data7 and data2 > data8:
        print(data2)
    if data3 > data2 and data3 > data1 and data3 > data4 and \
        data3 > data5 and data3 > data6 and data3 > data7 and data3 > data8:
        print(data3)
    if data4 > data2 and data4 > data3 and data4 > data1 and \
        data4 > data5 and data4 > data6 and data4 > data7 and data4 > data8:
        print(data4)
    if data5 > data2 and data5 > data3 and data5 > data4 and \
        data5 > data1 and data5 > data6 and data5 > data7 and data5 > data8:
        print(data5)
    if data6 > data2 and data6 > data3 and data6 > data4 and \
        data6 > data5 and data6 > data1 and data6 > data7 and data6 > data8:
        print(data6)
    if data7 > data2 and data7 > data3 and data7 > data4 and \
        data7 > data5 and data7 > data6 and data7 > data1 and data7 > data8:
        print(data7)
    if data8 > data2 and data8 > data3 and data8 > data4 and \
        data8 > data5 and data8 > data6 and data8 > data7 and data8 > data1:
        print(data8)
main()
