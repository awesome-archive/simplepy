@echo off
setlocal enabledelayedexpansion
:main
echo 1、转换
echo 2、变速
echo 3、替换视频中的音频（视频路径在前，音频路径在后）
echo 4、合并相同格式的多个视频或相同格式的多个音频
echo 5、分离
echo 6、截取
set /p i=输入分类对应的数字：
set /p a="输入文件路径（多个路径用|隔开）："
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
if %i%==4 goto main4
if %i%==5 goto main5
if %i%==6 goto main6
:main1
echo 1、视频转换
echo 2、音频转换
set /p i=输入分类对应的数字：
if %i%==1 goto main11
if %i%==2 goto main11
:main11
set /p b=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" -c:v libx264 -preset ultrafast "%b%"
goto continue
:main2
echo 1、视频变速
echo 2、音频变速
set /p i=输入分类对应的数字：
if %i%==1 goto main21
if %i%==2 goto main22
:main21
set /p b=输入倍数（0.5-100内的数，大于1时加速，小于1时减速）：
set /p c=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" -filter_complex "[0:v]setpts=1/%b%*PTS[v];[0:a]atempo=%b%[a]" -map "[v]" -map "[a]" "%c%"
goto continue
:main22
set /p b=输入倍数（0.5-100内的数，大于1时加速，小于1时减速）：
set /p c=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" -filter_complex atempo=%b% "%c%"
goto continue
:main3
set /p b=输入名字（包含后缀名，可带路径）：
for /f "tokens=1* delims=|" %%i in ("%a%") do (
ffmpeg -i "%%i" -i "%%j" -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 "%b%")
goto continue
:main4
set /p b=输入名字（包含后缀名，可带路径）：
set n=0
call :loop "%a%"
:loop
for /f "tokens=1* delims=|" %%i in ("%~1") do (
set /a n+=1
copy "%%i" !n!%%~xi
echo file '!n!%%~xi'>>mergelist.txt
if not %%j=="" call :loop "%%j")
ffmpeg -f concat -i mergelist.txt -c copy "%b%"
for /f "delims=' tokens=2" %%i in (mergelist.txt) do (
del /f/s/q %%i)
del /f/s/q mergelist.txt
goto continue
:main5
echo 1、从视频去除音频
echo 2、从视频分离完整音频
set /p i=输入分类对应的数字：
if %i%==1 goto main51
if %i%==2 goto main52
:main51
set /p b=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" -an "%b%"
goto continue
:main52
set /p b=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" -vn "%b%"
goto continue
:main6
echo 1、从视频截取某时刻图片
echo 2、从视频制作gif
echo 3、截取某段视频
echo 4、从视频截取音频
echo 5、从音频截取音频
set /p i=输入分类对应的数字：
if %i%==1 goto main61
if %i%==2 goto main62
if %i%==3 goto main62
if %i%==4 goto main62
if %i%==5 goto main62
:main61
set /p b=输入时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：
set /p c=输入名字（包含后缀名，可带路径）：
ffmpeg -i "%a%" -ss %b% -frames 1 "%c%"
goto continue
:main62
set /p b=输入开始时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：
set /p c=输入结束时刻，格式为时:分:秒（整数，最多两位数，如00:06:06）：
set /p d=输入名字（包含后缀名，可带路径）：
ffmpeg -ss %b% -to %c% -i "%a%" -c copy "%d%"
:continue
set /p i=是否继续（y:继续，其它：退出）：
if %i%==y (goto main) else exit