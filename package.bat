@echo off
chcp 65001
echo 正在激活Conda虚拟环境...

:: 使用Conda激活虚拟环境
call "D:\program\anaconda3\condabin\conda.bat" activate wifi

:: 打包Python脚本为exe
echo 正在启动PyInstaller打包进程...
pyinstaller -F -w -i .\images\wificrack.ico --add-data "images/wificrack.ico;images" --distpath .\ .\wifi_crack_tool.py

:: 删除.spec文件
if exist wifi_crack_tool.spec (
    del wifi_crack_tool.spec
    echo .spec文件已删除.
)

:: 删除build文件夹
if exist build (
    rmdir /S /Q build
    echo build文件夹已删除.
)

echo 打包过程已完成! ===> wifi_crack_tool.exe
pause
