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
echo 1���鿴Windows Defender״̬
echo 2���л�Windows Defender״̬
set /p i=ѡ�����ֺ�س���
if %i%==1 goto main1
if %i%==2 goto main2
:main1
powershell "if((Get-MpPreference).DisableRealtimeMonitoring){write-host Windows Defenderʵʱ�����ѹر�}else{write-host Windows Defenderʵʱ�����ѿ���}"
goto continue
:main2
powershell "if((Get-MpPreference).DisableRealtimeMonitoring){Set-MpPreference -DisableRealtimeMonitoring 0;write-host Windows Defenderʵʱ�����ѿ���}else{Set-MpPreference -DisableRealtimeMonitoring 1;write-host Windows Defenderʵʱ�����ѹر�}"
:continue
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (
cls
goto main) else exit