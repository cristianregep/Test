#!/usr/bin/env python
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def extract_from_re(expr, source):
	regex = re.compile(expr)
	return regex.findall(source)
def remove_noise(list):
	newlist = []
	count=1
	for element in list:
		if count > 2 and count!=len(list):
			newlist.append(element)
		count+=1
	return newlist
def show_columns(list):
	for i in range(0,len(list)/2):	
		print "--------------ROW-----------------"
		show_list(extract_from_re("<td.*?</td>", list[i*2]))
		print "***"
		show_list(extract_from_re("<td.*?</td>", list[i*2+1]))

def process_columns(list):
	for i in range(0,len(list)/2):
                row1 = extract_from_re("<td.*?</td>", list[i*2])
                row2 = extract_from_re("<td.*?</td>", list[i*2+1])
		create_query(row1,row2)

def create_query(row1, row2):
	name = extract_from_re("</script>(.*)</td>",row1[1])[0].replace("<br />", "", 1)
	school = extract_from_re("<a.*?>(.*)</a>", row1[4])[0]
	county = extract_from_re("<a.*?>(.*)</a>", row1[5])[0]
	specializare =  extract_from_re("<td.*?>(.*)</td>", row1[8])[0]
	oral_ro = extract_from_re("<td.*?>(.*)</td>", row1[9])[0]
	scris_ro = extract_from_re("<td.*?>(.*)</td>", row1[12])[0]
	limba_materna = extract_from_re("<td.*?>(.*)</td>", row1[13])[0]
	limba_moderna = extract_from_re("<td.*?>(.*)</td>", row1[14])[0]
	nota_limba_moderna = extract_from_re("<td.*?>(.*)</td>", row1[15])[0]
	print nota_limba_moderna

def show_list(list):
	for elem in list:
		print elem

def get_source(url):
	browser = webdriver.Firefox() # Get local session of firefox
        browser.get(url)
        return browser.page_source

def process_page(url):
	source = get_source(url)
	main_table = extract_from_re("id=\"mainTable\".*</table>", source)
	rows = remove_noise(extract_from_re("<tr.*?</tr>", main_table[0]))
	return rows
