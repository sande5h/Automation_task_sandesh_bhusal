from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os 
import random

def main():
    
    SITE = "https://authorized-partner.vercel.app/"
    TEMP_MAIL_SITE = "https://temp-mail.io/en" 
    random_number = str(9000000000 + random.randint(0, 999999999))
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    
    
    driver.get(SITE)
    
    # get Started
    get_started_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get Started')]")))
    get_started_btn.click()
    print("Clicked 'Get Started'")
    
    
    # checkbox for register
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='checkbox']")))
    checkbox.click()
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]")))
    continue_btn.click()
    print("Clicked Continue")
    
    
    
    # temp mail
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(TEMP_MAIL_SITE)
    temp_email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    
    # Loading wait 
    for i in range(10):
        temp_email = temp_email_input.get_attribute("value")
        if temp_email and "Loading" in temp_email.lower() :
            break
        time.sleep(1)

    print("Temporary email:", temp_email)
    
    #first form 
    driver.switch_to.window(driver.window_handles[0])
    
    first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    last_name_input = driver.find_element(By.NAME, "lastName")
    email_input = driver.find_element(By.NAME, "email") 
    phone_number_input = driver.find_element(By.NAME, "phoneNumber")
    password_input = driver.find_element(By.NAME, "password")
    confirm_password_input = driver.find_element(By.NAME, "confirmPassword")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    email_input.send_keys(temp_email)
    phone_number_input.send_keys(random_number)
    password_input.send_keys("Sandesh@123")
    confirm_password_input.send_keys("Sandesh@123")

    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
    next_btn.click()
    
    print("Filled First Form")
    
    
    # get otp 
    driver.switch_to.window(driver.window_handles[1])
    otp_code = None
    for _ in range(60):
        
        inbox_items = driver.find_elements(By.CSS_SELECTOR, "li.message")
        for item in inbox_items:
            subject = item.find_element(By.CSS_SELECTOR, "span.new-message.message__subject")
            otp_preview = item.find_element(By.CSS_SELECTOR, "span.line-clamp-2")
            # print(subject.text)
                
            if "Signup Confirm OTP" in subject.text:
                # print(otp_preview.text[-6:])
                otp_code = otp_preview.text[-6:]
                break
    
        if otp_code:
            # print(otp_code)
            break
        time.sleep(2) 
        # driver.refresh()
    
    
    # enter otp
    if otp_code:
        print("OTP received:", otp_code)
    else:
        print("OTP not found yet")
    driver.switch_to.window(driver.window_handles[0])
    otp_input = driver.find_element(By.XPATH, "//input[@data-input-otp='true']")
    otp_input.send_keys(otp_code)
    verify_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Verify Code')]")))
    verify_btn.click()
        
        
    # second form 
    # agency_name,role_in_agency,agency_email,agency_website,agency_address
    
    agency_name_input = wait.until(EC.presence_of_element_located((By.NAME, "agency_name")))
    role_in_agency_input = driver.find_element(By.NAME, "role_in_agency")
    agency_email_input = driver.find_element(By.NAME, "agency_email") 
    agency_website_input = driver.find_element(By.NAME, "agency_website")
    agency_address_input = driver.find_element(By.NAME, "agency_address")
    
    agency_name_input.send_keys("John2")
    role_in_agency_input.send_keys("Doe2")
    agency_email_input.send_keys(temp_email)
    agency_website_input.send_keys("www.google.com")
    agency_address_input.send_keys("chysal-09")
    
    region_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Select Your Region')]")))
    region_dropdown.click()
    region_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='dialog']//span[contains(text(), 'Nepal')]") ))
    region_option.click()
    print("Region selected")
    
    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
    next_btn.click()

    print("Filled Second form")
    
    
    # third form 
    
    # Click the experience dropdown button
    experience_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and contains(., 'Select Your Experience Level')]")))
    experience_dropdown.click()

    experience_option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='option' and contains(., '3 years')]")))

    driver.execute_script("arguments[0].scrollIntoView(true);", experience_option)
    ActionChains(driver).move_to_element(experience_option).click().perform()
    print("Selected experience")


    students_input = driver.find_element(By.NAME, "number_of_students_recruited_annually")
    focus_input = driver.find_element(By.NAME, "focus_area")
    success_input = driver.find_element(By.NAME, "success_metrics")
    
    students_input.send_keys("50")
    focus_input.send_keys("Undergraduate admissions to Canada")
    success_input.send_keys("90")
    
    services_to_select = ["Career Counseling", "Visa Processing"]
    for service in services_to_select:
        service_btn = driver.find_element(By.XPATH, f"//label[contains(text(), '{service}')]/preceding-sibling::button")
        service_btn.click()
        print(f"Selected service: {service}")
        
        
    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]")))
    next_btn.click()
    print("Third form filled")
    
    
    # fourth form
    business_input = wait.until(EC.presence_of_element_located((By.NAME, "business_registration_number")))
    business_input.send_keys("1234567890")
    
    countries_dropdown = driver.find_element(By.XPATH, "//button[@role='combobox' and contains(., 'Select Your Preferred Countries')]")
    countries_dropdown.click()

    country_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Canada')]")))
    country_option.click()
    
    institutions_to_select = ["Universities", "Colleges"]
    for inst in institutions_to_select:
        inst_btn = driver.find_element(By.XPATH, f"//label[contains(text(), '{inst}')]/preceding-sibling::button")
        inst_btn.click()
        print(f"Selected institution type: {inst}")
        
    cert_input = driver.find_element(By.NAME, "certification_details")
    cert_input.send_keys("ICEF Certified Education Agent")
        

    # file upload  companyRegistration.pdf , educationCertificate.pdf
    current_dir = os.getcwd()  
    driver.find_elements(By.XPATH, "//input[@type='file']")[0].send_keys(os.path.join(current_dir, "companyRegistration.pdf"))
    driver.find_elements(By.XPATH, "//input[@type='file']")[1].send_keys(os.path.join(current_dir, "educationCertificate.pdf"))

    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]")
    submit_btn.click()
    print("Form submitted")

    
    success_notification = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Verification and Preferences Added successfully! Registration completed!')]")
        )
    )
    print("Registration completed successfully! closing browser in 30 seconds")
    time.sleep(30)
    
    driver.quit()
    

if __name__ == "__main__" : 
    
    try:
        main()
    except Exception as error :
        print("Restarting")
        print("Error " , error)
        main()
        pass
    