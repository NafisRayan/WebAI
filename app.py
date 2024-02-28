import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Streamlit app code
st.title('Web Scraping with Pandas and Streamlit')

# Input for the website URL
url = st.text_input('Enter the website URL', 'https://news.ycombinator.com/')

# Function to scrape data
def scrape_data(url):
    # Send HTTP request and parse content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scraping logic - use BeautifulSoup to find and extract all text content
    # This example scrapes all text within paragraph tags
    paragraphs = soup.find_all('p')
    texts = [paragraph.text for paragraph in paragraphs]

    # Create a DataFrame using pandas
    data = {'Text': texts}
    df = pd.DataFrame(data)

    # return the processed data
    return df

    # return the processed data
    return df

# Button to trigger scraping
if st.button('Scrape Data'):
    if url:
        scraped_data = scrape_data(url)
        st.write(scraped_data)
    else:
        st.write('Please enter a valid website URL')
