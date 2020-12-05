#Import modules
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen


#Accepting url of a website using Web GUI
st.title("Webscraping a Website")
raw_url = st.text_input("Enter URL Here")


#Create a drop down with the features that can be extracted
opt =['HTML','Text','H1','H2','H3','H4','H5','H6','Table1','Table2','Table3',
        'Table4','Table5','Table6','Links','Titles','Images']
option = st.sidebar.selectbox('Please select what you want to scrape', opt )











#Dropdown with list of features
if st.sidebar.checkbox("Show", False):
    page = urlopen(raw_url)  #Extract HTML of the page
    soup = BeautifulSoup(page) #Beautify the text
    words = ' '.join(map(lambda p:p.text,soup.find_all('p')))

#Prettify the text
    if (option == 'HTML'): st.write(soup.prettify())

#Extract the links
    if (option == 'Links'): 
    	for link in soup.find_all('a'):
	    	if 'href' in link.attrs: 
	    		st.write(link.attrs['href'])







    #Extract the HTML features of webpage
    if (option == 'Text'): st.write(words)
    if (option == 'H1'): st.write(soup.h1)
    if (option == 'H2'): st.write(soup.h2)
    if (option == 'H3'): st.write(soup.h3)
    if (option == 'H4'): st.write(soup.h4)
    if (option == 'H5'): st.write(soup.h5)
    if (option == 'H6'): st.write(soup.h6)
    if (option == 'Table1'): st.table(pd.read_html(raw_url)[0])
    if (option == 'Table2'): st.table(pd.read_html(raw_url)[1])
    if (option == 'Table3'): st.table(pd.read_html(raw_url)[2])
    if (option == 'Table4'): st.table(pd.read_html(raw_url)[3])
    if (option == 'Table5'): st.table(pd.read_html(raw_url)[4])
    if (option == 'Table6'): st.table(pd.read_html(raw_url)[5])







    #Extract titles
    if (option == 'Titles'):
    	for link in soup.find_all('a'):
	    	if 'title' in link.attrs:
	    		st.write(link.attrs['title'])

    #Extract the image links
    if (option == 'Images'):
        for link in soup.find_all('img'):
            if 'src' in link.attrs:
                st.write(link.attrs['src'])










