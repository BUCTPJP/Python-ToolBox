# 计算BMI

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
 
import Ui_自制工具箱

class MyMainForm(QMainWindow,Ui_自制工具箱.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.calculate.clicked.connect(self.display.show)
    def show(self):
        height = self.inputheight.text()
        weight = self.inputweight.text()
        BMI = weight / pow(height, 2)
        self.display.show.setText(BMI)
        if BMI < 18.5:
            INT, DOM = '偏瘦', '偏瘦'
        elif 18.5 <= BMI < 24:
            INT, DOM = '正常', '正常'
        elif 24 <= BMI < 25:
            INT, DOM = '正常', '偏胖'
        elif 25 <= BMI < 28:
            INT, DOM = '偏胖', '偏胖'
        elif 28 <= BMI < 30:
            INT, DOM = '偏胖', '肥胖'
        else:
            INT, DOM = '肥胖', '肥胖'
        self.display.setText("BMI的指标为：国际'{0}'，国内'{1}'".format(INT, DOM))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_自制工具箱.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())






height, weight = eval(input('请输入身高（米）和体重（公斤）【逗号隔开】:'))
BMI = weight / pow(height, 2)
print('BMI的数值为:{:.2f}'.format(BMI))
if BMI < 18.5:
    INT, DOM = '偏瘦', '偏瘦'
elif 18.5 <= BMI < 24:
    INT, DOM = '正常', '正常'
elif 24 <= BMI < 25:
    INT, DOM = '正常', '偏胖'
elif 25 <= BMI < 28:
    INT, DOM = '偏胖', '偏胖'
elif 28 <= BMI < 30:
    INT, DOM = '偏胖', '肥胖'
else:
    INT, DOM = '肥胖', '肥胖'
print("BMI的指标为：国际'{0}'，国内'{1}'".format(INT, DOM))
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_自制工具箱.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



