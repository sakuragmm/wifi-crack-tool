@echo off
echo ">>>>> build start <<<<<"
:: 使用Conda激活虚拟环境 修改为本地 conda 安装目录
call "D:\program\anaconda3\condabin\conda.bat" activate wifi

:: 打包Python脚本为exe
pyinstaller -F -w -i .\images\wificrack.ico --add-data "images/wificrack.ico;images" --distpath .\ .\wifi_crack_tool.py

:: 删除.spec文件
if exist wifi_crack_tool.spec (
    del wifi_crack_tool.spec
)

:: 删除build文件夹
if exist build (
    rmdir /S /Q build
)

echo ">>>>> build success! <<<<<"
pause
