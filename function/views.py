from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from django.conf import settings  # 导入配置文件
from django.core.mail import send_mail  # 导入发送邮件的包
import json
from snownlp import sentiment,SnowNLP



@csrf_exempt
def count(request):
    # 低分未处理
    low_unprocesseds = Comments.objects.filter(sys_score__lte=0.5,is_scored=0)
    low_unprocessed = 0
    for i in low_unprocesseds:
        low_unprocessed = low_unprocessed + 1
    # 低分已处理
    low_processeds = Comments.objects.filter(sys_score__lte=0.5, is_scored=1)
    low_processed = 0
    for i in low_processeds:
        low_processed = low_processed + 1
    # 高分未处理
    high_unprocesseds = Comments.objects.filter(sys_score__gt=0.5, is_scored=0)
    high_unprocessed = 0
    for i in high_unprocesseds:
        high_unprocessed = high_unprocessed + 1
    # 高分已处理
    high_processeds = Comments.objects.filter(sys_score__gt=0.5, is_scored=1)
    high_processed = 0
    for i in high_processeds:
        high_processed = high_processed + 1
    # print({"low_unprocessed": low_unprocessed, "low_processed": low_processed, "high_unprocessed": high_unprocessed,
    #      "high_processed": high_processed, "msg": "success"})

    return JsonResponse({"low_unprocessed":low_unprocessed,"low_processed":low_processed,
                         "high_unprocessed": high_unprocessed,"high_processed":high_processed,"msg":"success"})
@csrf_exempt
def index(request):
    return render(request,"function/index.html")

@csrf_exempt
def low_unprocessed_list_html(request):
    return render(request,"function/comment_list_low_unprocessed.html")

@csrf_exempt
def high_unprocessed_list_html(request):
    return render(request,"function/comment_list_high_unprocessed.html")

@csrf_exempt
def low_processed_list_html(request):
    return render(request,"function/comment_list_low_processed.html")

@csrf_exempt
def high_processed_list_html(request):
    return render(request,"function/comment_list_high_processed.html")

@csrf_exempt
def comment_content_low_processed(request):
    return render(request,"function/comment_content_low_processed.html")

@csrf_exempt
def comment_content_low_unprocessed(request):
    return render(request,"function/comment_content_low_unprocessed.html")

@csrf_exempt
def comment_content_high_processed(request):
    return render(request,"function/comment_content_high_processed.html")

@csrf_exempt
def comment_content_high_unprocessed(request):
    return render(request,"function/comment_content_high_unprocessed.html")

@csrf_exempt
def admin(request):
    return render(request,"admin/index.html")

@csrf_exempt
def comment_list(request):

    library = request.POST.get("library")
    process = request.POST.get("process")
    page_current = int(request.POST.get("page_current"))
    start = (page_current-1)*10
    end = (page_current * 10)

    low_unprocesseds = Comments.objects.filter(sys_score__lte=0.5, is_scored=0)
    low_unprocessed = 0
    for i in low_unprocesseds:
        low_unprocessed = low_unprocessed + 1
    # 低分已处理
    low_processeds = Comments.objects.filter(sys_score__lte=0.5, is_scored=1)
    low_processed = 0
    for i in low_processeds:
        low_processed = low_processed + 1
    # 高分未处理
    high_unprocesseds = Comments.objects.filter(sys_score__gt=0.5, is_scored=0)
    high_unprocessed = 0
    for i in high_unprocesseds:
        high_unprocessed = high_unprocessed + 1
    # 高分已处理
    high_processeds = Comments.objects.filter(sys_score__gt=0.5, is_scored=1)
    high_processed = 0
    for i in high_processeds:
        high_processed = high_processed + 1

    # 低分未处理

    if library == 'low' and process == 'unprocessed':
        low_un_list = []
        low_unprocesseds = Comments.objects.filter(sys_score__lte=0.5, is_scored=0)
        for i in low_unprocesseds[start:end]:
            low_un_list.append({"id": i.comment_id,"catch_time": i.catch_time,"comment_time": i.comment_time,
                                "final_score": i.sys_score})
        pages = (low_unprocessed // 10)

        if low_unprocessed % 10 != 0:
            pages = pages +1
        return JsonResponse({"msg": "success", "items": low_un_list, "pages": pages})

    # 低分已处理

    if library == 'low' and process == 'processed':
        low_list = []
        low_processeds = Comments.objects.filter(sys_score__lte=0.5, is_scored=1)
        for i in low_processeds[start:end]:
            low_list.append({"id": i.comment_id,"catch_time": i.catch_time,"comment_time": i.comment_time,
                             "final_score": i.sys_score})
        pages = (low_processed // 10)

        if low_processed % 10 != 0:
            pages = pages +1
        return JsonResponse({"msg": "success", "items": low_list, "pages": pages})

    # 高分未处理
    if library == 'high' and process == 'unprocessed':
        high_un_list = []
        high_unprocesseds = Comments.objects.filter(sys_score__gt=0.5, is_scored=0)
        for i in high_unprocesseds[start:end]:
            high_un_list.append({"id": i.comment_id,"catch_time": i.catch_time,"comment_time": i.comment_time,
                                 "final_score": i.sys_score})
        pages = (high_unprocessed // 10)

        if high_unprocessed % 10 != 0:
            pages = pages +1
        return JsonResponse({"msg": "success", "items": high_un_list, "pages": pages})

    # 高分已处理

    if library == 'high' and process == 'processed':
        high_list = []
        high_processeds = Comments.objects.filter(sys_score__gt=0.5, is_scored=1)
        for i in high_processeds[start:end]:
            high_list.append({"id": i.comment_id,"catch_time": i.catch_time,"comment_time": i.comment_time,
                              "final_score": i.sys_score})
        pages = (high_processed // 10)

        if high_processed % 10 != 0:
            pages = pages +1
        return JsonResponse({"msg": "success", "items": high_list, "pages": pages})


@csrf_exempt
def count1(request):
    comment_id = int(request.POST.get("comment_id"))
    comment = Comments.objects.get(comment_id = comment_id)
    low_comment = []
    low_comments = Comments.objects.filter(sys_score__lte = 0.5)
    for x in (low_comments):
        low_comment.append(x.comment_id)
    if comment.comment_id in low_comment:
        if comment.is_scored == 0:
            library = "low"
            process = "unprocessed"
            dic = {"msg" : "success", "library" : library, "process" : process, "comment_id" : comment_id}
            return HttpResponse(json.dumps(dic))
        else:
            library = "low"
            process = "processed"
            dic = {"msg" : "success", "library" : library, "process" : process, "comment_id" : comment_id}
            return HttpResponse(json.dumps(dic))

    else:
        if comment.is_scored == 0:
            library = "high"
            process = "unprocessed"
            dic = {"msg" : "success", "library" : library, "process" : process, "comment_id" : comment_id}
            return HttpResponse(json.dumps(dic))
        else:
            library = "high"
            process = "processed"
            dic = {"msg" : "success", "library" : library, "process" : process, "comment_id" : comment_id}
            return HttpResponse(json.dumps(dic))


@csrf_exempt
def comment_content(request):
    library = request.POST.get("library")
    comment_Id = str(request.POST.get("comment_id"))
    # 低分
    if library == 'low':
        comment = Comments.objects.get(comment_id=comment_Id)
        man = []
        manager = AuthUser.objects.filter()
        for x in manager:
            man.append(x.username)
        if not comment.arti_score and comment.is_scored == 0:
            arti_score="Null"
            dict2 = [{"manager" : man, "comment_id" : comment.comment_id , "catch_address" : comment.address,
                  "catch_time" : comment.catch_time,"comment_time" : comment.comment_time,
                  "sys_score" : comment.sys_score, "comment_content" : comment.content,
                  'arti_score' : arti_score}]
            return JsonResponse({"msg" : "success", "dic" : dict2})
        else:
            arti_score=comment.arti_score
            dict2 = [{"manager" : man, "comment_id" : comment.comment_id , "catch_address" : comment.address,
                  "catch_time" : comment.catch_time,"comment_time" : comment.comment_time,
                  "sys_score" : comment.sys_score, "comment_content" : comment.content,
                  'arti_score' : arti_score}]
            return JsonResponse({"msg" : "success", "dic" : dict2})

    # 高分
    if library == 'high':
        comment = Comments.objects.get(comment_id=comment_Id)
        man = []
        manager = AuthUser.objects.filter()
        for x in manager:
            man.append(x.username)
        if not comment.arti_score and comment.is_scored == 0:
            arti_score="Null"
            dict2 = [{"manager" : man, "comment_id" : comment.comment_id , "catch_address" : comment.address,
                  "catch_time" : comment.catch_time,"comment_time" : comment.comment_time,
                  "sys_score" : comment.sys_score, "comment_content" : comment.content,
                  'arti_score' : arti_score}]
            return JsonResponse({"msg" : "success", "dic" : dict2})
        else:
            arti_score=comment.arti_score
            dict2 = [{"manager" : man, "comment_id" : comment.comment_id , "catch_address" : comment.address,
                  "catch_time" : comment.catch_time,"comment_time" : comment.comment_time,
                  "sys_score" : comment.sys_score, "comment_content" : comment.content,
                  'arti_score' : arti_score}]
            return JsonResponse({"msg" : "success", "dic" : dict2})


# 人工评分
@csrf_exempt
def submit_newscore(request):
    comment_current_id = request.POST.get('comment_current_id')
    new_score = request.POST.get('new_score')
    if new_score:
        Comments.objects.filter(comment_id = comment_current_id).update(arti_score=new_score,is_scored=1)
        return JsonResponse({"msg" : "success"})
    else:
        return JsonResponse({"msg" : "failure"})


# 发送邮件
@csrf_exempt
def send_message(request):
    comment_current_id = request.POST.get('comment_current_id')
    manager = request.POST.get('manager')
    manage = AuthUser.objects.get(username = manager)
    comment = Comments.objects.get(comment_id = comment_current_id)
    commentId = comment.comment_id
    comment_address = comment.address
    comment_content = comment.content
    sys_score = comment.sys_score
    arti_score=comment.arti_score
    mail = manage.email

    content = str('评论ID:'+str(commentId)+',        '+'评论地址:'+comment_address+',        '+
                  '评论内容:'+comment_content+',        '+'系统评分:'+str(sys_score)+',        '+
                  '人工评分'+str(arti_score))

    send_title = '评论' # 邮件主题
    send_message = content  #邮件内容
    send_obj_list = [mail]  # 收件人列表
    send_html_message = '<h1>包含 html 标签且不希望被转义的内容</h1>'
    send_status = send_mail(send_title, send_message, settings.EMAIL_FROM, send_obj_list, send_html_message)
    # print(send_status)  # 发送状态,可用可不用
    if send_status == 1:
        return JsonResponse({"msg" : "success"})
    else:
        return JsonResponse({"msg" : "failure"})


#翻页
@csrf_exempt
def changeitems(request):
    man = []
    library = request.POST.get("library")
    comment_id = int(request.POST.get("comment_current_id"))
    target = request.POST.get('target')
    process = request.POST.get('process')
    manager = AuthUser.objects.all()
    for x in manager:
        man.append(x.username)
    # 低分-已处理
    if library == "low" and process == "processed":
        commentLi = Comments.objects.filter(sys_score__lte=0.5, is_scored=1)
        list=[]
        for i in commentLi:
            list.append(i.comment_id)
        #上一页
        if target == "previous":
            commentList = []
            for x in commentLi:
                if x.comment_id < comment_id:
                    commentList.append(x.comment_id)
            if commentList == []:
                comment = Comments.objects.get(comment_id = list[-1])
                dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                          "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                          "sys_score": comment.sys_score, "comment_content": comment.content}]
                return JsonResponse({"msg": "success", "dic": dict2})
            else:
                for y in commentList[::-1]:
                    if comment_id - y > 0:
                        comment = Comments.objects.get(comment_id = y)
                        dict2 = [{"manager" : man, "comment_id" : comment.comment_id, "catch_address" : comment.address,
                              "catch_time" : comment.catch_time, "comment_time" : comment.comment_time,
                              "sys_score" : comment.sys_score, "comment_content" : comment.content}]
                        return JsonResponse({"msg" : "success", "dic" : dict2})
                    else:
                        return JsonResponse({"msg" : "failure"})
        #下一页
        else:
            commentList = []
            for x in commentLi:
                if x.comment_id > comment_id:
                    commentList.append(x.comment_id)
            if commentList == []:
                comment = Comments.objects.get(comment_id = list[0])
                dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                          "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                          "sys_score": comment.sys_score, "comment_content": comment.content}]
                return JsonResponse({"msg": "success", "dic": dict2})
            else:
                for y in commentList:
                    if y - comment_id > 0:
                        comment = Comments.objects.get(comment_id = y)
                        dict2 = [{"manager" : man, "comment_id" : comment.comment_id, "catch_address" : comment.address,
                              "catch_time" : comment.catch_time, "comment_time" : comment.comment_time,
                              "sys_score" : comment.sys_score, "comment_content" : comment.content}]
                        return JsonResponse({"msg" : "success", "dic" : dict2})
                    else:
                        return JsonResponse({"msg" : "failure"})
    # 低分-未处理
    if library == "low" and process == "unprocessed":
        commentLi = Comments.objects.filter(sys_score__lte = 0.5, is_scored = 0)
        list = []
        for i in commentLi:
            list.append(i.comment_id)
        if list == []:
            return JsonResponse({"msg" : "index"})
        else:
            # 上一页
            if target == "previous":
                commentList = []
                for x in commentLi:
                    if x.comment_id < comment_id:
                        commentList.append(x.comment_id)
                if commentList == []:
                    comment = Comments.objects.get(comment_id = list[-1])
                    dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                              "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                              "sys_score": comment.sys_score, "comment_content": comment.content}]
                    return JsonResponse({"msg": "success", "dic": dict2})
                else:
                    for y in commentList[::-1]:
                        if comment_id - y > 0:
                            comment = Comments.objects.get(comment_id=y)
                            dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                                      "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                                      "sys_score": comment.sys_score, "comment_content": comment.content}]
                            return JsonResponse({"msg": "success", "dic": dict2})
                        else:
                            return JsonResponse({"msg": "failure"})
            # 下一页
            else:
                commentList = []
                for x in commentLi:
                    if x.comment_id > comment_id:
                        commentList.append(x.comment_id)
                if commentList == []:
                    comment = Comments.objects.get(comment_id = list[0])
                    dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                              "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                              "sys_score": comment.sys_score, "comment_content": comment.content}]
                    return JsonResponse({"msg": "success", "dic": dict2})
                else:
                    for y in commentList:
                        if y - comment_id > 0:
                            comment = Comments.objects.get(comment_id=y)
                            dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                                      "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                                      "sys_score": comment.sys_score, "comment_content": comment.content}]
                            return JsonResponse({"msg": "success", "dic": dict2})
                        else:
                            return JsonResponse({"msg": "failure"})

    # 高分-已处理
    if library == "high" and process == "processed":
        commentLi = Comments.objects.filter(sys_score__gt=0.5, is_scored=1)
        list=[]
        for i in commentLi:
            list.append(i.comment_id)
        # 上一页
        if target == "previous":
            commentList = []
            for x in commentLi:
                if x.comment_id < comment_id:
                    commentList.append(x.comment_id)
            if commentList == []:
                comment = Comments.objects.get(comment_id = list[-1])
                dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                          "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                          "sys_score": comment.sys_score, "comment_content": comment.content}]
                return JsonResponse({"msg": "success", "dic": dict2})
            else:
                for y in commentList[::-1]:
                    if comment_id - y > 0:
                        comment = Comments.objects.get(comment_id=y)
                        dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                                  "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                                  "sys_score": comment.sys_score, "comment_content": comment.content}]
                        return JsonResponse({"msg": "success", "dic": dict2})
                    else:
                        return JsonResponse({"msg": "failure"})
        # 下一页
        else:
            commentList = []
            for x in commentLi:
                if x.comment_id > comment_id:
                    commentList.append(x.comment_id)
            if commentList == []:
                comment = Comments.objects.get(comment_id = list[0])
                dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                          "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                          "sys_score": comment.sys_score, "comment_content": comment.content}]
                return JsonResponse({"msg": "success", "dic": dict2})
            else:
                for y in commentList:
                    if y - comment_id > 0:
                        comment = Comments.objects.get(comment_id=y)
                        dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                                  "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                                  "sys_score": comment.sys_score, "comment_content": comment.content}]
                        return JsonResponse({"msg": "success", "dic": dict2})
                    else:
                        return JsonResponse({"msg": "failure"})
    # 高分-未处理
    if library == "high" and process == "unprocessed":
        commentLi = Comments.objects.filter(sys_score__gt=0.5, is_scored=0)
        list=[]
        for i in commentLi:
            list.append(i.comment_id)
        if list == []:
            return JsonResponse({"msg": "index"})
        else:
            # 上一页
            if target == "previous":
                commentList = []
                for x in commentLi:
                    if x.comment_id < comment_id:
                        commentList.append(x.comment_id)
                if commentList == []:
                    comment = Comments.objects.get(comment_id = list[-1])
                    dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                              "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                              "sys_score": comment.sys_score, "comment_content": comment.content}]
                    return JsonResponse({"msg": "success", "dic": dict2})
                else:
                    for y in commentList[::-1]:
                        if comment_id - y > 0:
                            comment = Comments.objects.get(comment_id=y)
                            dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                                      "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                                      "sys_score": comment.sys_score, "comment_content": comment.content}]
                            return JsonResponse({"msg": "success", "dic": dict2})
                        else:
                            return JsonResponse({"msg": "failure"})
            # 下一页
            else:
                commentList = []
                for x in commentLi:
                    if x.comment_id > comment_id:
                        commentList.append(x.comment_id)
                if commentList == []:
                    comment = Comments.objects.get(comment_id = list[0])
                    dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                              "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                              "sys_score": comment.sys_score, "comment_content": comment.content}]
                    return JsonResponse({"msg": "success", "dic": dict2})
                else:
                    for y in commentList:
                        if y - comment_id > 0:
                            comment = Comments.objects.get(comment_id=y)
                            dict2 = [{"manager": man, "comment_id": comment.comment_id, "catch_address": comment.address,
                                      "catch_time": comment.catch_time, "comment_time": comment.comment_time,
                                      "sys_score": comment.sys_score, "comment_content": comment.content}]
                            return JsonResponse({"msg": "success", "dic": dict2})
                        else:
                            return JsonResponse({"msg": "failure"})

@csrf_exempt
def save_train(request):
    f = open('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/snownlp/sentiment/SGMW_pos.txt','w')
    high_processeds = Comments.objects.filter(arti_score__gt=0.5, is_scored=1)
    for i in high_processeds:
        high_list = i.content
        f.write('\n')
        f.write(high_list)
    f.close()

    f = open('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/snownlp/sentiment/SGMW_neg.txt', 'w')
    low_processeds = Comments.objects.filter(arti_score__lte=0.5, is_scored=1)
    for i in low_processeds:
        low_list = i.content
        f.write('\n')
        f.write(low_list)
    f.close()

    sentiment.train('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/snownlp/sentiment/SGMW_neg.txt','/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/snownlp/sentiment/SGMW_pos.txt')
    sentiment.save('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/snownlp/sentiment/SGMW_sentiment.marshal')

    return JsonResponse({"msg": "success"})

@csrf_exempt
def precision(request):
    sample = 0
    right = 0
    wrong = 0
    is_scoreds = Comments.objects.filter(is_scored=1)
    for i in is_scoreds:
        sample = sample + 1
        if (i.arti_score <= 0.5 and i.sys_score <= 0.5) or (i.arti_score>0.5 and i.sys_score>0.5):
            right = right + 1
        else:
            wrong = wrong + 1
    precision_rate = round((right / sample),4)
    j = json.dumps(str(str(precision_rate*100) + "%" + "，    总数：" + str(sample) + "，   正确数：" + str(right) + "，   错误数：" + str(wrong)),ensure_ascii=False)
    return JsonResponse({"msg":"success", "accuracy": j})
@csrf_exempt
def sys_all(request):
    samples = Comments.objects.all()
    for i in samples:
         s = SnowNLP(str(i.content))
         i.sys_score = s.sentiments
         i.save()

    return JsonResponse({"msg": "success"})
