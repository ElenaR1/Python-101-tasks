import json,io

class Song:
    def __init__(self,title,artist,album,length):
        self.title=title
        self.artist=artist
        self.album=album
        self._length=length

    def __str__(self):
        s="{"+self.artist+"} - "+"{"+self.title+"} from {"+self.album+"} - {"+self._length+"}"
        return s
    def __eq__(self,other):
        if self.title==other.title and self.artist==other.artist and self.album==other.album and self._length==other._length:
            return True
        else:
            return False
    def __hash__(self):
        return hash((self.title,self.artist,self.album,self._length))
    def length(self,seconds=False,minutes=False,hours=False):
        if seconds==True:
            if self._length.count(':')==1:
                m, s = self._length.split(':')
                return int(m) * 60 + int(s)
            if self._length.count(':')==2:
                h,m, s = self._length.split(':')
                return int(h) * 3600 + int(m) * 60 + int(s)
        if minutes==True:
            if self._length.count(':')==1:
                 m, s = self._length.split(':')
                 return int(m) 
            if self._length.count(':')==2:
                h,m, s = self._length.split(':')
                return int(h) * 60 + int(m) 
        if hours==True:
            if self._length.count(':')==1:
                m, s = self._length.split(':')
                sum_seconds=int(m) * 60 + int(s)
            if sum_seconds >=3600:
                return sum_seconds//3600
            else:
                return 'less than an hour'
            if self._length.count(':')==2:
                h,m, s = self._length.split(':')
                return int(h)
        if seconds==False and minutes==False and hours==False:
            return self._length


    def to_jason(self,name,indent=4):
        my_dict={}
        my_dict["dict:"]=self.__dict__
        my_dict["type"]=self.__class__.__name__
        y=json.dumps(my_dict,indent=indent)
       # with io.open('data.txt', 'w') as f:
        name=name.replace(' ','-')
        s=name+'.json'
        #y=y+','
        print(y)
        f=open(s, "a+")
        f.write(y)


def main():
    s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
    print(s)
    print('hash',hash(s))
    print('length',s.length())
    print(s.length(seconds=True))
    print(s.length(minutes=True))
    print(s.length(hours=True))
    s2 = Song(title="Ich Will", artist="Manowar", album="The Sons of Odin", length="4:06")
    print('mins:',s2.length(minutes=True))
if __name__=='__main__':
    main()