@echo off
echo 1���鿴wifi���루��ȫ������Ĺؼ����ݾ������룩
echo 2��ɾ���ѱ����wifi����
set /p i=�������ֺ�س���
if %i%==1 netsh wlan show profile * key=clear
if %i%==2 netsh wlan delete profile *
pause