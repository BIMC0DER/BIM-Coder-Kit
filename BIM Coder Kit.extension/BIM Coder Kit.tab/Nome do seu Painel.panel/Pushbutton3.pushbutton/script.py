# -*- coding: utf-8 -*-
"""Descrição do comando."""
__title__ = 'Pushbutton3'
__doc__ = 'Descrição detalhada do que este comando faz'

# Importações da API do Revit
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

# Importações do pyRevit
from pyrevit import revit, DB, UI
from pyrevit import forms, script

# Obtém o documento atual e a interface
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# Função principal
def main():
    # Seu código aqui
    forms.alert('Comando acionado com sucesso!', title=__title__)

# Execução principal
if __name__ == '__main__':
    main()
