'''
Created on 3 de jul de 2019

@author: ANDY
'''

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QStatusBar,\
 QFileDialog

from loterias import *
from loteriasWeb import *
from gerarNumeros import gerarMega
from gerarNumeros import gerarLoto

import loteriasLog
import loteriasDesenvolvedor
import PyQt5

class MyForm(QMainWindow):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)       
        
        #self.statusbar = QStatusBar()
        self.ui.actionSair.triggered.connect(qApp.quit)
        
        """ Definindo e configurando os elementos da barra de menu """
        
        ''' aba File '''
        # Definindo evento Abrir
        self.ui.actionAbrir.triggered.connect(self.actAbrir)
        
        # Definindo evento Salvar
        self.ui.actionSalvar.triggered.connect(self.actSalvar)
        
        ''' aba Opção '''
        # Definindo evento Jogar
        self.ui.actionJogar.triggered.connect(self.jogar)
        
        # Definindo evento Web
        self.ui.actionWeb.triggered.connect(self.web)
        
        # Definindo evento Apagar jogos
        self.ui.actionApagar_Jogos.triggered.connect(self.apagar)
        
        ''' aba About '''
        # Definindo evento sobre o dev
        self.ui.actionSobre_o_desenvolvedor.triggered.connect(self.sobredev)
        
        # Definindo evento Log
        self.ui.actionLog_de_Atualiza_es.triggered.connect(self.log)
        
        """ Definindo e configurando os pushs buttons da Mega Sena """
        
        # Definindo push button jogar Mega sena
        self.ui.ButtonJogarMega.clicked.connect(self.jogar)
        
        # Definindo push button apagar jogos Mega sena
        self.ui.ButtonApagarMega.clicked.connect(self.apagar)
        
        # Definindo push button web Mega sena
        self.ui.ButtonWebMega.clicked.connect(self.web)
        
        """ Definindo e configurando os pushs buttons da LotoFacil """
        
        # Definindo push button jogar Lotofácil
        self.ui.ButtonJogarLoto.clicked.connect(self.jogar)
        
        # Definindo push button apagar jogos Lotofácil
        self.ui.ButtonApagarLoto.clicked.connect(self.apagar)
        
        # Definindo push button web Lotofácil
        self.ui.ButtonWebLoto.clicked.connect(self.web)
        
        ###self.ui.tabWidget.currentTabName()
        
        # Definindo e imprimindo a data que consta no sistema
        date = QtCore.QDate.currentDate().toString('ddd dd-MM-yyyy')        
        self.ui.labelDate.setText(date)
        
        # setting the timer
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()
        
        self.show()
        
    def showlcd(self):
        #esta função é chamada para mostrar o relógio
        
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.ui.lcdNumber.display(text)
        
    def actAbrir(self):
        """ Esta função permite abrir um arquivo """
        
        # a variavel self.ui.tabWidget.currentIndex() identifica a tab atual
        # onde 0 é mega , 1 lotofacil e assim por diante
         
        if self.ui.tabWidget.currentIndex() == 0:
            
            fname = QFileDialog.getOpenFileName(self, 'Abrir arquivo', '', 'Text Files (*.mega)')
            if fname[0]:
                
                with open(fname[0], 'r') as f:
                    data = f.read()
                    self.ui.textEditMega.setText(data)
                self.statusBar().showMessage("Arquivo aberto com sucesso!", 5000)
                
            else:
                self.statusBar().showMessage("Nenhum arquivo aberto!", 5000)
        
        elif self.ui.tabWidget.currentIndex() == 1:
            
            fname = QFileDialog.getOpenFileName(self, 'Abrir arquivo', '', 'Text Files (*.loto)')
            if fname[0]:
                
                with open(fname[0], 'r') as f:
                    data = f.read()
                    self.ui.textEditLoto.setText(data)
                self.statusBar().showMessage("Arquivo aberto com sucesso!", 5000)
                
            else:
                self.statusBar().showMessage("Nenhum arquivo aberto!", 5000)
                
    def actSalvar(self):
        
        if self.ui.tabWidget.currentIndex() == 0:
            
            if self.ui.textEditMega.toPlainText() == '':            
                self.statusBar().showMessage("Nenhum jogo Mega sena a ser salvo!", 5000)
            
            else:        
                fileName, _ = QFileDialog.getSaveFileName(self,"Save File", "", "Text File (*.mega)")             
                
                if fileName :
                    with open(fileName, 'w') as f:
                        data = self.ui.textEditMega.toPlainText()
                        f.write(data)
                        self.statusBar().showMessage("Jogo salvo com sucesso!", 5000)
                else:
                    self.statusBar().showMessage("Operação Salvar arquivo cancelada!", 5000)
                    
        elif self.ui.tabWidget.currentIndex() == 1:
            
            if self.ui.textEditLoto.toPlainText() == '':            
                self.statusBar().showMessage("Nenhum jogo LotoFácil a ser salvo!", 5000)
            
            else:        
                fileName, _ = QFileDialog.getSaveFileName(self,"Save File", "", "Text File (*.loto)")             
                
                if fileName :
                    with open(fileName, 'w') as f:
                        data = self.ui.textEditLoto.toPlainText()
                        f.write(data)
                        self.statusBar().showMessage("Jogo salvo com sucesso!", 5000)
                else:
                    self.statusBar().showMessage("Operação Salvar arquivo cancelada!", 5000)
        
    def sobredev(self):
        self.dev = QtWidgets.QDialog()
        self.uiDev = loteriasDesenvolvedor.Ui_Dialog()
        self.uiDev.setupUi(self.dev)
        self.dev.show()
    
    def log(self):
        self.winLog = QtWidgets.QDialog()
        self.uiLog = loteriasLog.Ui_Dialog()
        self.uiLog.setupUi(self.winLog)
        
        #print(gerarMega())
        self.winLog.show()
    
    def jogar(self):
        
        if self.ui.tabWidget.currentIndex() == 0:
            
            aux = 0            
            somaMega = self.ui.spinBoxJogosMega.value() * 3.5
            if self.ui.spinBoxDezenasMega.value() == 7:
                somaMega = self.ui.spinBoxJogosMega.value() * 24.50
            if self.ui.spinBoxDezenasMega.value() == 8:
                somaMega = self.ui.spinBoxJogosMega.value() * 98
            if self.ui.spinBoxDezenasMega.value() == 9:
                somaMega = self.ui.spinBoxJogosMega.value() * 294
            if self.ui.spinBoxDezenasMega.value() == 10:
                somaMega = self.ui.spinBoxJogosMega.value() * 735
            if self.ui.spinBoxDezenasMega.value() == 11:
                somaMega = self.ui.spinBoxJogosMega.value() * 1617
            if self.ui.spinBoxDezenasMega.value() == 12:
                somaMega = self.ui.spinBoxJogosMega.value() * 3234
            if self.ui.spinBoxDezenasMega.value() == 13:
                somaMega = self.ui.spinBoxJogosMega.value() * 6006
            if self.ui.spinBoxDezenasMega.value() == 14:
                somaMega = self.ui.spinBoxJogosMega.value() * 10510.50
            if self.ui.spinBoxDezenasMega.value() == 15:
                somaMega = self.ui.spinBoxJogosMega.value() * 17517.50
            
                
                    
            dezenasMega = self.ui.spinBoxDezenasMega.value()
            jogosMega = self.ui.spinBoxJogosMega.value()
            restrictMega = [self.ui.ListaMega1, self.ui.ListaMega2, self.ui.ListaMega3,\
                        self.ui.ListaMega4, self.ui.ListaMega5, self.ui.ListaMega6,\
                        self.ui.ListaMega7, self.ui.ListaMega8]
            resultadoMega = []
            
            # inicialização da variavel que vai contar o tempo
            tempoMega = QtCore.QTime()
            tempoMega.start()
            
            # gerando numeros aleatorios
            while jogosMega > 0:
                
                while dezenasMega > aux:
                    
                    aleat = gerarMega(restrictMega)
                    
                    while aleat in resultadoMega:
                        aleat = gerarMega(restrictMega)                                        
                        
                    resultadoMega.append(aleat)
                    
                    aux += 1
                    
                # ordenando o resultado de forma crescente
                resultadoMega.sort()
                
                self.ui.textEditMega.append(' '.join(str("{:02d}".format(num)) for num in resultadoMega))
                
                aux = 0
                
                resultadoMega.clear()                
                jogosMega-=1
            tempoMega = tempoMega.elapsed() * 0.001
            
            self.statusBar().showMessage("jogo efetuado em : %0.3f s" % tempoMega, 5000)
            self.ui.textEditMega.append('\nValor do(s) Jogo(s): ' +str(somaMega)+' R$\nFeito ' +self.ui.labelDate.text()+' às '\
                                        +QtCore.QTime.currentTime().toString('hh:mm:ss')+ '\n')
            
            for vMega in restrictMega:
                if vMega.isChecked():
                    vMega.setAutoExclusive(False)
                    vMega.setChecked(False)
                    vMega.setAutoExclusive(True)                    
        
        elif self.ui.tabWidget.currentIndex() == 1:
            
            aux1 = 0
            
            somaLoto = self.ui.spinBoxJogosLoto.value() * 2
            if self.ui.spinBoxDezenasLoto.value() == 16:
                somaLoto = self.ui.spinBoxJogosLoto.value() * 32
            if self.ui.spinBoxDezenasLoto.value() == 17:
                somaLoto = self.ui.spinBoxJogosLoto.value() * 272
            if self.ui.spinBoxDezenasLoto.value() == 18:
                somaLoto = self.ui.spinBoxJogosLoto.value() * 1632
                
            dezenasLoto = self.ui.spinBoxDezenasLoto.value()
            jogosLoto = self.ui.spinBoxJogosLoto.value()
            restrictLoto = [self.ui.ListaLoto1, self.ui.ListaLoto2, self.ui.ListaLoto3,\
                            self.ui.ListaLoto4, self.ui.ListaMega5]
            resultadoLoto = []
            
            # inicialização da variavel que vai contar o tempo
            tempoLoto = QtCore.QTime()
            tempoLoto.start()
            
            # gerando numeros aleatorios
            while jogosLoto > 0:
                
                while dezenasLoto > aux1:
                    
                    aleat = gerarLoto(restrictLoto)
                    
                    while aleat in resultadoLoto:
                        aleat = gerarLoto(restrictLoto)
                        
                    resultadoLoto.append(aleat)
                    
                    aux1 += 1
                    
                # ordenando o resultado de forma crescente
                resultadoLoto.sort()
                
                self.ui.textEditLoto.append(' '.join(str("{:02d}".format(num)) for num in resultadoLoto))
                aux1 = 0
                resultadoLoto.clear()
                
                jogosLoto-=1
            tempoLoto = tempoLoto.elapsed() * 0.001
            
            self.statusBar().showMessage("jogo efetuado em : %0.3f s" % tempoLoto, 5000)
            self.ui.textEditLoto.append('\nValor do(s) Jogo(s): ' +str(somaLoto)+' R$\nFeito ' +self.ui.labelDate.text()+\
                                 ' às '+QtCore.QTime.currentTime().toString('hh:mm:ss')+ '\n')
            
            for vLoto in restrictLoto:
                if vLoto.isChecked():
                    vLoto.setAutoExclusive(False)
                    vLoto.setChecked(False)
                    vLoto.setAutoExclusive(True)
    
    def apagar(self):
        """ Esta função o jogo efetuado"""
        
        if self.ui.tabWidget.currentIndex() == 0:
            
            if self.ui.textEditMega.toPlainText() == "":
                self.statusBar().showMessage("Nenhum jogo da Mega Sena ser apagado!", 5000)
            else:
                self.ui.textEditMega.clear()
                self.statusBar().showMessage("Últimos jogos da Mega Sena apagados!", 5000)
            
        elif self.ui.tabWidget.currentIndex() == 1:
            
            if self.ui.textEditLoto.toPlainText() == "":
                self.statusBar().showMessage("Nenhum jogo da LotoFácil ser apagado!", 5000)
            else:
                self.ui.textEditLoto.clear()
                self.statusBar().showMessage("Últimos jogos da LotoFácil apagados!", 5000)
    
    def web(self):
        """ Esta função abre uma nova janela com um navegador dentro
        lembrando que é necessário instanciar sempre todas as janela
        não importa se for do tipo Dialog, Widget ou MainWindow """
        
        if self.ui.tabWidget.currentIndex() == 0:
            self.webMega = QtWidgets.QWidget()
            self.uiWebMega = Ui_Form()
            self.uiWebMega.setupUi(self.webMega)
            
            self.webMega.setWindowTitle("Resultado MEGA SENA")
            
            # Configurando os butões do navegador
            self.uiWebMega.pushButtonBack.clicked.connect(self.uiWebMega.widget.back)
            self.uiWebMega.pushButtonReload.clicked.connect(self.uiWebMega.widget.reload)
            self.uiWebMega.pushButtonForward.clicked.connect(self.uiWebMega.widget.forward)            
            
            # Configurando o link
            self.uiWebMega.widget.load(QUrl('http://www.loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/'))
            self.statusBar().showMessage("Consulta Web Mega Sena processada com sucesso!", 5000)
            
            self.webMega.show()            
            
        elif self.ui.tabWidget.currentIndex() == 1:
            self.webLoto = QtWidgets.QWidget()
            self.uiWebLoto = Ui_Form()
            self.uiWebLoto.setupUi(self.webLoto)
            
            self.webLoto.setWindowTitle("Resultado LOTOFACIL")
            
            # Configurando os butões do navegador
            self.uiWebLoto.pushButtonBack.clicked.connect(self.uiWebLoto.widget.back)
            self.uiWebLoto.pushButtonReload.clicked.connect(self.uiWebLoto.widget.reload)
            self.uiWebLoto.pushButtonForward.clicked.connect(self.uiWebLoto.widget.forward)            
            
            # Configurando o link
            self.uiWebLoto.widget.load(QUrl('http://www.loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/'))
            self.statusBar().showMessage("Consulta Web LotoFácil processada com sucesso!", 5000)
            
            self.webLoto.show()
            
            
        