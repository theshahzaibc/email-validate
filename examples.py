from email_validate import email_validator

def main():
    emailAddress = "youremail@domain.com"
    evalid = email_validator()
    is_valid = evalid.verify_email(emailAddress)
    print(is_valid)
if __name__ == '__main__':
    main()
