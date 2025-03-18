# -*- coding: utf-8 -*-
__title__ = "Pushbutton"
__author__ = "Seu nome"
__version__ = "Versão 1.0"
__doc__ = """
_____________________________________________________________________
Descrição:

Coloque aqui uma breve descrição sobre a funcionalidade do plugin
_____________________________________________________________________
Passo a passo:

Coloque aqui o passo a passo de utilização do plugin

_____________________________________________________________________
Última atualização:
- [25.03.2025] - VERSÃO 1.0

"""
# ___  __  __  ____    ___   ____   _____  ____  
#|_ _||  \/  ||  _ \  / _ \ |  _ \ |_   _|/ ___| 
# | | | |\/| || |_) || | | || |_) |  | |  \___ \ 
# | | | |  | ||  __/ | |_| ||  _ <   | |   ___) |
#|___||_|  |_||_|     \___/ |_| \_\  |_|  |____/ 
#=================================================

# Importações Python e .NET
import clr
import clr
import os, traceback,math,wpf,re
clr.AddReference("System.Windows.Forms")
clr.AddReference("System")

from System.Collections.Generic import List
from System.Windows.Controls import CheckBox, Button, TextBox, ListBoxItem, TextBlock, ComboBoxItem

from System.Windows.Forms import Application, Form, ComboBox, Label, Button, FormStartPosition,FormBorderStyle
from System.Drawing import Point, Size, Font,ContentAlignment
from System.Windows import Window
from System.Windows.Controls import ComboBoxItem

# Importações Revit API
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# Importações pyRevit
from pyrevit import forms, script

# Suas Funções/ Snippets personalizados
#from Snippets._selection import pick_by_category
#from Snippets._geometry_operations import element_get_geometry 
#from Snippets._transaction import bc_transaction

# Variáveis globais do Revit
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Application
rvt_year = int(app.VersionNumber)
PATH_SCRIPT = os.path.dirname(__file__)


# _____  _   _  _   _   ____  _____  ___   ___   _   _  ____  
#|  ___|| | | || \ | | / ___||_   _||_ _| / _ \ | \ | |/ ___| 
#| |_   | | | ||  \| || |      | |   | | | | | ||  \| |\___ \ 
#|  _|  | |_| || |\  || |___   | |   | | | |_| || |\  | ___) |
#|_|     \___/ |_| \_| \____|  |_|  |___| \___/ |_| \_||____/ 
                                                            












# __  __     _     ___  _   _ 
#|  \/  |   / \   |_ _|| \ | |
#| |\/| |  / _ \   | | |  \| |
#| |  | | / ___ \  | | | |\  |
#|_|  |_|/_/   \_\|___||_| \_|
                             

# Exemplo de uso do Output
output = script.get_output()
output.print_md("# Processando elementos...")

try:
    # Seu código aqui
    x = 1 # Variável de exemplo 

except Exception as e:
    output.print_md("### ERRO: {}".format(str(e)))

output.print_md("# Operação concluída!")




