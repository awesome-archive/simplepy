@echo off
:main
echo 1�����ö�ʱ�ػ�
echo 2�����ö�ʱ����
echo 3��ȡ����ʱ�ػ�����
set /p i=ѡ�����ֺ�س���
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
:main1
set /p i=���볬ʱʱ�䣺
shutdown /s /f /t %i%
goto continue
:main2
set /p i=���볬ʱʱ�䣺
shutdown /r /f /t %i%
goto continue
:main3
shutdown /a
:continue
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (
cls
goto main) else exit