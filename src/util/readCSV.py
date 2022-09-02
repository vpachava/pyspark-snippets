import re
from pyspark import SparkContext
from pyspark import SparkConf

conf = SparkConf().setAppName("mytest").setMaster("local[*]")
sc = SparkContext(conf=conf)

# change file path to where you have saved the csv file
file_rdd= sc.textFile("/home/vengala/PycharmProjects/pyspark-snippets/data/input/netflix_titles.csv")

COMMA_DELIMITER = re.compile(''',(?=(?:[^"]*"[^"]*")*[^"]*$)''')

rows = file_rdd \
    .map(lambda line : COMMA_DELIMITER.split(line))

listofrows = rows.map(lambda row: row).collect()
print(listofrows)