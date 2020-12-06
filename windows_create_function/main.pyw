from gui import Ui_Dialog_mainWindow
from PyQt5 import QtCore, QtWidgets, QtGui

class main_ui(Ui_Dialog_mainWindow):
    
    def acceptNuttonPressed(self):
        try:
            repoName = self.lineEdit_projectName.text()
            if repoName != '' and ' ' not in repoName:
                flags = self.defineFlags()
                command = f"env\scripts\python windows_create_function\createRepo.py {repoName}{flags}"
                import os
                file_folder = os.path.abspath(__file__).replace('\\', '/').rstrip('main.pyw')
                file_folder = file_folder.replace('windows_create_function/', '')
                print(file_folder)
                os.chdir(file_folder)
                os.system(command)
                Dialog_mainWindow.accept()
        except Exception as e:
            print('[ERROR]:', e)

    def defineFlags(self) -> str:
        local = self.defineLocalRepoFlag()
        remote = self.defineRemoteRepoFlag()
        env = self.defineEnvCreationFlag()
        flags = ''
        flags += (f' {self.local}' if not local else '')
        flags += (f' {self.remote}' if not remote else '')
        flags += (f' {self.env}' if env else '')
        return flags
        
    def defineLocalRepoFlag(self):
        flag = self.checkBox_localRepo.isChecked()
        self.local = ('-no_local' if not flag else None)
        return flag
        
    def defineRemoteRepoFlag(self):
        flag = self.checkBox_remoteRepo.isChecked()
        self.remote = ('-no_remote' if not flag else None)
        return flag

    def defineEnvCreationFlag(self):
        flag = self.checkBox_virtualEnv.isChecked()
        self.env = ('-pyenv' if flag else None)
        return flag


    def setup(self):
        # Check Boxes
        self.checkBox_localRepo.setChecked(True)
        self.checkBox_remoteRepo.setChecked(True)
        self.checkBox_virtualEnv.setChecked(False)

        # Buttons Actions
        self.buttonBox_startProject.accepted.connect(self.acceptNuttonPressed)
        self.buttonBox_startProject.rejected.connect(Dialog_mainWindow.reject)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_mainWindow = QtWidgets.QDialog()
    ui = main_ui()
    ui.setupUi(Dialog_mainWindow)
    ui.setup()
    Dialog_mainWindow.show()
    sys.exit(app.exec_())