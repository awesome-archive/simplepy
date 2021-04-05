@echo off
setlocal enabledelayedexpansion
:main
set /p a=输入要重命名的目录或者文件所在的目录的路径：
echo 1、重命名目录下具有相同关键词的目录
echo 2、重命名目录下具有相同关键词的文件
echo 3、重命名目录下的所有目录
echo 4、重命名目录下的所有文件
echo 5、重命名目录下的所有目录和文件
echo 6、替换目录名
echo 7、替换文件名
echo 8、替换目录和文件名
set /p i=输入分类对应的数字：
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
if %i%==4 goto main4
if %i%==5 goto main5
if %i%==6 goto main6
if %i%==7 goto main7
if %i%==8 goto main8
:main1
set /p b=输入关键词（只会重命名具有这些关键词的目录）：
set /p c=输入你要的目录名：
set x=0
for /d %%y in ("%a%\*%b%*") do (
set /a x+=1
ren "%%y" "%c%!x!")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main2
set /p b=输入关键词（只会重命名具有这些关键词的文件，可以是相同的后缀名）：
set /p c=输入你要的文件名（无后缀名）：
set /p d=输入你要的后缀名（回车无后缀名）：
set x=0
for %%y in ("%a%\*%b%*") do (
set /a x+=1
ren "%%y" "%c%!x!.%d%")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main3
set /p b=输入你要的目录名：
set x=0
for /d %%y in ("%a%\*") do (
set /a x+=1
ren "%%y" "%b%!x!")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main4
set /p b=输入你要的文件名（无后缀名）：
set /p c=输入你要的后缀名（回车无后缀名）：
set x=0
for %%y in ("%a%\*") do (
set /a x+=1
ren "%%y" "%b%!x!.%c%")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main5
set /p b=输入你要的名字：
set x=0
for /f "delims=" %%y in ('dir /b "%a%"') do (
set /a x+=1
ren "%a%\%%y" "%b%!x!")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main6
set /p b=输入目录中你要替换的字符：
set /p c=输入替换后的字符：
for /f "delims=" %%y in ('dir /ad/b "%a%"') do (
set d=%%y
set e=!d:%b%=%c%!
ren "%a%\!d!" "!e!")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main7
set /p b=输入文件中你要替换的字符：
set /p c=输入替换后的字符：
for /f "delims=" %%y in ('dir /aa/b "%a%"') do (
set d=%%y
set e=!d:%b%=%c%!
ren "%a%\!d!" "!e!")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit
:main8
set /p b=输入你要替换的字符：
set /p c=输入替换后的字符：
for /f "delims=" %%y in ('dir /b "%a%"') do (
set d=%%y
set e=!d:%b%=%c%!
ren "%a%\!d!" "!e!")
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit