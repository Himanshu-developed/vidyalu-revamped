from core.models import OtpVerification
from utils.sns_sms_service import sendSms
import math, random
import logging
logger = logging.getLogger(__name__)


def generateOtp(user):
    logger.info("generating otp for user", user)
    digits = "0123456789"
    OTP = ""
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
    logger.info("otp generated successfully")
    try:
        logger.info("saving generated otp for user", user)
        otpObj=OtpVerification.objects.filter(user=user, is_verified=False).first()
        if  otpObj:
            otpObj.is_verified=True
            otpObj.save()
        otpObj=OtpVerification.objects.create(user=user, otp=int(OTP))
        sendSms({
            "message":f"Your One Time Password for login at vidyalu is {OTP}. Kindly do not share it with anyone",
            "mobile":'+'+str(user.dial_code)+user.phone
        })
        if otpObj:
            return True
        else:
            return False
    except Exception as e:
        logger.error("error occured while generating otp for user", e)
        return False

def verifyOtp(user):
    pass