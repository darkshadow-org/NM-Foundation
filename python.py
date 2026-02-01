import sys

def check_license():
    # Yeh aapka unique key hai jo aap client ko denge
    VALID_KEY = "DARK-SHADOW-2026-PRO" 
    
    user_key = input("Please enter your License Key to access the tool: ")
    
    if user_key == VALID_KEY:
        print("[+] Access Granted. Initializing Forensics Pro...")
    else:
        print("[-] Invalid License Key. Contact @darkshadow_org to purchase.")
        sys.exit()

# Tool ka main code yahan shuru hoga
check_license()
print("Running Advanced Analysis...")
