from App import config


def isLoginValid(login, msg):
    status = config.ok
    for simbol in config.logValid: 
        if not simbol in login or ' ' in login:
            status = config.err
            msg.append(config.invalidLoginFormat)
            break
    if config.minLoginLen > len(login) or len(login) > config.maxLoginLen:
        status = config.err
        msg.append(config.invalidLoginLen)
    return status, msg


def isPassValid(password, msg):
    status = config.ok
    if config.minPassLen > len(password) or len(password) > config.maxPassLen:
        status = config.err
        msg.append(config.invalidPassLen)
    if ' ' in password:
        status = config.err
        msg.append(config.invalidPassSpace)
    return status, msg
  
    
def isNameValid(name, msg):
    status = config.ok
    if config.minNameLen > len(name) or len(name) > config.maxNameLen:
        status = config.err
        msg.append(config.invalidNameLen)
    return status, msg


def isFormValid(whatForm, email, password, name=''):
    msg=[]
    statuslog, msg= isLoginValid(email, msg)
    statusPass, msg = isPassValid(password, msg)
    if whatForm == config.reg:
        statusName, msg = isNameValid(name, msg)
        status = (config.ok if statuslog == statusPass == statusName == config.ok else  config.err)
    else:
        status = (config.ok if statuslog == statusPass == config.ok else  config.err)
    return status, msg
