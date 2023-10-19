#read file once use regex to answer each q
import re

open('universitydata.txt', 'r')
#count records
#maters = count records w/ masters
#female_masters = count records w/ female masters
#1. records / masters
#1a. records / femalemasters
#2. White Male > .+ [White], [Male]

masters = re.findall('Masters')

income = open('income.txt')
