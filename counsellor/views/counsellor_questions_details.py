
from rest_framework.views import APIView
from core.permissions import IsCounsellor
from core.helpers import api_response
from counsellor.models.counsellor_question_model import CounsellorQuestion
from counsellor.serializers.counsellor_question_serializer import CounsellorQuestionSerializer,CounsellorQuestionGetSerializer
# from teacher.serializers.teacher_question_serializer import TeacherQuestionSerializer,TeacherQuestionPostSerializer,TeacherQuestionFilePostSerializer
# from docx import Document

class CounsellorTestQuestionAPI(APIView):
    permission_classes = (IsCounsellor,)

    def post(self,request):
        user_id = request.user.id
        serializer = CounsellorQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(counsellor_id=request.user.id)
            return api_response(200, "Counsellor Questions created sucessfully", serializer.data, status=True)
        else:
            return api_response(400, "Unable to create Questions", serializer.errors, status=False)



class CounsellorTestChangeQuestionAPI(APIView):
    permission_classes = (IsCounsellor,)

    def put(self,request):
        user_id = request.user.id
        question_id = request.data.get("id", None)
        question = CounsellorQuestion.objects.get(id=question_id)
        serializer = CounsellorQuestionSerializer(question,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(counsellor_id=request.user.id)
            return api_response(200, "Questions updated successfully", serializer.data, status=True)
        return api_response(400, "Questions update failed", {}, status=False)



class CounsellorTestGetQuestionAPI(APIView):
    permission_classes = (IsCounsellor,)

    def post(self,request):
        user_id = request.user.id
        # teacher_id = Teacher.objects.get(teacher_id = user_id).id
        test_id = request.data.get("id", None)
        question = CounsellorQuestion.objects.filter(counsellor_id = user_id,test_id=test_id)
        if question:
            serialized_question = CounsellorQuestionGetSerializer(question, many = True)
            return api_response(200,"Question retrived successfully", serialized_question.data, status=True)
        else:
            return api_response(200, "No Question found", [], status=True)




class CounsellorTestDeleteQuestionAPI(APIView):
    permission_classes = (IsCounsellor,)

    def post(self,request):
        try:
            question_id = request.data.get("id", None)
            question = CounsellorQuestion.objects.get(id=question_id)
            question.delete()
            return api_response(200,"Question deleted successfully",{}, status=True)
        except CounsellorQuestion.DoesNotExist:
            return api_response(400, "Question delete failed", {}, status=False)

















# class TestQuestionAPI(APIView):
#     # permission_classes = (IsTeacher,)
#     def get(self,request):
#         queryset = Question.objects.all()
#
#         serializer = TeacherQuestionSerializer(queryset,many = True)
#         return api_response(200,"Questions retrived successfully", serializer.data, status=True)
#
#     def put(self,request):
#         pass
#
#     def delete(self,request):
#         pass
#
#
#
# class TestQuestionFileAPI(APIView):
#     def post(self,request):
#         # serializer = TeacherQuestionPostSerializer(request.data)
#         file_name = request.FILES['question_file']
#         data = Document(file_name)
#         data_list = [i.text for i in data.paragraphs]
#         question_list = []
#         options_list = []
#         ans_list = []
#
#         for i in data_list:
#             if 'Question' in i:
#                 question_list.append(i)
#             elif 'Options' in i:
#                 options_list.append(i)
#             elif 'Ans' in i:
#                 ans_list.append(i)
#
#         options_list_options = []
#         for i in options_list:
#             options_list_options.append(i.split(',')[1:])
#
#         print(question_list)
#         print(options_list_options)
#
#         question_ans_text_dict = [{'question_text':i[0],'option_one':i[1][0],'option_two':i[1][1],'option_three':i[1][2],'option_four':i[1][3],'correct_answer':i[2]} for i in zip(question_list,options_list_options,ans_list)]
#
#         print(question_ans_text_dict)
#
#         serializer = TeacherQuestionFilePostSerializer(data = question_ans_text_dict,many = True)
#         serializer.is_valid(raise_exception=True)
#         # print(serializer.data)
#         serializer.save()
#
#         return api_response(200,"Work in progress",serializer.data, status=True)