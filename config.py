from selenium import webdriver


Rowtracker = ""

FileCount = 0

YearList = ['1999', '2000', '2001', '2002',
            '2003', '2004', '2005', '2006',
            '2007', '2008', '2009', '2010',
            '2011', '2012', '2013', '2014',
            '2015', '2016', '2017', '2018'
            ]

ComponentList = ['Demographics', 'Dietary', 'Examination',  # A list of available Datasets for NHANES Data
                 'Laboratory', 'Questionnaire']

UrlYear = []  # Currently active year for file scrape and save

UrlComponent = []  # Currently active component for file scrape and save

SaveComponent = ''

Url = str((r"https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=" +
                       Component + "&CycleBeginYear=" + str(config.UrlYear[0])))

driver = webdriver.Chrome()

data = []
