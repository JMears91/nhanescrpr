import pandas as pd
import config
import os



def make_csv():                                                     # TODO write function for csv conversion
    savs = []
    FileDir = r""
    for file in os.listdir():
        ActiveFile = pd.file.read_sas()
        ActiveFile.to_csv()
    pass


def make_sav():                                                     # TODO write function for spss conversion
    savs = []
    FileDir = r""
    for file in os.listdir():
        if file.endswith(".sav"):
            savs.append(os.path.join(FileDir, file)
            pass

    pass