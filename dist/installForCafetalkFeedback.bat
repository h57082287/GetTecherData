@echo off

echo %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe
:: ���ȦW��
set TaskName=getDataforCafetalkFeedback

:: ��J�`���g��
set /p cycle=�п�J�`���g��(�䴩�ﶵ��'��'�A'��'�A'�P'�A'��'):

:: �}�l�ɶ�
set /p time=�п�J�_�l�ɶ�(HH:mm:ss):

:: �P�_�`���g�� 
if %cycle%==�� SCHTASKS /Create /SC MINUTE /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 
if %cycle%==�� SCHTASKS /Create /SC HOURLY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 
if %cycle%==�� SCHTASKS /Create /SC DAILY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT  
if %cycle%==�P SCHTASKS /Create /SC WEEKLY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 
if %cycle%==�� SCHTASKS /Create /SC MONTHLY /TN %TaskName% /TR %~dp0getTecherData/getDataforCafetalkFeedback/getDataforCafetalkFeedback.exe /ST %time% /IT 

:: ��J���N��
pause