# WebAI

This Streamlit application offers a straightforward interface for web scraping. Users can enter a website URL, and the provided code utilizes BeautifulSoup and Pandas to extract and display various forms of content such as text, links, and images from the specified website.

## Getting Started
- To begin, ensure you have the necessary packages installed:
  - `streamlit`
  - `pandas`
  - `requests`
  - `beautifulsoup4`
  - `pdfkit`

- Input the desired website URL into the designated text field to initiate the scraping process.

## Purpose
The primary objective of this application is to illustrate the process of web scraping using Python libraries like BeautifulSoup for parsing web content and Pandas for organizing extracted data.

## Functionality
### Input
Users are prompted to input the URL of the website they wish to scrape. The initial URL is set as 'https://bbc.com' for demonstration purposes.

### Scraping Logic
Upon entering the URL and clicking the "Scrape Data" button, the application sends an HTTP request to the specified URL and proceeds to parse its content using BeautifulSoup. The scraping logic involves extracting paragraphs, anchors (links), and images from the website.

### Displaying Data
The scraped data, including text, links, and images, are presented to the user in a tabular format, courtesy of Pandas.

### PDF Generation
Following the data extraction, users have the option to download the scraped data as a PDF by clicking the "Download as PDF" button.

## Implementation
The application is implemented using Streamlit, which provides a simple and intuitive method for creating web applications with Python.

## Usage
1. Clone the provided code.
2. Install the necessary dependencies.
3. Run the application with Streamlit and input a desired website URL for scraping.
4. After scraping, the data can be downloaded as a PDF for further use.
