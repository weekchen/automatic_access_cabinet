# coding = UTF-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Box
import string, random
from my_serial import MySerial


boxes_pos = {
        'box_100': "100#50", 'box_101': "200#50", 'box_102': "300#50",
        'box_200': "100#150", 'box_201': "200#150", 'box_202': "300#150",
        'box_300': "100#250", 'box_301': "200#250", 'box_302': "300#250",
        'box_400': "100#350", 'box_401': "200#350", 'box_402': "300#350",
        }


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def take_in(request):
    boxes = {
        'box_100': "red", 'box_101': "#21fc94", 'box_102': "red",
        'box_200': "red", 'box_201': "#21fc94", 'box_202': "red",
        'box_300': "red", 'box_301': "#21fc94", 'box_302': "red",
        'box_400': "red", 'box_401': "#21fc94", 'box_402': "red",
    }
    box_list = Box.objects.all()
    for var in box_list:
        box_name = var.name
        if var.status == "empty" and box_name != 'box_100':
            boxes[box_name] = "#21fc94"
        elif box_name == 'box_100':
            boxes[box_name] = "yellow"
        else:
            boxes[box_name] = "red"
    return render(request, 'take_in.html', context=boxes)


def take_out(request):
    return render(request, 'take_out.html')


def update_status_out(request):
    message = ""
    if request.method == 'GET':
        box_list = Box.objects.all()
        if 'pwd' in request.GET and request.GET['pwd']:
            pwd = request.GET['pwd']
            for var in box_list:
                password = var.password
                if pwd == password:
                    message = "FOUND" + " " + var.name
                    # TODO:货物已搜寻到，返回 var.name 的坐标给你下位机
                    my_serial = MySerial("COM4", 9600, None)
                    my_serial.send_data(boxes_pos[var.name])
                    msg = ''
                    while len(msg) < 4:
                        msg = my_serial.read_data()
                    my_serial.close_port()
                    print(msg)
                    print("取货坐标为" + boxes_pos[var.name])
                    # message = msg
                    # 更新数据库
                    Box.objects.filter(name=var.name).update(status='empty', password='null')
                    break
        if message == "":
            message = "取件码错误，NOT FOUND"
    else:
        message = "something wrong"
    return HttpResponse(message)


def update_status_in(request):
    message = ""
    if request.method == 'GET':
        box_list = Box.objects.all()
        if 'box_num' in request.GET and request.GET['box_num']:
            name = request.GET['box_num']
            for var in box_list:
                if var.name == name:
                    break
            if var.status == 'empty':
                pwd = get_pwd()
                Box.objects.filter(name=var.name).update(status='occupy', password=pwd)
                message = "存储成功，你的取件密码为" + " " + pwd
                #     TODO:存货口已选择，返回 var.name 的坐标给你下位机
                my_serial = MySerial("COM4", 9600, None)
                print("存货坐标为" + boxes_pos[var.name])
                my_serial.send_data(boxes_pos[var.name])
                msg = ''
                while len(msg) < 4:
                    msg = my_serial.read_data()
                print(msg)
                my_serial.close_port()
            else:
                message = "该柜子已占用，请选择其他柜子"
    else:
        message = "something wrong"
    return HttpResponse(message)


def get_pwd():
    seeds = string.digits
    random_str = []
    for i in range(4):
        random_str.append(random.choice(seeds))
    # print("".join(random_str))
    pwd = "".join(random_str)
    return pwd
