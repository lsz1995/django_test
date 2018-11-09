from django.shortcuts import render
from django.views.generic.base import View
from apps.message.models import UserMessage
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
# Create your views here.
import json
from django.http import JsonResponse


class LoginView(View):
        def get(self, request):


            return render(request, "login.html" )

        def post(self, request):

                user_name = request.POST

                print(user_name)
               # return HttpResponse('{"status":"success"}', content_type='application/json')  # 不返回网页 返回json给浏览器
                response = HttpResponseRedirect(reverse('index'))
                return response
class ApiView(View):
        def get(self,request):

                page =request.GET.get('page', '')
                city =request.GET.get('city', '')

                return JsonResponse({"result": 0, "msg": page+' '+city})
        def post(self,request):

                page = request.GET.get('page', '')
                city =request.GET.get('city', '')
                # username =request.POST.get("username")
                # password = request.POST.get("password")
                # data = {
                #         'page':page,
                #         'username':username,
                #         'password':password,
                #         'city':city,
                # }
                #
                #
                # return JsonResponse({"result": 0, "msg": data})

                data = serializers.serialize('json', UserMessage.objects.all(), fields=('name', 'address'))

                sent_data ={
                        'page':page,
                        'city':city,
                        'data':json.loads(data),
                }
                return HttpResponse(json.dumps(sent_data), content_type='application/json')
