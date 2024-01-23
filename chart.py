from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox as mb
yf.pdr_override()


def chart_dollar():
    df = pdr.get_data_yahoo('USDRUB=X', start='2022-01-20', end='2023-01-20')
    if df.index[0] != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("ДОЛЛАР", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show()
    else: show_warning()

# нету
def chart_tenge():
    df = pdr.get_data_yahoo('RUBKZT=X', start='2020-01-20', end='2021-01-20')
    if df.index != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("ТЕНГЕ", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show()
    else: show_warning()

def chart_euro():
    df = pdr.get_data_yahoo('EURRUB=X', start='2022-01-20', end='2023-01-20')
    if df.index != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("ЕВРО", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show()
    else: show_warning()

# нету
def chart_yuan():
    df = pdr.get_data_yahoo('CNYRUB=X', start='2011-01-01', end='2024-01-20')
    if df.index != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("ЮЯНЬ", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show()
    else: show_warning()

# нету
def chart_shekel():
    df = pdr.get_data_yahoo('ILSRUB=X', start='2022-01-20', end='2023-01-20')
    if df.index != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("ШЕКЕЛЬ", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show()
    else: show_warning()

def chart_yen():
    df = pdr.get_data_yahoo('RUBJPY=X', start='2011-01-20', end='2023-01-20')
    if df.index != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("ЙЕНА", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show() 
    else: show_warning()

def chart_pound():
    df = pdr.get_data_yahoo('GBPRUB=X', start='2022-01-20', end='2023-01-20')
    if df.index != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("ФУНТ СТЕРЛНГОВ", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show()
    else: show_warning()

# нету
def chart_rupiah():
    df = pdr.get_data_yahoo('INRRUB=X', start='2022-01-20', end='2023-01-20')
    if df.index != None:
        fig = plt.figure(figsize=(16, 8))
        ax = fig.subplots(1)
        ax.plot(df.index, df['Close'])
        ax.set_title("РУПИЙ", size=20, color='black')
        ax.grid(True)
        plt.tight_layout()
        plt.show()
    else: show_warning()

def show_warning():
    msg = "Данные отсутствуют"
    mb.showwarning("ВНИМАНИЕ", msg)