from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def get_source():
	browser = webdriver.Firefox() # Get local session of firefox
	browser.get("http://bacalaureat.edu.ro/2011/rapoarte/rezultate/alfabetic/page_2.html") # Load pag
	source = browser.page_source
	return source

