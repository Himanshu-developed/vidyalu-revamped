from core.models import User
import logging
logger = logging.getLogger(__name__)
def get_user_from_phone(mobile:str, dial_code:int)-> User:
    try:
        logger.info("fetching user from phone")
        user=User.objects.get(phone=mobile, dial_code=dial_code)
        logger.info("User Fetched Successfully", user)
        return user
    except Exception as e:
        print("there", e)
        logger.error("Error Occured while fetching user", e)
        return None