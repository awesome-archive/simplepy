@echo off
setlocal enabledelayedexpansion
:main
echo 1��ת��
echo 2������
echo 3���滻��Ƶ�е���Ƶ����Ƶ·����ǰ����Ƶ·���ں�
echo 4���ϲ���ͬ��ʽ�Ķ����Ƶ����ͬ��ʽ�Ķ����Ƶ
echo 5������
echo 6����ȡ
set /p i=��������Ӧ�����֣�
set /p a="�����ļ�·�������·����|��������"
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
if %i%==4 goto main4
if %i%==5 goto main5
if %i%==6 goto main6
:main1
echo 1����Ƶת��
echo 2����Ƶת��
set /p i=��������Ӧ�����֣�
if %i%==1 goto main11
if %i%==2 goto main11
:main11
set /p b=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" -c:v libx264 -preset ultrafast "%b%"
goto continue
:main2
echo 1����Ƶ����
echo 2����Ƶ����
set /p i=��������Ӧ�����֣�
if %i%==1 goto main21
if %i%==2 goto main22
:main21
set /p b=���뱶����0.5-100�ڵ���������1ʱ���٣�С��1ʱ���٣���
set /p c=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" -filter_complex "[0:v]setpts=1/%b%*PTS[v];[0:a]atempo=%b%[a]" -map "[v]" -map "[a]" "%c%"
goto continue
:main22
set /p b=���뱶����0.5-100�ڵ���������1ʱ���٣�С��1ʱ���٣���
set /p c=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" -filter_complex atempo=%b% "%c%"
goto continue
:main3
set /p b=�������֣�������׺�����ɴ�·������
for /f "tokens=1* delims=|" %%i in ("%a%") do (
ffmpeg -i "%%i" -i "%%j" -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 "%b%")
goto continue
:main4
set /p b=�������֣�������׺�����ɴ�·������
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
echo 1������Ƶȥ����Ƶ
echo 2������Ƶ����������Ƶ
set /p i=��������Ӧ�����֣�
if %i%==1 goto main51
if %i%==2 goto main52
:main51
set /p b=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" -an "%b%"
goto continue
:main52
set /p b=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" -vn "%b%"
goto continue
:main6
echo 1������Ƶ��ȡĳʱ��ͼƬ
echo 2������Ƶ����gif
echo 3����ȡĳ����Ƶ
echo 4������Ƶ��ȡ��Ƶ
echo 5������Ƶ��ȡ��Ƶ
set /p i=��������Ӧ�����֣�
if %i%==1 goto main61
if %i%==2 goto main62
if %i%==3 goto main62
if %i%==4 goto main62
if %i%==5 goto main62
:main61
set /p b=����ʱ�̣���ʽΪʱ:��:�루�����������λ������00:06:06����
set /p c=�������֣�������׺�����ɴ�·������
ffmpeg -i "%a%" -ss %b% -frames 1 "%c%"
goto continue
:main62
set /p b=���뿪ʼʱ�̣���ʽΪʱ:��:�루�����������λ������00:06:06����
set /p c=�������ʱ�̣���ʽΪʱ:��:�루�����������λ������00:06:06����
set /p d=�������֣�������׺�����ɴ�·������
ffmpeg -ss %b% -to %c% -i "%a%" -c copy "%d%"
:continue
set /p i=�Ƿ������y:�������������˳�����
if %i%==y (goto main) else exit