from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("saini1998")
password_box = browser.find_element_by_id("password")
password_box.send_keys("sainiaaryaman1998")
password_box.submit()
assert "saini1998" in browser.page_source
profile_link = browser.find_elements_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "saini1998" in link_label

# read about waits and page objects


browser.quit()
