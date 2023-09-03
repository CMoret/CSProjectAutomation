import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the web browser
web_browser = webdriver.Chrome()
web_browser.maximize_window()

# Navigate to YouTube
web_browser.get('https://www.youtube.com/')

# Wait for the search input field to be clickable
search_input = WebDriverWait(web_browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")))
search_input.send_keys('professor messer')

# Click search button
search_button = WebDriverWait(web_browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button")))
search_button.click()

# Click on the Professor Messer's channel link
profmesser_link = WebDriverWait(web_browser,10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/div/div[2]/a/div[1]/ytd-channel-name/div/div/yt-formatted-string")))
profmesser_link.click()
time.sleep(5)

# Click on playlist tab
playlist_link = WebDriverWait(web_browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[4]/div/div[1]")))
playlist_link.click()
time.sleep(5)

# Click on a specific video
video_link = WebDriverWait(web_browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[2]/div/ytd-grid-playlist-renderer[4]/div/h3/a")))
video_link.click()
time.sleep(300)

# Close browser when done
web_browser.quit()
