from flask import Blueprint, render_template
from selenium import webdriver
import time

china = Blueprint('china', __name__)


@china.route("/index")
def demo_index():
    return render_template("home/index.html")


@china.route("/baidu")
def demo_weibo():
    driver = webdriver.Chrome("tool/chromedriver")
    driver.maximize_window()
    driver.get("https://www.baidu.com/")
    driver.find_element_by_name("wd").send_keys("冰雪")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.quit()
    return "success"
