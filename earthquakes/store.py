import os


class Store:

    @classmethod
    def toFile(cls, eq_list):
        cls.createFolder()
        cls.createFile()
        with open('../data/earhquakes.csv', 'a') as writer:
            for eq in eq_list:
                eq_str = ",".join(eq)
                writer.write("%s\r\n" % (eq_str))
            print ("Data successfully stored to file")

    @classmethod
    def createFile(cls):
        with open('../data/earhquakes.csv', 'w') as writer:
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
