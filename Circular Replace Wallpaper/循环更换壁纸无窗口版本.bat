@echo off
%1 mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
Powershell.exe -executionpolicy remotesigned -File ѭ��������ֽ.ps1
pause