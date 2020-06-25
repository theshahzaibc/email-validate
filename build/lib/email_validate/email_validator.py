import requests
import re

class email_validator:
    """Check the email format validity and if the email actually exists."""

    def __init__(self,):
        self.email = None
    def verify_email(self,email):
        self.email = email
        cf = self.check_format()
        if(cf == "validFormat"):
            vea = self.verify_email_async()
            return vea
        else:
            return cf

    def check_format(self):
        if(self.email is not None):
            if(re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", self.email) != None):
                return "validFormat"
            return "invalidFormat"
        else:
            return "emptyEmail";

    def verify_email_async(self):
        if(self.email is not None):
            base_url = "https://api.2ip.me/email.txt"
            var_email = {'email':self.email}
            r = requests.get(base_url,params=var_email)
            if(r.status_code == 200):
                if(r.text == "true"):
                    return "validEmail"
                else:
                    return "invalidEmail"
            else:
                return "error"

        else:
            return "emptyEmail"
