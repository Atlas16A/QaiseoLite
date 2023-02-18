# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtChart import QChart, QChartView
from Ui_MainScreen import Ui_QaiseoLite
import APICalls
from NetworkGraph import LiveChart
import subprocess
import os

#pyinstaller main.py -y --name "QaiseoLite" --add-binary="yagna.exe;." --add-binary="gftp.exe;." --add-binary="jq.exe;." --windowed

import inspect

print(inspect.getmodule(QChart))


class QaiseoApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(QaiseoApp, self).__init__()
        
        cwd = os.getcwd()
        yagnaPath = os.path.join(cwd, "yagna.exe")
        jqPath = os.path.join(cwd, "jq.exe")
        YagnaAppKey = None


        subprocess.Popen([yagnaPath, "service", "run"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.ui = Ui_QaiseoLite()
        self.ui.setupUi(self)

        self.BaseStackedWidget = self.findChild(QtWidgets.QStackedWidget, "stackedWidget")
        


        self.NavHandler()
    
    def ContentChange(self, index):
        self.BaseStackedWidget.setCurrentIndex(index)

    def NavHandler(self):
        self.actions = {
            "actionOverview": 0,
            "actionLive_Graphs": 1,
            "actionHistorical_Stats": 2,
            "actionGLM_Token": 3,
            "actionSwap": 4,
            "actionSend": 5,
            "actionTransaction_History": 6,
            "actionCreate_Task": 7,
            "actionLoad_Task": 8,
            "actionTask_Settings": 9,
        }
        
        for action_name, index in self.actions.items():
            action = self.findChild(QtWidgets.QAction, action_name)
            action.triggered.connect(lambda checked, index=index: self.ContentChange(index))
        
    def ApiReceive(self, Value, CallID):

        self.AvgEarnPerTask_Amount = self.findChild(QtWidgets.QLabel, "AvgEarnPerTask_Amount")
        self.NetworkEarn6H_Amount = self.findChild(QtWidgets.QLabel, "NetworkEarn6H_Amount")
        self.NetworkEarn24H_Amount = self.findChild(QtWidgets.QLabel, "NetworkEarn24H_Amount")
        self.TotalNetworkEarn_Amount = self.findChild(QtWidgets.QLabel, "TotalNetworkEarn_Amount")

        lookup = {
        1: self.AvgEarnPerTask_Amount.setText,
        2: self.NetworkEarn6H_Amount.setText,
        3: self.NetworkEarn24H_Amount.setText,
        4: self.TotalNetworkEarn_Amount.setText,
        }
        if CallID in lookup:
            lookup[CallID](Value)

    def NetworkActivityUpdate(self, timestamps, provider_amount):
        self.NetworkActivityGraph = self.findChild(QChartView, "NetworkActivityGraph")
        
        self.NetworkActivity = LiveChart()
        self.NetworkActivity.chart.setTitle("Providers Computing Right Now")
        self.NetworkActivity.providers_axis.setTitleText("Providers")
        self.NetworkActivityGraph.setChart(self.NetworkActivity.chart)
        self.NetworkActivity.update_chart(timestamps, provider_amount)
    def OnlineDiskUpdate(self, timestamps, Disk):
        self.OnlineDiskGraph = self.findChild(QChartView, "OnlineDiskGraph")
        
        self.OnlineDisk = LiveChart()
        self.OnlineDisk.chart.setTitle("Disk Online and available for compute")
        self.OnlineDisk.providers_axis.setTitleText("Disk TB")
        self.OnlineDiskGraph.setChart(self.OnlineDisk.chart)
        self.OnlineDisk.update_chart(timestamps, Disk)
    def OnlineCoresUpdate(self, timestamps, Cores):
        self.OnlineCoresGraph = self.findChild(QChartView, "OnlineCoresGraph")
        
        self.OnlineCores = LiveChart()
        self.OnlineCores.chart.setTitle("Cores Online and available for compute")
        self.OnlineCores.providers_axis.setTitleText("Cores")
        self.OnlineCoresGraph.setChart(self.OnlineCores.chart)
        self.OnlineCores.update_chart(timestamps, Cores)
    def OnlineMemoryUpdate(self, timestamps, Memory):
        self.OnlineMemoryGraph = self.findChild(QChartView, "OnlineMemoryGraph")
        
        self.OnlineMemory = LiveChart()
        self.OnlineMemory.chart.setTitle("Memory Online and available for compute")
        self.OnlineMemory.providers_axis.setTitleText("Memory TB")
        self.OnlineMemoryGraph.setChart(self.OnlineMemory.chart)
        self.OnlineMemory.update_chart(timestamps, Memory)
    def OnlineProvidersUpdate(self, timestamps, Providers):
        self.OnlineProvidersGraph = self.findChild(QChartView, "OnlineProviderGraph")
        
        self.OnlineProviders = LiveChart()
        self.OnlineProviders.chart.setTitle("Providers Online and available for compute")
        self.OnlineProviders.providers_axis.setTitleText("Providers")
        self.OnlineProvidersGraph.setChart(self.OnlineProviders.chart)
        self.OnlineProviders.update_chart(timestamps, Providers)


def main():
    ApiCallLoop = APICalls.UpdatePriceThread()
    app = QtWidgets.QApplication(sys.argv)
    Window = QaiseoApp()
    Window.show()
    APICalls.ApiThreadConnection(ApiCallLoop, Window)
    app.exec_()

if __name__ == "__main__":
    main()
