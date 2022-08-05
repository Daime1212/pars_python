import random

from selenium import webdriver
import time
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def selenium_hh(job_title):


    from selenium.webdriver.support.wait import WebDriverWait

    browser = webdriver.Chrome(executable_path='./chromedriver')

    browser.maximize_window()
    browser.get('https://hh.ru/?hhtmFrom=vacancy_search_list')


    search_button = browser.find_element(By.CSS_SELECTOR, 'data-page-analytics-event="searchButton.submit')


    search_input = browser.find_element(By.id, 'a11y-search-input')
    search_input.send_keys('job_title')

    search_input.click


    salary_xpath = '/html/body/div[5]/div/div[3]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div/div/div/div[6]/div/div[2]/li[3]/label/span/span[1]'
    salary = browser.find_element(By.XPATH, salary_xpath)


    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "salary_xpath"))).click()


    import re
    count_integer = re.sub(r'\D', '', salary.text)


    print(f'Max: {count_integer}')

    browser.close()
    return count_integer

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    count = random.randint(1, 1000)
    await update.message.reply_text(f'Job:{count}')


app = ApplicationBuilder().token("5478942655:AAGr7Mty9K9ggHoWHeiWBVFtCX4ZPnFGcCU").build()

handler = MessageHandler(filters.TEXT, reply)
app.add_handler(handler)

app.run_polling()

