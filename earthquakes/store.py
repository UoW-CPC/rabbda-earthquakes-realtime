import os


class Store:

    @classmethod
    def toFile(cls, eq_list):
        cls.createFolder()
        cls.createFile()
        count = 0
        with open('../data/earthquakes.csv', 'a') as writer:
            for eq in eq_list:
                count = count + 1
                eq_str = ",".join(eq)
                writer.write("%s\r\n" % (eq_str))
            print "Data stored to file, records: ",count

    @classmethod
    def createFile(cls):
        with open('../data/earthquakes.csv', 'w') as writer:
            writer.write("")

    @classmethod
    def createFolder(cls):
        path = "../data/"
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed, already exist" % path)
        else:
            print ("Successfully created the directory %s " % path)
