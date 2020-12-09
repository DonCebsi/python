def fun(s):
    # return True if s is a valid email, else return False
    if s.count('@') != 1:
        return False
    if s.count('.') != 1:
        return False
    username, website = s.split('@')
    # check username for validity
    tmp = username.replace('-','a')
    tmp2 = tmp.replace('_','a')
    if not tmp2.isalnum():
        return False
    # check website for validity
    if '.' not in website:
        return False
    websitename, ext = website.split('.')
    if not websitename.isalnum():
        return False
    if len(ext) > 3:
        return False
    return True
