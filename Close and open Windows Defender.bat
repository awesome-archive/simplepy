@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
goto UACPrompt
) else ( goto gotAdmin )
:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B
:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
pushd "%CD%"
CD /D "%~dp0"
:main
echo 1、查看Windows Defender状态
echo 2、切换Windows Defender状态
set /p i=选择数字后回车：
if %i%==1 goto main1
if %i%==2 goto main2
:main1
powershell "if((Get-MpPreference).DisableRealtimeMonitoring){write-host Windows Defender实时保护已关闭}else{write-host Windows Defender实时保护已开启}"
goto continue
:main2
powershell "if((Get-MpPreference).DisableRealtimeMonitoring){Set-MpPreference -DisableRealtimeMonitoring 0;write-host Windows Defender实时保护已开启}else{Set-MpPreference -DisableRealtimeMonitoring 1;write-host Windows Defender实时保护已关闭}"
:continue
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (
cls
goto main) else exit