from rest_framework.views import APIView
from rest_framework.response import Response
from core.modules.get_user_from_phone import get_user_from_phone
from core.modules.otphelpers import generateOtp, verifyOtp
import logging
logger = logging.getLogger(__name__)
class GenerateOtp(APIView):
    def get(self, request):
        mobile= request.GET.get('mobile')
        dial_code= request.GET.get('dial_code')
        logger.info("Generating Otp for phone", mobile)
        if not mobile and dial_code:
            return Response({
                "message":"Bad Request",
                "status":False,
                "result":{}
            }, status=400)
        user= get_user_from_phone(mobile, dial_code)
        if(generateOtp(user)):
            return Response({
                "message":"otp sent successfully",
                "status":True,
                "result":{"user_id":user.id}
            }, status=200)