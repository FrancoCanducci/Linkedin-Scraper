import requests
from bs4 import BeautifulSoup

# Replace this with the URL of the LinkedIn company profile you want to scrape
url = 'https://www.linkedin.com/company/qsaude/about/'

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element containing the "Visão Geral" information
visao_geral = soup.find('div', {'class': 'org-top-card__primary-content'})

# Extract the website and size of the company from the "Visão Geral" information
website = visao_geral.find('a', {'class': 'org-top-card-summary__website-link'})['href']
size = visao_geral.find('p', {'class': 'org-about-company-module__company-size-definition-text'}).text

# Print the results
print('Website:', website)
print('Size:', size)