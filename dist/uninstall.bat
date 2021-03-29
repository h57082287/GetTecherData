@echo off
:: 輸入移除項目
set /p deleteNum=請輸入欲移除的任務編號(1.Verbling  2.Cafetalk  3.Cafetalk評論):
:: 選擇移除
if %deleteNum%==1 schtasks /Delete /TN getDataforVerbling
if %deleteNum%==2 schtasks /Delete /TN getDataforCafetalk
if %deleteNum%==3 schtasks /Delete /TN getDataforCafetalkFeedback

:: 按下任意鍵結束
pause