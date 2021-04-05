@echo off
:main
echo 1、升级pip
echo 2、查看已安装软件包列表
echo 3、在线搜索软件包
echo 4、查看可升级软件包
echo 5、在线安装软件包
echo 6、从本地安装软件包
echo 7、从依赖包列表在线安装
echo 8、卸载软件包
echo 9、升级软件包
echo 10、导出已安装软件包列表
set /p i=输入分类对应的数字：
if %i%==1 goto main1
if %i%==2 goto main2
if %i%==3 goto main3
if %i%==4 goto main4
if %i%==5 goto main5
if %i%==6 goto main6
if %i%==7 goto main7
if %i%==8 goto main8
if %i%==9 goto main9
if %i%==10 goto main10
:main1
python -m pip install --upgrade pip
goto continue
:main2
pip list
goto continue
:main3
set /p a=输入软件包名：
pip search %a%
goto continue
:main4
pip list --outdated
goto continue
:main5
set /p a=输入软件包名：
pip install %a%
goto continue
:main6
set /p a=输入本地软件包路径：
pip install "%a%"
goto continue
:main7
set /p a=输入依赖包列表路径：
pip install -r "%a%"
goto continue
:main8
set /p a=输入软件包名：
pip uninstall %a%
goto continue
:main9
set /p a=输入软件包名：
pip install --upgrade %a%
goto continue
:main10
pip freeze >requirements.txt
:continue
set /p i=是否继续（n:退出，其它：继续）：
if %i%==n (exit) else (
cls
goto main)