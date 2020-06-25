# email_validate

`email_validate` can verify any email address by efficiently checking the domain name and pinging the handler to verify its existence.

## Features

- Syntax checks
- MX(Mail Exchange records) verification
- Email Handler verification
- Caching domain lookups to improve performance
 

## Compatibility
- Written in Python 3.7.
- Supports Python 3.7+.
- It should work on Linux, Mac and Windows.

## Installation
### From [pypi.org](https://pypi.org/project/email-validate/)
```
$ pip install email-validate
```
### From source code
```
$ git clone https://github.com/theshahzaibc/email_validate
$ cd email_validate
$ virtualenv env
$ source env/bin/activate
$ python setup.py develop
```

## Usage
```
>>> from email_validate import email_validator
>>> evalid = email_validator()
>>> evalid.verify_email('foo@bar.com')
invalidEmail
>>> evalid.verify_email('shahzaibsaifullah@gmail.com')
validEmail
>>> evalid.verify_email('foobar.com')
invalidFormat```
see for more examples [examples.py](https://github.com/theshahzaibc/email-validate/blob/master/examples.py)

## Contribute
- Issue Tracker: https://github.com/theshahzaibc/email-validate/issues
- Source Code: https://github.com/theshahzaibc/email-validate## Support
If you are having issues, please create an issue for it. And feel free to contribute as well 😄.
