@echo off
:: ��J��������
set /p deleteNum=�п�J�����������Ƚs��(1.Verbling  2.Cafetalk  3.Cafetalk����):
:: ��ܲ���
if %deleteNum%==1 schtasks /Delete /TN getDataforVerbling
if %deleteNum%==2 schtasks /Delete /TN getDataforCafetalk
if %deleteNum%==3 schtasks /Delete /TN getDataforCafetalkFeedback

:: ���U���N�䵲��
pause