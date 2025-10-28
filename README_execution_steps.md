# Automated Registration Script (Selenium)

This script automates registration on [Authorized Partner](https://authorized-partner.vercel.app/) using Selenium WebDriver and a temporary email service.

---
## **Requirements**

1. **Python 3.10+**
2. Internet Services Working
---
## **Setup**
 
1. **Download Script Files**  
    Make sure the following files are in the same directory as the script:
    - `signup_automation_script.py`
    - `companyRegistration.pdf`
    - `educationCertificate.pdf`
2. Open terminal in the script folder 
3. Create and activate Environment ( `Example for windows`) 
	- `python -m venv .venv` 
	- `source .\.venv\Scripts\activate `
4. Install Requirements
	- `pip install selenium`
---
## **Run**
- `python .\signup_automation_script.py`    

---
## **Known bugs**
- The Random generator can sometime generate same number which will fail the execution. The chance of this occurring exponentially low. So starting the script will negate this issue.  

---
## **Error Handling**

If an error occurs, the script will attempt to restart automatically once.

---
## **Important**

- Make sure temp-mail.io is accessible from your network.
- Keep PDF files in the same directory as the script or update the paths accordingly.

---
