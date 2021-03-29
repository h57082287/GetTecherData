@echo off

echo %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe
:: 任務名稱
set TaskName=getDataforCafetalkFeedback

:: 輸入循環週期
set /p cycle=請輸入循環週期(支援選項為'時'，'日'，'周'，'月'):

:: 開始時間
set /p time=請輸入起始時間(HH:mm:ss):

:: 判斷循環週期 
if %cycle%==分 SCHTASKS /Create /SC MINUTE /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 
if %cycle%==時 SCHTASKS /Create /SC HOURLY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 
if %cycle%==日 SCHTASKS /Create /SC DAILY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT  
if %cycle%==周 SCHTASKS /Create /SC WEEKLY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 
if %cycle%==月 SCHTASKS /Create /SC MONTHLY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 

:: 輸入任意鍵
pause