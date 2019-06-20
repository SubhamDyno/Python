class Random:
    def defineA():
        Path = "D:\Project-User Defined\Static\DataSet-1.txt"
        Data = open(Path, mode='r')
        DataRead = Data.read();
        #DataRead = DataRead.split('/')
        print(DataRead.splitlines())
        


Obj = Random.defineA();
