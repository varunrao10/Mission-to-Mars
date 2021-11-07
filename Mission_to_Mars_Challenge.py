# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# Parse the resulting html with soup
html = browser.html
hemi_soup = soup(html, 'html.parser')

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

#Both the title and the image are within this div
hemisphere_item = hemi_soup.find_all('div', class_='item')

#heading iterator to get each item
heading_iterator = 0

#Loop through each title and image
for result in hemisphere_item:
    
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    
    hemispheres = {"img_url":"", "title":""}

    # Find and click the full image button
    full_image = browser.find_by_tag('h3')[heading_iterator]
    
    #Get Title and then strip for just the text
    hemisphere_title = result.find('h3').text
    hemispheres["title"] = hemisphere_title
    full_image.click()
        
    #Grab image from site
    slide_elem = browser.find_by_tag('a')[3]
    
    hemispheres["img_url"] = slide_elem["href"]
    
    browser.back()
    
    heading_iterator = heading_iterator + 1
    hemisphere_image_urls.append(hemispheres)
    
print(hemisphere_image_urls) 

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()