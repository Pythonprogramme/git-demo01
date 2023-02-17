# 引入常见的基础模块
from django.shortcuts import render, HttpResponse, redirect, reverse
# 插入 django.http 模块
from django.http import JsonResponse,FileResponse
# 插入时间日期
from datetime import datetime, date,timedelta
# 插入 Q查询
from django.db.models import Q ,Sum
# 插入随机函数
import random
# 插入 setting
from django.conf import settings