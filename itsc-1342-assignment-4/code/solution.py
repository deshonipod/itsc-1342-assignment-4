# DeShon Harris - Assignment 4

def check_session(idle_minutes, max_idle=30):
    if idle_minutes < max_idle:
        return "SESSION_ACTIVE"
    elif idle_minutes == max_idle:
        return "SESSION_EXPIRED"
    elif (idle_minutes - max_idle) >= 15:
        return "EXPIRED_SESSION"
    else:
        return "SESSION_EXPIRED"