def simple(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

if __name__ == '__main__':
    a=int(input())
    print(simple(a))
