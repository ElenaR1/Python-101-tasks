def chain(iterable_one, iterable_two):
    l=[]
    for el in iterable_one:
        l.append(el)
    for el in iterable_two:
        l.append(el)

    for val in l:
        yield val



def chain2(iterable_one, iterable_two):
    l=[]
    for el in iterable_one:
        l.append(el)
    for el in iterable_two:
        l.append(el)

    class L:
         def __init__(self,lst):
            self.lst=lst
           

         def __iter__(self):
            self.index=0
            return self

         def __next__(self):
            index=self.index
            self.index+=1
            try:
                return self.lst[index]
            except IndexError:
                raise StopIteration

    obj=L(l)
    # i=iter(obj)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # for el in obj:
    #     print(el)
    return L(l)


def compress(iterable, mask):
    for ind,el in enumerate(iterable):
        if mask[ind]==True:
            yield el


def cycle(iterable):
    s=""
    i=0
    while i<4:
        for el in iterable:
            s+=str(el)
        i+=1
        yield s
    
def remove_newline(str):
    n=len(str)
    str=str[:n-1]
    return str
def cat(arguments):
    f=open("001.txt")
    i=0;
    array=f.readlines()
    while i<len(array)-1:
        array[i]=remove_newline(array[i])     
        yield array[i]
        i=i+1
    yield array[i]
    f.close()


def read_input(prompt):
    x = input()
    while int(x)<5:
        yield x
        x = input()

def book_reader():
    lines=list(cat("001.txt"))
    print(lines[0])
    for item in lines:
        if item.find("# Chapter")!=-1 or item.find("#Chapter")!=-1:
            print('Press space to see the chapter')
            ch=input()
            if ch!=' ':
                print('invalid input')
                break
        print(item)

def main():
    
    print(chain(range(0, 4), range(4, 8)))
    print(list(chain(range(0, 4), range(4, 8))))
    #chain2(range(0, 4), range(4, 8))

    print(chain2(range(0, 4), range(4, 8)))
    print(list(chain2(range(0, 4), range(4, 8))))

    print(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
    print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))

    print(cycle(range(0,10)))
    print(list(cycle(range(0,10))))
    endless = cycle(range(0,10))
    for item in endless:
        print(item)

    # print('================')
    # lines=list(book_reader())
    # print(lines[0])
    # for item in lines:
    #     if item.find("# Chapter")!=-1 or item.find("#Chapter")!=-1:
    #         print('Press space to see the chapter')
    #         ch=input()
    #         if ch!=' ':
    #             print('invalid input')
    #             break
    #     print(item)

    book_reader()

    # l=list(read_input(4))
    # for el in l:
    #     print(el)

if __name__=='__main__':
    main()



