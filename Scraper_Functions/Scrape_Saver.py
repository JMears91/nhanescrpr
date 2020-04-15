import selenium
import urllib
from urllib import request
import config
import os


def Yearselector():                                          # TODO update year selector to incorporate multiple years
    """ This function allows you to currently specify up to one
       year to scrape data from. This will be updated to allow
       selection of multiple years.

    """
    AddYear = True                                           # While active scrape will query the user for a year input.
    YearInput = ''

    while AddYear:
        print('select one of the following years:\n ', config.YearList[0:])
        YearInput = input()

        if YearInput in config.YearList:
            config.UrlYear.append(YearInput)
            AddYear = False
        elif len(YearInput) > 4:
            print('Incorrect entry try again')
        else:
            print('Year unavailable try again')


def Componentselector():
    """This function allows you to specify
       up to 5 categories for scraping from.

    """

    AddComponent = True
    ComponentInput = []
    ComponentSelection = ['1', '2', '3',
                          '4', '5'
                         ]

    while AddComponent:
        print('Select numbers for the following categories:\n',
              '1.', config.ComponentList[0], '\n',
              '2.', config.ComponentList[1], '\n',
              '3.', config.ComponentList[2], '\n',
              '4.', config.ComponentList[3], '\n',
              '5.', config.ComponentList[4], '\n',
              )
        ComponentInput = input('select category from 1-5:')

        if ComponentInput in ComponentSelection:
            config.UrlComponent.append(config.ComponentList[int(ComponentInput) - 1])
            AddAnother = input('Add another Category? y/n')
            if AddAnother is 'y':
                pass
            elif AddAnother is 'n':
                AddComponent = False
            else:
                print('an error occurred')
                pass
        else:
            print('Incorrect selection try again')
            pass


def Filescraper():
    """Filescraper will extract all NHANES .XPT files
       from the specified target url.
       It achieves this by iterating over the javascript table
       and extracting the file href from each individual row.
       This continues until no further files are found.

    """

    config.driver.get(Url)
    FileCount = 0
    while True:
        try:
            FileCount += 1
            rowID = str(FileCount)
            result = config.driver.find_element_by_xpath(r"//*[@id='GridView1']/tbody/tr[" +
                                                         rowID + "]/td[3]/a"
                                                         )

            config.data.append(result.get_attribute("href"))

        except selenium.common.exceptions.NoSuchElementException:
            print('End of table reached: ' + str(FileCount - 1) + ' files downloaded')
            break


def Dir_checker(file):
    """ Takes the list of scraped file names
        and queries the target directory to
        determine if a folder exists for the
        specified year.

    """
    if ( r"C:\Users\johnm\Documents\NHANES\TEMP") + file[32:42]).exists():
        pass

    else:
        os.mkdir(r"C:\Users\johnm\Documents\NHANES\TEMP" + file[32:42],)


def Filesaver(SaveDir):
    """ Takes the list of scraped .XPT files
        and downloads the files to the specified
        save directory.

    """

    for file in config.data:
        Dir_checker(file)
        urllib.request.urlretrieve(file, filename=(SaveDir + file[32:]))
        print(file[43:] + " Successfully saved")


def ScrapeSaveMain():
    """  Whilst the list containing years selected for
         data-scraping contains at least one value.
         All files within requested components will be
         scraped and saced to the specified directory.

    """
    while len(config.UrlYear) > 0:
        for Component in config.UrlComponent:
            SaveComponent = str(Component)                            # TODO is save component required? can't see how
            print(Filescraper())
            Filesaver(r"C:\Users\johnm\Documents\NHANES\TEMP")
        config.UrlYear.pop(0)