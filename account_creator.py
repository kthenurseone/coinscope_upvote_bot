import requests
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os
import random
from selenium.webdriver.chrome.service import Service
import zipfile
from random_username.generate import generate_username
import sys
import configparser
config = configparser.ConfigParser()
config.read("settings.ini")
mySettings = config['SETTINGS']


######SORGU
import requests
import hashlib
import time
def lis():
    abcaw = mySettings["LICENCE"]
    url = 'https://kthenurseone.com/licence/show.php?username=' + abcaw + "&bot=coinscope_account_creator"
    response = requests.get(url) 
    response = response.text #siteden gelen
    response = response.replace(" ","")
    sifre = str(time.time())[0:9]
    sifreleyici = hashlib.sha256()
    sifreleyici.update(sifre.encode("utf-8"))
    hashe = sifreleyici.hexdigest() #bizim şifre

    while hashe != response:
       print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")
       time.sleep(1)
       return lis()

lis()
######SORGU 

ACCOUNT_PASSWORD = mySettings["ACCOUNT_PASSWORD"]
BOT_RUN_TIME = mySettings["ACCOUNT_AMOUNT"]


for adasd in range(10):
    if(mySettings["LICENCE"] == "TEST"):
        print("This is the test licence. Please contact with t.me/kthenurseone to get full version.")
    else:
        print("K' The Nurse One CoinScope Account Creator BOT //// Telegram: t.me/kthenurseone")
    time.sleep(0.2)


def get_chromedriver():
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    proxy = mySettings["PROXY"]
    #print(proxy)
    myProxy = proxy.split(":")
    #print(myProxy)
    PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS = myProxy[0],myProxy[1],myProxy[2],myProxy[3]
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    s = Service(executable_path='chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    # if use_proxy:
    pluginfile = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    chrome_options.add_extension(pluginfile)
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument(f'user-agent={userAgent}')
    prefs2 = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs2)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=chrome_options,service=s)
    return driver




def create():
    driver = get_chromedriver()
    driver.maximize_window()
    driver.get("https://www.coinscope.co/login")
    actions = ActionChains(driver) 
    print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")
    
    
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
    response = requests.request("GET", url, headers=header)
    email = response.text.split("@")[0].replace('["','')
    domain = response.text.split("@")[1].replace('"]','')
    full_mail = str(email) + "@" + str(domain)
    # print(full_mail)
    ############################################    SELENIUM PART ############################################
    
    clickMail = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/main/div[2]/div/div[2]/div/div/div[1]/form/ul/li[2]/button")))
    clickMail.click()
    print("Email sign up button clicked.")
    time.sleep(1)
    emailInput = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.NAME, "email")))
    emailInput.send_keys(full_mail)
    emailInput.send_keys(Keys.RETURN)
    print("Email wrote:", full_mail)
    username = generate_username(1)
    userName = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.NAME, "name")))
    userName.send_keys(username)
    print("Username wrote: ",username)
    print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")
    password = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.NAME, "newPassword")))
    password.send_keys(ACCOUNT_PASSWORD)
    print("Password wrote:", ACCOUNT_PASSWORD)
    driver.save_screenshot("1.png")
    print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")
    time.sleep(3)
    signUp = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//button[@class='firebaseui-id-submit firebaseui-button mdl-button mdl-js-button mdl-button--raised mdl-button--colored']")))
    signUp.click()
    print("Sign up button clicked.")
    driver.save_screenshot("2.png")
    time.sleep(2)
    print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")

    
    ############################################    SELENIUM PART ############################################
    email_check = "https://www.1secmail.com/api/v1/?action=getMessages&login=" + str(email) + "&domain=" + str(domain)
    # print(email_check)
    print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")
    response_email = requests.request("GET", email_check, headers=header)
    while len(response_email.text) < 5:
        response_email = requests.request("GET", email_check, headers=header)
        # print("Waiting for message: " + email + "@" + domain)
        # print(email_check)
        # print(email + "@" + domain)
        # print(response_email.text)
        print("Waiting for verification mail.")
        print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")
        time.sleep(1)
    y = json.loads(response_email.text)
    print(y[0]["id"])
    get_message_url = "https://www.1secmail.com/api/v1/?action=readMessage&login=" + str(email) + "&domain=" + str(domain) + "&id=" + str(y[0]["id"])
   # print(get_message_url)
    message = requests.request("GET", get_message_url, headers=header)
    x = json.loads(message.text)
    # print(x["htmlBody"])
    for a in x["htmlBody"].split("'"):
        if a.startswith('https://coinscopeassets.firebaseapp.com'):
            a = a.replace("amp;","")
            print(a)
            driver.get(a)
            signUp = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[3]/div/button"))).click()
            WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"/html/body")))
            
            print("Email verification done.")
            print("BOT OWNER TELEGRAM : t.me/kthenurseone   CONTACT ME")

            open("accounts.txt", "a").write("\n" + full_mail + ":" + ACCOUNT_PASSWORD)
            time.sleep(12)
            driver.quit()
            if(mySettings["LICENCE"] == "TEST"):
                print("This is the test licence. Please contact with t.me/kthenurseone to get full version.")
                time.sleep(100)
                sys.exit("This is the test licence. Please contact with t.me/kthenurseone to get full version.")


    

for abc in range(int(BOT_RUN_TIME)):
    try:
        create()
    except Exception as e:
        print(e)
        pass
    