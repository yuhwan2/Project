# views.py
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import csv

def check(request):
    return render(request, 'check/check.html')

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df









def chart_data(request):

    df = read_csv_file(r'D:\Team3\Project\Data\gens\2022-06-23.csv')

    # 시간과 예측값을 가져와서 리스트로 변환
    labels = df['time'].tolist()
    data = df['amount'].tolist()
    chart_data = {
        'labels': labels,
        'data': data,
    }

    return JsonResponse(chart_data)
