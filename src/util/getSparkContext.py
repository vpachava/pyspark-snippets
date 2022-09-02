#!/usr/bin/python

from pyspark import SparkContext
from pyspark import SparkConf


conf = SparkConf().setAppName("mytest").setMaster("local[*]")
sc = SparkContext(conf=conf)

print(type(sc),"\n")
print(dir(sc))
print(sc.version,"\n")
