import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pdfkit

# Streamlit app code
st.title('Web Scraping with Pandas and Streamlit')

# Input for the website URL
url = st.text_input('Enter the website URL', 'https://bbc.com')

# Function to scrape data
def scrape_data(url):
    # Send HTTP request and parse content
    response = requests.get(url)
    # print(response)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scraping logic - use BeautifulSoup to find and extract various types of content
    texts = [element.text for element in soup.find_all(['p', 'a', 'img'])]
    links = [element.get('href') for element in soup.find_all('a') if element.get('href')]
    images = [element.get('src') for element in soup.find_all('img') if element.get('src')]

    # Ensure all lists are of the same length by padding the shorter ones with None
    max_length = max(len(texts), len(links), len(images))
    texts += [None] * (max_length - len(texts))
    links += [None] * (max_length - len(links))
    images += [None] * (max_length - len(images))

    # Create a DataFrame using pandas for texts, links, and images
    data = {'Text': texts, 'Links': links, 'Images': images}
    df = pd.DataFrame(data)

    # return the processed data
    return df


# Function to generate a PDF from the scraped data
def generate_pdf(scraped_data):
    # Convert the DataFrame to HTML
    html = scraped_data.to_html(index=False)
    
    # Generate the PDF
    pdfkit.from_string(html, 'scraped_data.pdf')


# Button to trigger scraping
if st.button('Scrape Data'):
    if url:
        scraped_data = scrape_data(url)
        paragraph = ' '.join(scraped_data['Text'].dropna())
        st.write(scraped_data)
        st.write(paragraph)

        # Button to download the scraped data as a PDF
        if st.button('Download as PDF'):
            generate_pdf(scraped_data)
            st.success('PDF generated successfully.')
        
    else:
        st.write('Please enter a valid website URL')
