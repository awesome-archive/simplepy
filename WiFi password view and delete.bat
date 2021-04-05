@echo off
echo 1、查看wifi密码（安全设置里的关键内容就是密码）
echo 2、删除已保存的wifi密码
set /p i=输入数字后回车：
if %i%==1 netsh wlan show profile * key=clear
if %i%==2 netsh wlan delete profile *
pause