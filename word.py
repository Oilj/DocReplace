# -*- coding: cp936 -*-
import win32com ,os
from win32com.client import Dispatch, constants
w = win32com.client.Dispatch('Word.Application')
# w = win32com.client.DispatchEx('Word.Application')

w.Visible = 0
w.DisplayAlerts = 0

current_path = os.getcwd()
files = os.listdir(current_path+"\\..")
print "��ѡ����Ҫ�滻�ĵ��ĸ�ʽ��[1]:.doc    [2]: .docx"
doctypeinput=input()
if doctypeinput == 1:
    doctype='.doc'
elif doctypeinput == 2:
    doctype='.docx'
else :
    doctype='.docfhhfd'
OldStr=raw_input("���滻�Ĵʣ�")
NewStr=raw_input("�� "+OldStr+" �滻Ϊ��")
for filename in files:
    if filename.endswith(doctype):
    # ���µ��ļ�
        
        filenamein=current_path+"\\..\\"+filename
        filenameout=current_path+"\\..\\new\\"+filename
        if not os.path.isdir(current_path+"\\..\\new"):
            os.mkdir(current_path+"\\..\\new")
        print filename+"�滻�ɹ���"
        doc = w.Documents.Open( FileName = filenamein )

        
        
        # ���������滻
        w.Selection.Find.ClearFormatting()
        w.Selection.Find.Replacement.ClearFormatting()
        w.Selection.Find.Execute(OldStr, False, False, False, False, False, True, 1,
        True, NewStr, 2)
        # ҳü�����滻
        w.ActiveDocument.Sections[0].Headers[0].Range.Find.ClearFormatting()
        w.ActiveDocument.Sections[0].Headers[0].Range.Find.Replacement.ClearFormatting()
        w.ActiveDocument.Sections[0].Headers[0].Range.Find.Execute(OldStr, False,
        False, False, False, False, True, 1, False, NewStr, 2)


        # �ر�
        doc.SaveAs(filenameout)
        doc.Close()
#w.Documents.Close()
w.Quit()
