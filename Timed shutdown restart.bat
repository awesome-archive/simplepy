@echo off
:main
echo 1、设置定时关机
echo 2、设置定时重启
echo 3、取消定时关机重启
set /p i=选择数字后回车：
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
:main1
set /p i=输入超时时间：
shutdown /s /f /t %i%
goto continue
:main2
set /p i=输入超时时间：
shutdown /r /f /t %i%
goto continue
:main3
shutdown /a
:continue
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (
cls
goto main) else exit