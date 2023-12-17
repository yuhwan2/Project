import pandas as pd
import matplotlib.pyplot as plt
import os

def read_csv_file(file_path):
    # CSV 파일 읽기
    return pd.read_csv(file_path)

def generate_plot(csv_data):
    # 플롯 생성
    plt.plot(csv_data['time'], csv_data['Predicted'])
    plt.xlabel('Time')
    plt.ylabel('Predicted Value')

    # 정적 파일로 저장
    plot_path = 'check/static/plot.png'
    plt.savefig(plot_path)

    return plot_path
