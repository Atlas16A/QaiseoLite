from PyQt5.QtChart import QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtCore import QDateTime, Qt, QPointF, QTimeZone
from PyQt5.QtGui import QColor, QPen, QBrush, QFont

class LiveChart:
    def __init__(self):
        self.series = QLineSeries()
        self.chart = QChart()
        self.chart.addSeries(self.series)
        
        self.time_axis = QDateTimeAxis()
        self.time_axis.setTickCount(10)
        self.time_axis.setFormat("hh:mm ap")
        self.time_axis.setTitleText("Time")
        self.chart.addAxis(self.time_axis, Qt.AlignBottom)
        self.series.attachAxis(self.time_axis)
        
        self.providers_axis = QValueAxis()
        self.providers_axis.setTickCount(10)
        self.providers_axis.setLabelFormat("%d")
        self.chart.addAxis(self.providers_axis, Qt.AlignLeft)
        self.series.attachAxis(self.providers_axis)

        self.linecolor = QColor('#0000FF')
        self.pen = QPen(self.linecolor)
        self.pen.setWidth(5)
        self.series.setPen(self.pen)
        self.chart.setBackgroundBrush(QBrush(QColor("#2A2B42")))
        self.chart.setTitleBrush(QBrush(Qt.white))
        self.chart.legend().setBrush(QBrush(Qt.white))
        self.time_axis.setTitleBrush(QBrush(Qt.white))
        self.providers_axis.setTitleBrush(QBrush(Qt.white))
        self.time_axis.setLabelsColor(Qt.white)
        self.providers_axis.setLabelsColor(Qt.white)
        self.chart.setTitleFont(QFont("Gill Sans MT", 11))
        self.time_axis.setTitleFont(QFont("Gill Sans MT", 11))
        self.providers_axis.setTitleFont(QFont("Gill Sans MT", 11))
        self.time_axis.setLabelsFont(QFont("Gill Sans MT", 11))
        self.providers_axis.setLabelsFont(QFont("Gill Sans MT", 11))
        self.chart.legend().setVisible(False)
        
    def update_chart(self, timestamps, providers):
        self.series.clear()
        for i in range(len(timestamps)):
            point = QPointF(QDateTime.fromSecsSinceEpoch(timestamps[i], QTimeZone.systemTimeZone()).toMSecsSinceEpoch(), float(providers[i]))
            self.series.append(point)

        min_time = min(timestamps)
        max_time = max(timestamps)
        self.time_axis.setRange(QDateTime.fromSecsSinceEpoch(min_time, QTimeZone.systemTimeZone()), QDateTime.fromSecsSinceEpoch(max_time))
        
        min_provider = float(min(providers))
        max_provider = float(max(providers))
        self.providers_axis.setRange(min_provider, max_provider)