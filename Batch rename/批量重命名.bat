@echo off
setlocal enabledelayedexpansion
:main
set /p a=����Ҫ��������Ŀ¼�����ļ����ڵ�Ŀ¼��·����
echo 1��������Ŀ¼�¾�����ͬ�ؼ��ʵ�Ŀ¼
echo 2��������Ŀ¼�¾�����ͬ�ؼ��ʵ��ļ�
echo 3��������Ŀ¼�µ�����Ŀ¼
echo 4��������Ŀ¼�µ������ļ�
echo 5��������Ŀ¼�µ�����Ŀ¼���ļ�
echo 6���滻Ŀ¼��
echo 7���滻�ļ���
echo 8���滻Ŀ¼���ļ���
set /p i=��������Ӧ�����֣�
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
if %i%==4 goto main4
if %i%==5 goto main5
if %i%==6 goto main6
if %i%==7 goto main7
if %i%==8 goto main8
:main1
set /p b=����ؼ��ʣ�ֻ��������������Щ�ؼ��ʵ�Ŀ¼����
set /p c=������Ҫ��Ŀ¼����
set x=0
for /d %%y in ("%a%\*%b%*") do (
set /a x+=1
ren "%%y" "%c%!x!")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main2
set /p b=����ؼ��ʣ�ֻ��������������Щ�ؼ��ʵ��ļ�����������ͬ�ĺ�׺������
set /p c=������Ҫ���ļ������޺�׺������
set /p d=������Ҫ�ĺ�׺�����س��޺�׺������
set x=0
for %%y in ("%a%\*%b%*") do (
set /a x+=1
ren "%%y" "%c%!x!.%d%")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main3
set /p b=������Ҫ��Ŀ¼����
set x=0
for /d %%y in ("%a%\*") do (
set /a x+=1
ren "%%y" "%b%!x!")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main4
set /p b=������Ҫ���ļ������޺�׺������
set /p c=������Ҫ�ĺ�׺�����س��޺�׺������
set x=0
for %%y in ("%a%\*") do (
set /a x+=1
ren "%%y" "%b%!x!.%c%")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main5
set /p b=������Ҫ�����֣�
set x=0
for /f "delims=" %%y in ('dir /b "%a%"') do (
set /a x+=1
ren "%a%\%%y" "%b%!x!")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main6
set /p b=����Ŀ¼����Ҫ�滻���ַ���
set /p c=�����滻����ַ���
for /f "delims=" %%y in ('dir /ad/b "%a%"') do (
set d=%%y
set e=!d:%b%=%c%!
ren "%a%\!d!" "!e!")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main7
set /p b=�����ļ�����Ҫ�滻���ַ���
set /p c=�����滻����ַ���
for /f "delims=" %%y in ('dir /aa/b "%a%"') do (
set d=%%y
set e=!d:%b%=%c%!
ren "%a%\!d!" "!e!")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit
:main8
set /p b=������Ҫ�滻���ַ���
set /p c=�����滻����ַ���
for /f "delims=" %%y in ('dir /b "%a%"') do (
set d=%%y
set e=!d:%b%=%c%!
ren "%a%\!d!" "!e!")
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit