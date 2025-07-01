from frappe.utils.password import passlibctx

def validate_password(user, password):
    truehash = user.password
    if passlibctx.verify(password,truehash):
        valid = True
    else:
        valid = False
    return valid

def update_password(new):
    newhash = encode(new)
    return newhash

def encode(password):
    hashed = passlibctx.hash(password)
    return hashed

