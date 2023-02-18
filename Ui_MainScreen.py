# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\YagnaInstaller\QasieoQT\Qaiseo\QaiseoSimple\QaiseoLite\MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QaiseoLite(object):
    def setupUi(self, QaiseoLite):
        QaiseoLite.setObjectName("QaiseoLite")
        QaiseoLite.resize(1085, 505)
        self.centralwidget = QtWidgets.QWidget(QaiseoLite)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: rgb(42, 43, 66);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Network_Stats_Overview = QtWidgets.QWidget()
        self.Network_Stats_Overview.setObjectName("Network_Stats_Overview")
        self.gridLayout = QtWidgets.QGridLayout(self.Network_Stats_Overview)
        self.gridLayout.setObjectName("gridLayout")
        self.BasicNetworkStatsContainer = QtWidgets.QFrame(self.Network_Stats_Overview)
        self.BasicNetworkStatsContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BasicNetworkStatsContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BasicNetworkStatsContainer.setObjectName("BasicNetworkStatsContainer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.BasicNetworkStatsContainer)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AvgEarnPerTaskContainer = QtWidgets.QFrame(self.BasicNetworkStatsContainer)
        self.AvgEarnPerTaskContainer.setStyleSheet("background-color: rgb(85, 85, 131);\n"
"background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.AvgEarnPerTaskContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AvgEarnPerTaskContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AvgEarnPerTaskContainer.setObjectName("AvgEarnPerTaskContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.AvgEarnPerTaskContainer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AvgEarnPerTask = QtWidgets.QLabel(self.AvgEarnPerTaskContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        self.AvgEarnPerTask.setFont(font)
        self.AvgEarnPerTask.setAlignment(QtCore.Qt.AlignCenter)
        self.AvgEarnPerTask.setObjectName("AvgEarnPerTask")
        self.verticalLayout_2.addWidget(self.AvgEarnPerTask)
        self.AvgEarnPerTask_Amount = QtWidgets.QLabel(self.AvgEarnPerTaskContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        font.setBold(True)
        self.AvgEarnPerTask_Amount.setFont(font)
        self.AvgEarnPerTask_Amount.setAlignment(QtCore.Qt.AlignCenter)
        self.AvgEarnPerTask_Amount.setObjectName("AvgEarnPerTask_Amount")
        self.verticalLayout_2.addWidget(self.AvgEarnPerTask_Amount)
        self.horizontalLayout.addWidget(self.AvgEarnPerTaskContainer)
        self.NetworkEarn6HContainer = QtWidgets.QFrame(self.BasicNetworkStatsContainer)
        self.NetworkEarn6HContainer.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.NetworkEarn6HContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NetworkEarn6HContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NetworkEarn6HContainer.setObjectName("NetworkEarn6HContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.NetworkEarn6HContainer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.NetworkEarn6H = QtWidgets.QLabel(self.NetworkEarn6HContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        self.NetworkEarn6H.setFont(font)
        self.NetworkEarn6H.setAlignment(QtCore.Qt.AlignCenter)
        self.NetworkEarn6H.setObjectName("NetworkEarn6H")
        self.verticalLayout_3.addWidget(self.NetworkEarn6H)
        self.NetworkEarn6H_Amount = QtWidgets.QLabel(self.NetworkEarn6HContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        font.setBold(True)
        self.NetworkEarn6H_Amount.setFont(font)
        self.NetworkEarn6H_Amount.setAlignment(QtCore.Qt.AlignCenter)
        self.NetworkEarn6H_Amount.setObjectName("NetworkEarn6H_Amount")
        self.verticalLayout_3.addWidget(self.NetworkEarn6H_Amount)
        self.horizontalLayout.addWidget(self.NetworkEarn6HContainer)
        self.NetworkEarn24HContainer = QtWidgets.QFrame(self.BasicNetworkStatsContainer)
        self.NetworkEarn24HContainer.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.NetworkEarn24HContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NetworkEarn24HContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NetworkEarn24HContainer.setObjectName("NetworkEarn24HContainer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.NetworkEarn24HContainer)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.NetworkEarn24H = QtWidgets.QLabel(self.NetworkEarn24HContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        self.NetworkEarn24H.setFont(font)
        self.NetworkEarn24H.setAlignment(QtCore.Qt.AlignCenter)
        self.NetworkEarn24H.setObjectName("NetworkEarn24H")
        self.verticalLayout_4.addWidget(self.NetworkEarn24H)
        self.NetworkEarn24H_Amount = QtWidgets.QLabel(self.NetworkEarn24HContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        font.setBold(True)
        self.NetworkEarn24H_Amount.setFont(font)
        self.NetworkEarn24H_Amount.setAlignment(QtCore.Qt.AlignCenter)
        self.NetworkEarn24H_Amount.setObjectName("NetworkEarn24H_Amount")
        self.verticalLayout_4.addWidget(self.NetworkEarn24H_Amount)
        self.horizontalLayout.addWidget(self.NetworkEarn24HContainer)
        self.TotalNetworkEarnContainer = QtWidgets.QFrame(self.BasicNetworkStatsContainer)
        self.TotalNetworkEarnContainer.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.TotalNetworkEarnContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TotalNetworkEarnContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TotalNetworkEarnContainer.setObjectName("TotalNetworkEarnContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.TotalNetworkEarnContainer)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TotalNetworkEarn = QtWidgets.QLabel(self.TotalNetworkEarnContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        self.TotalNetworkEarn.setFont(font)
        self.TotalNetworkEarn.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalNetworkEarn.setObjectName("TotalNetworkEarn")
        self.verticalLayout_5.addWidget(self.TotalNetworkEarn)
        self.TotalNetworkEarn_Amount = QtWidgets.QLabel(self.TotalNetworkEarnContainer)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        font.setBold(True)
        self.TotalNetworkEarn_Amount.setFont(font)
        self.TotalNetworkEarn_Amount.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalNetworkEarn_Amount.setObjectName("TotalNetworkEarn_Amount")
        self.verticalLayout_5.addWidget(self.TotalNetworkEarn_Amount)
        self.horizontalLayout.addWidget(self.TotalNetworkEarnContainer)
        self.gridLayout.addWidget(self.BasicNetworkStatsContainer, 0, 0, 1, 1)
        self.NetworkChartData = QtWidgets.QToolBox(self.Network_Stats_Overview)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        self.NetworkChartData.setFont(font)
        self.NetworkChartData.setObjectName("NetworkChartData")
        self.Providers = QtWidgets.QWidget()
        self.Providers.setGeometry(QtCore.QRect(0, 0, 1067, 233))
        self.Providers.setObjectName("Providers")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Providers)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.OnlineProviderGraph = QChartView(self.Providers)
        self.OnlineProviderGraph.setObjectName("OnlineProviderGraph")
        self.horizontalLayout_4.addWidget(self.OnlineProviderGraph)
        self.NetworkChartData.addItem(self.Providers, "")
        self.Cores = QtWidgets.QWidget()
        self.Cores.setGeometry(QtCore.QRect(0, 0, 1067, 233))
        self.Cores.setObjectName("Cores")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Cores)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.OnlineCoresGraph = QChartView(self.Cores)
        self.OnlineCoresGraph.setObjectName("OnlineCoresGraph")
        self.horizontalLayout_5.addWidget(self.OnlineCoresGraph)
        self.NetworkChartData.addItem(self.Cores, "")
        self.Memory = QtWidgets.QWidget()
        self.Memory.setGeometry(QtCore.QRect(0, 0, 1067, 233))
        self.Memory.setObjectName("Memory")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Memory)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.OnlineMemoryGraph = QChartView(self.Memory)
        self.OnlineMemoryGraph.setObjectName("OnlineMemoryGraph")
        self.horizontalLayout_6.addWidget(self.OnlineMemoryGraph)
        self.NetworkChartData.addItem(self.Memory, "")
        self.Disk = QtWidgets.QWidget()
        self.Disk.setGeometry(QtCore.QRect(0, 0, 1067, 233))
        self.Disk.setObjectName("Disk")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Disk)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.OnlineDiskGraph = QChartView(self.Disk)
        self.OnlineDiskGraph.setObjectName("OnlineDiskGraph")
        self.horizontalLayout_7.addWidget(self.OnlineDiskGraph)
        self.NetworkChartData.addItem(self.Disk, "")
        self.NetworkActivity = QtWidgets.QWidget()
        self.NetworkActivity.setGeometry(QtCore.QRect(0, 0, 1067, 233))
        self.NetworkActivity.setObjectName("NetworkActivity")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.NetworkActivity)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.NetworkActivityGraph = QChartView(self.NetworkActivity)
        self.NetworkActivityGraph.setFrameShadow(QtWidgets.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.NetworkActivityGraph.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.NetworkActivityGraph.setForegroundBrush(brush)
        self.NetworkActivityGraph.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.NetworkActivityGraph.setObjectName("NetworkActivityGraph")
        self.horizontalLayout_3.addWidget(self.NetworkActivityGraph)
        self.NetworkChartData.addItem(self.NetworkActivity, "")
        self.gridLayout.addWidget(self.NetworkChartData, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.Network_Stats_Overview)
        self.Network_Stats_Live_Graphs = QtWidgets.QWidget()
        self.Network_Stats_Live_Graphs.setObjectName("Network_Stats_Live_Graphs")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Network_Stats_Live_Graphs)
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.NetworkCPUVendorDist = QtWidgets.QFrame(self.Network_Stats_Live_Graphs)
        self.NetworkCPUVendorDist.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.NetworkCPUVendorDist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NetworkCPUVendorDist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NetworkCPUVendorDist.setObjectName("NetworkCPUVendorDist")
        self.gridLayout_2.addWidget(self.NetworkCPUVendorDist, 0, 0, 1, 1)
        self.NetworkCPUArch = QtWidgets.QFrame(self.Network_Stats_Live_Graphs)
        self.NetworkCPUArch.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.NetworkCPUArch.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NetworkCPUArch.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NetworkCPUArch.setObjectName("NetworkCPUArch")
        self.gridLayout_2.addWidget(self.NetworkCPUArch, 0, 1, 1, 1)
        self.InvoicesPaid1H = QtWidgets.QFrame(self.Network_Stats_Live_Graphs)
        self.InvoicesPaid1H.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.InvoicesPaid1H.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InvoicesPaid1H.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InvoicesPaid1H.setObjectName("InvoicesPaid1H")
        self.gridLayout_2.addWidget(self.InvoicesPaid1H, 1, 0, 1, 1)
        self.InvoicesAccepted1H = QtWidgets.QFrame(self.Network_Stats_Live_Graphs)
        self.InvoicesAccepted1H.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;")
        self.InvoicesAccepted1H.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InvoicesAccepted1H.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InvoicesAccepted1H.setObjectName("InvoicesAccepted1H")
        self.gridLayout_2.addWidget(self.InvoicesAccepted1H, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.Network_Stats_Live_Graphs)
        self.Network_Stats_Historical = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.Network_Stats_Historical.setFont(font)
        self.Network_Stats_Historical.setObjectName("Network_Stats_Historical")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Network_Stats_Historical)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolBox_3 = QtWidgets.QToolBox(self.Network_Stats_Historical)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toolBox_3.setFont(font)
        self.toolBox_3.setObjectName("toolBox_3")
        self.HistoricalStatsProviders_2 = QtWidgets.QWidget()
        self.HistoricalStatsProviders_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.HistoricalStatsProviders_2.setObjectName("HistoricalStatsProviders_2")
        self.toolBox_3.addItem(self.HistoricalStatsProviders_2, "")
        self.HistoricalStatsMemory_2 = QtWidgets.QWidget()
        self.HistoricalStatsMemory_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HistoricalStatsMemory_2.setFont(font)
        self.HistoricalStatsMemory_2.setObjectName("HistoricalStatsMemory_2")
        self.toolBox_3.addItem(self.HistoricalStatsMemory_2, "")
        self.ProviderMedianPricing_2 = QtWidgets.QWidget()
        self.ProviderMedianPricing_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.ProviderMedianPricing_2.setObjectName("ProviderMedianPricing_2")
        self.toolBox_3.addItem(self.ProviderMedianPricing_2, "")
        self.ProvidersComputingSimultaneously_2 = QtWidgets.QWidget()
        self.ProvidersComputingSimultaneously_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.ProvidersComputingSimultaneously_2.setObjectName("ProvidersComputingSimultaneously_2")
        self.toolBox_3.addItem(self.ProvidersComputingSimultaneously_2, "")
        self.horizontalLayout_2.addWidget(self.toolBox_3)
        self.toolBox_4 = QtWidgets.QToolBox(self.Network_Stats_Historical)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toolBox_4.setFont(font)
        self.toolBox_4.setObjectName("toolBox_4")
        self.HistoricalStatsCores_2 = QtWidgets.QWidget()
        self.HistoricalStatsCores_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.HistoricalStatsCores_2.setObjectName("HistoricalStatsCores_2")
        self.toolBox_4.addItem(self.HistoricalStatsCores_2, "")
        self.HistoricalStatsDisk_2 = QtWidgets.QWidget()
        self.HistoricalStatsDisk_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.HistoricalStatsDisk_2.setObjectName("HistoricalStatsDisk_2")
        self.toolBox_4.addItem(self.HistoricalStatsDisk_2, "")
        self.ProviderAveragePricing_2 = QtWidgets.QWidget()
        self.ProviderAveragePricing_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.ProviderAveragePricing_2.setObjectName("ProviderAveragePricing_2")
        self.toolBox_4.addItem(self.ProviderAveragePricing_2, "")
        self.NewestProviders_2 = QtWidgets.QWidget()
        self.NewestProviders_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.NewestProviders_2.setObjectName("NewestProviders_2")
        self.toolBox_4.addItem(self.NewestProviders_2, "")
        self.horizontalLayout_2.addWidget(self.toolBox_4)
        self.stackedWidget.addWidget(self.Network_Stats_Historical)
        self.GLM_Token = QtWidgets.QWidget()
        self.GLM_Token.setObjectName("GLM_Token")
        self.label_7 = QtWidgets.QLabel(self.GLM_Token)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 191, 91))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.GLM_Token)
        self.Wallet_Swap = QtWidgets.QWidget()
        self.Wallet_Swap.setObjectName("Wallet_Swap")
        self.label_5 = QtWidgets.QLabel(self.Wallet_Swap)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 231, 131))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.Wallet_Swap)
        self.Wallet_Send = QtWidgets.QWidget()
        self.Wallet_Send.setObjectName("Wallet_Send")
        self.label_4 = QtWidgets.QLabel(self.Wallet_Send)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 201, 91))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.Wallet_Send)
        self.Wallet_TransactionHistory = QtWidgets.QWidget()
        self.Wallet_TransactionHistory.setObjectName("Wallet_TransactionHistory")
        self.label_6 = QtWidgets.QLabel(self.Wallet_TransactionHistory)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 231, 101))
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.Wallet_TransactionHistory)
        self.Tasks_CreateTask = QtWidgets.QWidget()
        self.Tasks_CreateTask.setObjectName("Tasks_CreateTask")
        self.label_3 = QtWidgets.QLabel(self.Tasks_CreateTask)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 211, 71))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.Tasks_CreateTask)
        self.Tasks_LoadTask = QtWidgets.QWidget()
        self.Tasks_LoadTask.setObjectName("Tasks_LoadTask")
        self.label_2 = QtWidgets.QLabel(self.Tasks_LoadTask)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 291, 101))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.Tasks_LoadTask)
        self.Tasks_Settings = QtWidgets.QWidget()
        self.Tasks_Settings.setObjectName("Tasks_Settings")
        self.label = QtWidgets.QLabel(self.Tasks_Settings)
        self.label.setGeometry(QtCore.QRect(70, 40, 171, 91))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.Tasks_Settings)
        self.verticalLayout.addWidget(self.stackedWidget)
        QaiseoLite.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QaiseoLite)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1085, 22))
        self.menubar.setStyleSheet("background-color: rgb(67, 67, 103);\n"
"border-radius: 30px;\n"
"color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuMarket_Data = QtWidgets.QMenu(self.menubar)
        self.menuMarket_Data.setObjectName("menuMarket_Data")
        self.menuNetwork_Stats = QtWidgets.QMenu(self.menuMarket_Data)
        self.menuNetwork_Stats.setObjectName("menuNetwork_Stats")
        self.menuWallet = QtWidgets.QMenu(self.menubar)
        self.menuWallet.setObjectName("menuWallet")
        self.menuTasks = QtWidgets.QMenu(self.menubar)
        self.menuTasks.setObjectName("menuTasks")
        QaiseoLite.setMenuBar(self.menubar)
        self.actionOverview = QtWidgets.QAction(QaiseoLite)
        self.actionOverview.setObjectName("actionOverview")
        self.actionLive_Graphs = QtWidgets.QAction(QaiseoLite)
        self.actionLive_Graphs.setObjectName("actionLive_Graphs")
        self.actionHistorical_Stats = QtWidgets.QAction(QaiseoLite)
        self.actionHistorical_Stats.setObjectName("actionHistorical_Stats")
        self.actionGLM_Token = QtWidgets.QAction(QaiseoLite)
        self.actionGLM_Token.setObjectName("actionGLM_Token")
        self.actionCreate_Task = QtWidgets.QAction(QaiseoLite)
        self.actionCreate_Task.setObjectName("actionCreate_Task")
        self.actionLoad_Task = QtWidgets.QAction(QaiseoLite)
        self.actionLoad_Task.setObjectName("actionLoad_Task")
        self.actionTask_Settings = QtWidgets.QAction(QaiseoLite)
        self.actionTask_Settings.setObjectName("actionTask_Settings")
        self.actionSwap = QtWidgets.QAction(QaiseoLite)
        self.actionSwap.setObjectName("actionSwap")
        self.actionSend = QtWidgets.QAction(QaiseoLite)
        self.actionSend.setObjectName("actionSend")
        self.actionTransaction_History = QtWidgets.QAction(QaiseoLite)
        self.actionTransaction_History.setObjectName("actionTransaction_History")
        self.menuNetwork_Stats.addAction(self.actionOverview)
        self.menuNetwork_Stats.addSeparator()
        self.menuNetwork_Stats.addAction(self.actionLive_Graphs)
        self.menuNetwork_Stats.addSeparator()
        self.menuNetwork_Stats.addAction(self.actionHistorical_Stats)
        self.menuMarket_Data.addAction(self.menuNetwork_Stats.menuAction())
        self.menuMarket_Data.addAction(self.actionGLM_Token)
        self.menuWallet.addAction(self.actionSwap)
        self.menuWallet.addAction(self.actionSend)
        self.menuWallet.addAction(self.actionTransaction_History)
        self.menuTasks.addAction(self.actionCreate_Task)
        self.menuTasks.addAction(self.actionLoad_Task)
        self.menuTasks.addAction(self.actionTask_Settings)
        self.menubar.addAction(self.menuMarket_Data.menuAction())
        self.menubar.addAction(self.menuWallet.menuAction())
        self.menubar.addAction(self.menuTasks.menuAction())

        self.retranslateUi(QaiseoLite)
        self.stackedWidget.setCurrentIndex(0)
        self.NetworkChartData.setCurrentIndex(0)
        self.NetworkChartData.layout().setSpacing(2)
        self.toolBox_3.setCurrentIndex(3)
        self.toolBox_3.layout().setSpacing(2)
        self.toolBox_4.setCurrentIndex(3)
        self.toolBox_4.layout().setSpacing(2)
        QtCore.QMetaObject.connectSlotsByName(QaiseoLite)

    def retranslateUi(self, QaiseoLite):
        _translate = QtCore.QCoreApplication.translate
        QaiseoLite.setWindowTitle(_translate("QaiseoLite", "QaiseoLite"))
        self.AvgEarnPerTask.setText(_translate("QaiseoLite", "Avg Earnings Per Task"))
        self.AvgEarnPerTask_Amount.setText(_translate("QaiseoLite", "0.000 GLM"))
        self.NetworkEarn6H.setText(_translate("QaiseoLite", "Network Earnings (6h)"))
        self.NetworkEarn6H_Amount.setText(_translate("QaiseoLite", "0.000 GLM"))
        self.NetworkEarn24H.setText(_translate("QaiseoLite", "Network Earnings (24h)"))
        self.NetworkEarn24H_Amount.setText(_translate("QaiseoLite", "0.000 GLM"))
        self.TotalNetworkEarn.setText(_translate("QaiseoLite", "Total Network Earnings"))
        self.TotalNetworkEarn_Amount.setText(_translate("QaiseoLite", "0.000 GLM"))
        self.NetworkChartData.setItemText(self.NetworkChartData.indexOf(self.Providers), _translate("QaiseoLite", "Providers"))
        self.NetworkChartData.setItemText(self.NetworkChartData.indexOf(self.Cores), _translate("QaiseoLite", "Cores"))
        self.NetworkChartData.setItemText(self.NetworkChartData.indexOf(self.Memory), _translate("QaiseoLite", "Memory"))
        self.NetworkChartData.setItemText(self.NetworkChartData.indexOf(self.Disk), _translate("QaiseoLite", "Disk"))
        self.NetworkChartData.setItemText(self.NetworkChartData.indexOf(self.NetworkActivity), _translate("QaiseoLite", "Network Activity"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.HistoricalStatsProviders_2), _translate("QaiseoLite", "Historical Stats: Providers"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.HistoricalStatsMemory_2), _translate("QaiseoLite", "Historical Stats: Memory"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.ProviderMedianPricing_2), _translate("QaiseoLite", "Provider Median Pricing"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.ProvidersComputingSimultaneously_2), _translate("QaiseoLite", "Providers Computing Simultaneously"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.HistoricalStatsCores_2), _translate("QaiseoLite", "Historical Stats: Cores"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.HistoricalStatsDisk_2), _translate("QaiseoLite", "Historical Stats: Disk"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.ProviderAveragePricing_2), _translate("QaiseoLite", "Provider Average Pricing"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.NewestProviders_2), _translate("QaiseoLite", "Newest Providers"))
        self.label_7.setText(_translate("QaiseoLite", "Basic market data of the GLM token"))
        self.label_5.setText(_translate("QaiseoLite", "Where token swap and fiat buying will be"))
        self.label_4.setText(_translate("QaiseoLite", "Basic area to send tokens"))
        self.label_6.setText(_translate("QaiseoLite", "Just gonna list all wallet transaction history"))
        self.label_3.setText(_translate("QaiseoLite", "Task creation area, node based"))
        self.label_2.setText(_translate("QaiseoLite", "Load up tasks, where the premade tasks can be found"))
        self.label.setText(_translate("QaiseoLite", "Tasks Settings like Budget"))
        self.menuMarket_Data.setTitle(_translate("QaiseoLite", "Market Data"))
        self.menuNetwork_Stats.setTitle(_translate("QaiseoLite", "Network Stats"))
        self.menuWallet.setTitle(_translate("QaiseoLite", "Wallets"))
        self.menuTasks.setTitle(_translate("QaiseoLite", "Tasks"))
        self.actionOverview.setText(_translate("QaiseoLite", "Overview"))
        self.actionLive_Graphs.setText(_translate("QaiseoLite", "Live Graphs"))
        self.actionHistorical_Stats.setText(_translate("QaiseoLite", "Historical Stats"))
        self.actionGLM_Token.setText(_translate("QaiseoLite", "GLM Token"))
        self.actionCreate_Task.setText(_translate("QaiseoLite", "Create Task"))
        self.actionLoad_Task.setText(_translate("QaiseoLite", "Load Task"))
        self.actionTask_Settings.setText(_translate("QaiseoLite", "Task Settings"))
        self.actionSwap.setText(_translate("QaiseoLite", "Swap"))
        self.actionSend.setText(_translate("QaiseoLite", "Send"))
        self.actionTransaction_History.setText(_translate("QaiseoLite", "Transaction History"))
from PyQt5.QtChart import QChartView