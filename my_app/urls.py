
from django.contrib import admin
from django.urls import path, include

from my_app import views

# urlpatterns = [
#     path('',views.login),
#     path('adminhome',views.adminhome),
#     path('experthome',views.experthome),
#     path('logincode',views.logincode),
#     path('addexpert',views.addexpert),
#     path('addsignlanguage',views.addsignlanguage),
#     path('blockunblock',views.blockunblock),
#     path('complaintReplay',views.complaintReplay),
#     path('managexpert',views.managexpert),
#     path('managesignlanguage',views.managesignlanguage),
#     path('viewcomplaint',views.viewcomplaint),
#     path('viewfeedback',views.viewfeedback),
#
#
#
# ]

urlpatterns = [
    path('',views.login,name="login"),
    path('AdminHome',views.AdminHome,name="AdminHome"),
    path('log_code',views.log_code,name="log_code"),
    path('ManageExpert',views.ManageExpert,name="ManageExpert"),
    path('ManageExpert_search',views.ManageExpert_search,name="ManageExpert_search"),
    path('AddExpert',views.AddExpert,name="AddExpert"),
    path('ViewUser',views.ViewUser,name="ViewUser"),
    path('ViewUser_search',views.ViewUser_search,name="ViewUser_search"),
    path('Feedback',views.Feedback,name="Feedback"),
    path('Feedback_search',views.Feedback_search,name="Feedback_search"),
    path('BlockUnblock',views.BlockUnblock,name="BlockUnblock"),
    path('BlockUnblock_search',views.BlockUnblock_search,name="BlockUnblock_search"),
    path('Complaints',views.Complaints,name="Complaints"),
    path('Complaints_search',views.Complaints_search,name="Complaints_search"),
    path('ManageAddLectures',views.ManageAddLectures,name="ManageAddLectures"),
    path('AddLecture',views.AddLecture,name="AddLecture"),
    path('EditLecture/<int:id>',views.EditLecture,name="EditLecture"),
    path('ManageAddLectures_delete/<int:id>',views.ManageAddLectures_delete,name="ManageAddLectures_delete"),
    path('editaction_lecture',views.editaction_lecture,name="editaction_lecture"),
    path('AddLecture_code',views.AddLecture_code,name="AddLecture_code"),
    path('LectureSearch',views.LectureSearch,name="LectureSearch"),
    path('ManageTest',views.ManageTest,name="ManageTest"),
    path('AddTestto',views.AddTestto,name="AddTestto"),
    path('AddTest',views.AddTest,name="AddTest"),
    path('EditTest/<int:id>',views.EditTest,name="EditTest"),
    path('DeleteTest/<int:id>',views.DeleteTest,name="DeleteTest"),
    path('AddQuestions',views.AddQuestions,name="AddQuestions"),
    path('AddQuestions_code',views.AddQuestions_code,name="AddQuestions_code"),
    path('QuestionDelete/<int:id>',views.QuestionDelete,name="QuestionDelete"),
    path('ViewQuestion/<int:id>',views.ViewQuestion,name="ViewQuestion"),
    path('Sugessions',views.Sugessions,name="Sugessions"),
    path('Reply/<int:id>',views.Reply,name="Reply"),
    path('Deletevideo/<int:id>',views.Deletevideo,name="Deletevideo"),
    path('Deletetips/<int:id>',views.Deletetips,name="Deletetips"),
    path('EditTips/<int:id>',views.EditTips,name="EditTips"),
    path('Replycode',views.Replycode,name="Replycode"),
    path('Replycode',views.Replycode,name="Replycode"),
    path('edittipsto_post',views.edittipsto_post,name="edittipsto_post"),
    path('AddExpert_code',views.AddExpert_code,name="AddExpert_code"),
    path('blockexp/<int:id>',views.blockexp,name="blockexp"),
    path('unblockexp/<int:id>',views.unblockexp,name="unblockexp"),
    path('ManageExpert_delete/<int:id>',views.ManageExpert_delete,name="ManageExpert_delete"),
    path('ManageExpert_edit/<int:id>',views.ManageExpert_edit,name="ManageExpert_edit"),
    path('updateexp',views.updateexp,name="updateexp"),
    path('ExpertHome',views.ExpertHome,name="ExpertHome"),
    path('feedbackexp',views.feedbackexp,name="feedbackexp"),
    path('Feedback_searchexp',views.Feedback_searchexp,name="Feedback_searchexp"),
    path('result',views.result,name="result"),
    path('testsearch',views.testsearch,name="testsearch"),
    path('editaction',views.editaction,name="editaction"),
    path('AdminHome_main',views.AdminHome_main,name="AdminHome_main"),
    path('experthome_main',views.experthome_main,name="experthome_main"),
    path('Sugessions_code',views.Sugessions_code,name="Sugessions_code"),
    path('Sugessions/<int:id>/<sid>',views.Sugessions,name="Sugessions"),
    path('add_camera',views.add_camera),
    path('add_camera_post',views.add_camera_post),
    path('view_camera',views.view_camera),

    path('chatwithuser', views.chatwithuser, name='chatwithuser'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),
    path('logout', views.logout, name='logout'),

    #______________________________--and
    path('and_log_code', views.and_log_code, name='and_log_code'),
    path('and_reg_code', views.and_reg_code, name='and_reg_code'),
    path('and_feedback_code', views.and_feedback_code, name='and_feedback_code'),
    path('and_complaint_code', views.and_complaint_code, name='and_complaint_code'),
    # path('and_lecture_code', views.and_complaint_code, name='and_lecture_code'),
    path('and_feeback_code', views.and_feeback_code, name='and_feeback_code'),
    path('and_lecture_code', views.and_lecture_code, name='and_lecture_code'),
    path('and_test_code', views.and_test_code, name='and_test_code'),
    path('and_compaint_view_code', views.and_compaint_view_code, name='and_compaint_view_code'),
    path('and_expert_view', views.and_expert_view, name='and_expert_view'),
    path('in_message2', views.in_message2, name='in_message2'),
    path('view_message2', views.view_message2, name='view_message2'),
    path('question_view', views.question_view, name='question_view'),
    path('and_result', views.and_result, name='and_result'),
    path('and_result_view', views.and_result_view, name='and_result_view'),
    path('and_sugession', views.and_sugession, name='and_sugession'),
    path('and_convert', views.and_convert, name='and_convert'),
    path('redirect', views.redirect, name='redirect'),
    path('guster_det', views.guster_det, name='guster_det'),
    path('Managetips', views.Managetips, name='Managetips'),
    path('Addtipsto', views.Addtipsto, name='Addtipsto'),
    path('Addtipsto_post', views.Addtipsto_post, name='Addtipsto_post'),
    path('Managevideo', views.Managevideo, name='Managevideo'),
    path('Addvideo', views.Addvideo, name='Addvideo'),
    path('Addvideo_post', views.Addvideo_post, name='Addvideo_post'),
    path('add_sign_language', views.add_sign_language, name='add_sign_language'),
    path('add_sign_language_post', views.add_sign_language_post, name='add_sign_language_post'),



path('adminwithexpert', views.chatwithuser, name='chatwithuser'),
    path('adminchatview', views.chatview, name='chatview'),
    path('admincoun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('admincoun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),







]
