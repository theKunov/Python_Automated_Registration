# Create registration in all languages on all brands.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
import string

# Add emails below: 
emails = [
    "bug_1@dfnadhe.com",
    "bug_2@dfnadhe.com",
    "bug_3@dfnadhe.com",
    "bug_4@dfnadhe.com",
    "bug_5@dfnadhe.com",
    "bug_6@dfnadhe.com",
    "bug_7@dfnadhe.com",
    "bug_8@dfnadhe.com",
    "bug_9@dfnadhe.com"
]

# user name is random generated. You can type password only. 
password = "sggsQQs7825"

web=webdriver.Chrome(ChromeDriverManager().install())

# -----------------------------------------------------------
lang1 = ['en', 'fr', 'it', 'ru', 'es', 'fi', 'nb', 'pt', 'sv']        # White Lion 
lang2 = ['en', 'fr', 'it', 'ru', 'es', 'fi', 'nb', 'pt', 'sv', 'da']  # Dingo 
lang3 = ['en', 'fr', 'de', 'it', 'ru', 'es', 'fi', 'nb', 'sv' ]       # Enzo  
lang4 = ['en', 'fr', 'de', 'it', 'ru', 'es', 'fi', 'nb', 'sv' ]       # Bronze 
lang5 = ['en', 'fr', 'de', 'it', 'ru', 'es', 'fi', 'nb', 'sv' ]       # Golden Axe 
lang6 = ['en', 'fr', 'de', 'it', 'ru', 'es', 'fi', 'nb', 'pt', 'sv' ] # Lionel Bets 
lang7 = ['en', 'de', 'fr', 'it', 'es', 'fi', 'nb', 'sv', 'ru', 'pt' ] # GALLO 
lang8 = ['en', 'fr', 'de', 'it', 'ru', 'es', 'fi', 'nb', 'sv' ]       # TS CASINO 
lang9 = ['en', 'fr', 'de', 'it', 'ru', 'es', 'fi', 'nb', 'sv' ]       # All Cashback 



# -----------------------------------------------------------
def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return(result_str)


#  White Lion ----------------------------------------

i = 0

while i < len(lang1):

    name = get_random_string(8)
    lang = lang1[i]
    Eadress = emails[i]
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)

    # ---------------- Chivalry -----------------------
    
    web.get("https://www.chivalrycasino.com/registration")

    time.sleep(5)
    # fill form                            
    username = web.find_element_by_xpath('//*[@id="loginName"]')
    username.send_keys(name)
    
    mail = web.find_element_by_xpath('//*[@id="email"]')
    mail.send_keys(Eadress)
    
    securityfield = web.find_element_by_xpath('//*[@id="password"]')
    securityfield.send_keys(password)
    
    securityfieldConf = web.find_element_by_xpath('//*[@id="password_repeat"]')
    securityfieldConf.send_keys(password)
    
    TnC= web.find_element_by_xpath('//*[@id="over18"]/label/input')
    TnC.click()
    
    reg1finish= web.find_element_by_xpath('//*[@id="ButtonForm"]/button')
    reg1finish.click()
    
    #---------------- REG step 2 ------------
    time.sleep(5)
    def get_random_string(length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return(result_str)
    
    name = get_random_string(8)
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(1000,99999)
    
    
    # -------------Name-------------
    time.sleep(3)
    Fn = web.find_element_by_xpath('//*[@id="firstName"]')
    Fn.send_keys(fname)
    
    Ln = web.find_element_by_xpath('//*[@id="lastName"]')
    Ln.send_keys(Lname)
    
    # -------------Birthdate-------------
    
    birth = web.find_element_by_xpath('//*[@id="birthDate"]')
    birth.send_keys("02022000")
    
    
    # -------------Rest-------------
    gender = "M"
    web.find_element_by_xpath("//option[@value='" + gender + "']").click()
    
    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    
    town = web.find_element_by_xpath('//*[@id="City"]')
    town.send_keys(city)
    
    st = web.find_element_by_xpath('//*[@id="address"]')
    st.send_keys(adress)
    
    ziP = web.find_element_by_xpath('//*[@id="zipCode"]')
    ziP.send_keys(code)
    
    tel = web.find_element_by_xpath('//*[@id="PhoneNumber"]')
    tel.send_keys(mob)
    
    reg2finish= web.find_element_by_xpath('//*[@id="ButtonForm"]/button')
    reg2finish.click()


    # -------------------------
    i += 1 
    time.sleep(10)

#  Dingo ----------------------------------------

i = 0

while i < len(lang2):

    name = get_random_string(8)
    lang = lang2[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)
    # ----------------------DINGO CASINO ------------------------------------

    web.get("https://dingo-casino.com")

    time.sleep(5)

    openRegWin = web.find_element_by_xpath('//*[@id="login"]/ul/li[1]/a').click()

    time.sleep(5)
    # fill form
    username = web.find_element_by_xpath('//*[@id="registerLoginInput"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="registerPasswordInput"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="registerconfirmpswInput"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="registerover18Input"]')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[1]/fieldset[7]/a')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)
    Fn = web.find_element_by_xpath('//*[@id="registerfnameInput"]')
    Fn.send_keys(fname)

    Ln = web.find_element_by_xpath('//*[@id="registerlnameInput"]')
    Ln.send_keys(Lname)

    # -------------Birthdate-------------
    web.find_element_by_xpath("//*[@id='registerBirthDayInput']/option[text()='05']").click()
    web.find_element_by_xpath("//*[@id='registerBirthMonthInput']/option[text()='01']").click()
    web.find_element_by_xpath("//*[@id='registerBirthYearInput']/option[text()='2000']").click()

    # -------------Rest-------------
    Gender= web.find_element_by_xpath('//*[@id="registermaleInput"]')
    Gender.click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    # web.find_element_by_xpath("//*[@id='registerLangInput']/option[text()='2000']").click()

    town = web.find_element_by_xpath('//*[@id="registercityInput"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="registeraddressInput"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="registerzipcodeInput"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="registermobileInput"]')
    tel.send_keys(mob)

    reg2finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[2]/fieldset[11]/a')
    reg2finish.click()


    # -------------------------
    i += 1 
    time.sleep(10)

#  Enzo ----------------------------------------

i = 0

while i < len(lang3):

    name = get_random_string(8)
    lang = lang3[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)
    # ------------------- ENZO CASINO --------------------
    
    web.get("https://www.enzocasino.com")
    time.sleep(5)

    openRegWin = web.find_element_by_xpath('//*[@id="login"]/ul/li[1]/a').click()

    time.sleep(5)
    # fill form
    username = web.find_element_by_xpath('//*[@id="registerLoginInput"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="registerPasswordInput"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="registerconfirmpswInput"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="registerover18Input"]')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[1]/fieldset[7]/a')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)
    Fn = web.find_element_by_xpath('//*[@id="registerfnameInput"]')
    Fn.send_keys(fname)

    Ln = web.find_element_by_xpath('//*[@id="registerlnameInput"]')
    Ln.send_keys(Lname)

    # -------------Birthdate-------------
    web.find_element_by_xpath("//*[@id='registerBirthDayInput']/option[text()='05']").click()
    web.find_element_by_xpath("//*[@id='registerBirthMonthInput']/option[text()='01']").click()
    web.find_element_by_xpath("//*[@id='registerBirthYearInput']/option[text()='2000']").click()

    # -------------Rest-------------
    Gender= web.find_element_by_xpath('//*[@id="registermaleInput"]')
    Gender.click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    # web.find_element_by_xpath("//*[@id='registerLangInput']/option[text()='2000']").click()

    town = web.find_element_by_xpath('//*[@id="registercityInput"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="registeraddressInput"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="registerzipcodeInput"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="registermobileInput"]')
    tel.send_keys(mob)

    reg2finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[2]/fieldset[11]/a')
    reg2finish.click()


    # -------------------------
    i += 1 
    time.sleep(10)

#  Brozne----------------------------------------

i = 0

while i < len(lang4):

    name = get_random_string(8)
    lang = lang4[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)

    # -------------------------- BRONZE CASINO ----------------------------------

    web.get("https://www.bronzecasino.com")

    time.sleep(5)

    openRegWin = web.find_element_by_xpath('//*[@id="login"]/ul/li[1]/a').click()

    time.sleep(5)
    # fill form
    username = web.find_element_by_xpath('//*[@id="registerLoginInput"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="registerPasswordInput"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="registerconfirmpswInput"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="registerover18Input"]')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[1]/fieldset[7]/a')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)
    Fn = web.find_element_by_xpath('//*[@id="registerfnameInput"]')
    Fn.send_keys(fname)

    Ln = web.find_element_by_xpath('//*[@id="registerlnameInput"]')
    Ln.send_keys(Lname)

    # -------------Birthdate-------------
    web.find_element_by_xpath("//*[@id='registerBirthDayInput']/option[text()='05']").click()
    web.find_element_by_xpath("//*[@id='registerBirthMonthInput']/option[text()='01']").click()
    web.find_element_by_xpath("//*[@id='registerBirthYearInput']/option[text()='2000']").click()

    # -------------Rest-------------
    Gender= web.find_element_by_xpath('//*[@id="registermaleInput"]')
    Gender.click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    # web.find_element_by_xpath("//*[@id='registerLangInput']/option[text()='2000']").click()

    town = web.find_element_by_xpath('//*[@id="registercityInput"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="registeraddressInput"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="registerzipcodeInput"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="registermobileInput"]')
    tel.send_keys(mob)

    reg2finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[2]/fieldset[11]/a')
    reg2finish.click()

    # -------------------------
    i += 1 
    time.sleep(10)

#  Golden Axe ----------------------------------------

i = 0

while i < len(lang5):

    name = get_random_string(8)
    lang = lang5[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)
    # ------------------------- GOLDEN AXE -----------------------------------
    web.get("https://www.goldenaxecasino.com")

    time.sleep(5)
    openRegWin = web.find_element_by_xpath('//*[@id="login"]/ul/li[1]/a').click()

    time.sleep(5)
    # fill form
    username = web.find_element_by_xpath('//*[@id="registerLoginInput"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="registerPasswordInput"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="registerconfirmpswInput"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="registerover18Input"]')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[1]/fieldset[7]/a')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)
    Fn = web.find_element_by_xpath('//*[@id="registerfnameInput"]')
    Fn.send_keys(fname)     

    Ln = web.find_element_by_xpath('//*[@id="registerlnameInput"]')
    Ln.send_keys(Lname)                 

    # -------------Birthdate-------------
    web.find_element_by_xpath("//*[@id='registerBirthDayInput']/option[text()='05']").click()
    web.find_element_by_xpath("//*[@id='registerBirthMonthInput']/option[text()='01']").click()
    web.find_element_by_xpath("//*[@id='registerBirthYearInput']/option[text()='2000']").click()

    # -------------Rest-------------
    Gender= web.find_element_by_xpath('//*[@id="registermaleInput"]')
    Gender.click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    # web.find_element_by_xpath("//*[@id='registerLangInput']/option[text()='2000']").click()

    town = web.find_element_by_xpath('//*[@id="registercityInput"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="registeraddressInput"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="registerzipcodeInput"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="registermobileInput"]')
    tel.send_keys(mob)

    reg2finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[2]/fieldset[11]/a')
    reg2finish.click()


    # -------------------------
    i += 1 
    time.sleep(10)

#  Lionel ----------------------------------------

i = 0

while i < len(lang6):

    name = get_random_string(8)
    lang = lang6[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)

    
# -------------------------- LIONEL BETS ----------------------------------


    web.get("https://www.lionelbets.com/?lang=en")

    time.sleep(5)

    openRegWin = web.find_element_by_xpath('//*[@id="login"]/ul/li[1]/a').click()

    time.sleep(5)
    # fill form
    username = web.find_element_by_xpath('//*[@id="registerLoginInput"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="registerPasswordInput"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="registerconfirmpswInput"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="registerover18Input"]')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[1]/fieldset[7]/a')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)
    Fn = web.find_element_by_xpath('//*[@id="registerfnameInput"]')
    Fn.send_keys(fname)

    Ln = web.find_element_by_xpath('//*[@id="registerlnameInput"]')
    Ln.send_keys(Lname)

    # -------------Birthdate-------------
    web.find_element_by_xpath("//*[@id='registerBirthDayInput']/option[text()='05']").click()
    web.find_element_by_xpath("//*[@id='registerBirthMonthInput']/option[text()='01']").click()
    web.find_element_by_xpath("//*[@id='registerBirthYearInput']/option[text()='2000']").click()

    # -------------Rest-------------
    Gender= web.find_element_by_xpath('//*[@id="registermaleInput"]')
    Gender.click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    # web.find_element_by_xpath("//*[@id='registerLangInput']/option[text()='2000']").click()

    town = web.find_element_by_xpath('//*[@id="registercityInput"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="registeraddressInput"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="registerzipcodeInput"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="registermobileInput"]')
    tel.send_keys(mob)

    reg2finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[2]/fieldset[11]/a')
    reg2finish.click()

    # -------------------------
    i += 1 
    time.sleep(10)

#  Gallo ----------------------------------------

i = 0

while i < len(lang7):

    name = get_random_string(8)
    lang = lang7[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)

    # ------------ GALLO --------------------------

    web.get("https://www.gallocasino.com/Registration")

    time.sleep(5)
    # fill form                            
    username = web.find_element_by_xpath('//*[@id="loginName"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="email"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="password"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="password_repeat"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="step_one"]/form/div[4]/label/span')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="step_one"]/form/div[5]/div')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)
    Fn = web.find_element_by_xpath('//*[@id="firstName"]')
    Fn.send_keys(fname)

    Ln = web.find_element_by_xpath('//*[@id="lastName"]')
    Ln.send_keys(Lname)

    # -------------Birthdate-------------

    birth = web.find_element_by_xpath('//*[@id="birthDate"]')
    birth.send_keys("02022000")


    # -------------Rest-------------
    gender = "M"
    web.find_element_by_xpath("//option[@value='" + gender + "']").click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()

    town = web.find_element_by_xpath('//*[@id="City"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="address"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="zipCode"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="PhoneNumber"]')
    tel.send_keys(mob)

    reg2finish= web.find_element_by_xpath('//*[@id="step_tow"]/form/div[7]/div')
    reg2finish.click()

    # -------------------------
    i += 1 
    time.sleep(10)
    

#  TS Casino ----------------------------------------

i = 0

while i < len(lang8):

    name = get_random_string(8)
    lang = lang8[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)

    # -------------- TS CASINO---------------------------

    web.get("https://www.ts-casino.com/")
    time.sleep(5)

    openRegWin = web.find_element_by_xpath('//*[@id="headerSignupLink"]').click()

    time.sleep(5)
    # fill form
    username = web.find_element_by_xpath('//*[@id="registerLoginInput"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="registerPasswordInput"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="registerconfirmpswInput"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="registerover18Input"]')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[1]/fieldset[7]/a')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)
    Fn = web.find_element_by_xpath('//*[@id="registerfnameInput"]')
    Fn.send_keys(fname)

    Ln = web.find_element_by_xpath('//*[@id="registerlnameInput"]')
    Ln.send_keys(Lname)

    # -------------Birthdate-------------
    web.find_element_by_xpath("//*[@id='registerBirthDayInput']/option[text()='05']").click()
    web.find_element_by_xpath("//*[@id='registerBirthMonthInput']/option[text()='01']").click()
    web.find_element_by_xpath("//*[@id='registerBirthYearInput']/option[text()='2000']").click()

    # -------------Rest-------------
    Gender= web.find_element_by_xpath('//*[@id="registermaleInput"]')
    Gender.click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    # web.find_element_by_xpath("//*[@id='registerLangInput']/option[text()='2000']").click()

    town = web.find_element_by_xpath('//*[@id="registercityInput"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="registeraddressInput"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="registerzipcodeInput"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="registermobileInput"]')
    tel.send_keys(mob)

    time.sleep(2)

    reg2finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[2]/fieldset[11]/a')
    reg2finish.click()

    # -------------------------
    i += 1 
    time.sleep(10)
    

#  All Cashback ----------------------------------------

i = 0

while i < len(lang9):

    name = get_random_string(8)
    lang = lang9[i]
    Eadress = emails[i]
    # -------------------------
    # -------------------------
    fname = get_random_string(4)
    Lname = get_random_string(6)
    city = get_random_string(8) 
    adress = get_random_string(5) 
    code = random.randint(1000,3000)
    mob = random.randint(10000,99999)
    # -------------- All Cashback -----------------

    web.get("https://www.allcashbackcasino.com")
    time.sleep(5)

    openRegWin = web.find_element_by_xpath('//*[@id="headerSignupLink"]').click()

    time.sleep(5)
    # fill form
    username = web.find_element_by_xpath('//*[@id="registerLoginInput"]')
    username.send_keys(name)

    mail = web.find_element_by_xpath('//*[@id="registerEmailInput"]')
    mail.send_keys(Eadress)

    securityfield = web.find_element_by_xpath('//*[@id="registerPasswordInput"]')
    securityfield.send_keys(password)

    securityfieldConf = web.find_element_by_xpath('//*[@id="registerconfirmpswInput"]')
    securityfieldConf.send_keys(password)

    TnC= web.find_element_by_xpath('//*[@id="registerover18Input"]')
    TnC.click()

    reg1finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[1]/fieldset[7]/a')
    reg1finish.click()

    #---------------- REG step 2 ------------

    # -------------Name-------------
    time.sleep(8)

    Fn = web.find_element_by_xpath('//*[@id="registerfnameInput"]')
    Fn.send_keys(fname)

    Ln = web.find_element_by_xpath('//*[@id="registerlnameInput"]')
    Ln.send_keys(Lname)

    # -------------Birthdate-------------
    web.find_element_by_xpath("//*[@id='registerBirthDayInput']/option[text()='05']").click()
    web.find_element_by_xpath("//*[@id='registerBirthMonthInput']/option[text()='01']").click()
    web.find_element_by_xpath("//*[@id='registerBirthYearInput']/option[text()='2000']").click()

    # -------------Rest-------------
    Gender= web.find_element_by_xpath('//*[@id="registermaleInput"]')
    Gender.click()

    web.find_element_by_xpath("//option[@value='" + lang + "']").click()
    # web.find_element_by_xpath("//*[@id='registerLangInput']/option[text()='2000']").click()

    town = web.find_element_by_xpath('//*[@id="registercityInput"]')
    town.send_keys(city)

    st = web.find_element_by_xpath('//*[@id="registeraddressInput"]')
    st.send_keys(adress)

    ziP = web.find_element_by_xpath('//*[@id="registerzipcodeInput"]')
    ziP.send_keys(code)

    tel = web.find_element_by_xpath('//*[@id="registermobileInput"]')
    tel.send_keys(mob)

    time.sleep(3)

    reg2finish= web.find_element_by_xpath('//*[@id="lightboxRegisterForm"]/div[2]/fieldset[11]/a')
    reg2finish.click()


    # -------------------------
    i += 1 
    time.sleep(10)
