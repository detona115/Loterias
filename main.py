'''
Created on 25 de jul de 2019

@author: ANDY
'''
import sys
from MyFormM import *

if __name__ == '__main__':
    "método main que inicia o app"
    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())