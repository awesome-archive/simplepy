@echo off
:main
echo 1������pip
echo 2���鿴�Ѱ�װ������б�
echo 3���������������
echo 4���鿴�����������
echo 5�����߰�װ�����
echo 6���ӱ��ذ�װ�����
echo 7�����������б����߰�װ
echo 8��ж�������
echo 9�����������
echo 10�������Ѱ�װ������б�
set /p i=��������Ӧ�����֣�
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
if %i%==4 goto main4
if %i%==5 goto main5
if %i%==6 goto main6
if %i%==7 goto main7
if %i%==8 goto main8
if %i%==9 goto main9
if %i%==10 goto main10
:main1
python -m pip install --upgrade pip
goto continue
:main2
pip list
goto continue
:main3
set /p a=�������������
pip search %a%
goto continue
:main4
pip list --outdated
goto continue
:main5
set /p a=�������������
pip install %a%
goto continue
:main6
set /p a=���뱾�������·����
pip install "%a%"
goto continue
:main7
set /p a=�����������б�·����
pip install -r "%a%"
goto continue
:main8
set /p a=�������������
pip uninstall %a%
goto continue
:main9
set /p a=�������������
pip install --upgrade %a%
goto continue
:main10
pip freeze >requirements.txt
:continue
set /p i=�Ƿ������n:�˳�����������������
if %i%==n (exit) else (
cls
goto main)