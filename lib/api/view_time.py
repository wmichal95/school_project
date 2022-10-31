from datetime import datetime


def get(user):
    return {
        'user': user,
        'time': str(datetime.now())
    }
