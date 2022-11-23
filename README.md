# A-Security-Device
Project Description:
_____________________
The program simulates a Security System for an Office or a Home.
The System gets Locked after entering the lock passcode: 561761, and it gets unlocked after entering the unlock code: 561764.
If the user entered a wrong lock passcode the system won’t lock and if the user entered a wrong unlock passcode the system won’t unlock.
If the user entered a correct unlock code, the system would give the message “Unlock”.
If the user entered a correct lock code, the system would give the message “Lock”.
The System does not show the characters that the user entered, instead it shows “*” symbol indicating that the user entered a character.
If the user entered non-valid characters (any characters other than numbers from 0 to 9), the system would simply ignore them and gives the message “Wrong Character”.

Technologies Used:
____________________
Python
IDE: Visual Studio
Operationg System: Windows

How to run the Project:
________________________
1-Clone the repository from GitHub.
2-Navigate to the Security Device folder.
3-Open the dist folder.
4-Open the SecurityDevice folder (.........\A-Security-Device\dist\SecurityDevice).
5-Double Click the SecurityDevice.exe to run the application.

How to use the Application:
___________________________
1-After opening the application, the initial state of the security device will be locked
2-Enter the first unlock passcode digit "5" then press enter (Note: when you enter the digit the device will read it but it won't show anything on the screen until you press enter)
3-Enter the second unlock passcode digit "6" then press enter (Note: when you enter the digit the device will read it but it won't show anything on the screen until you press enter)
4-Enter the third unlock passcode digit "1" then press enter (Note: when you enter the digit the device will read it but it won't show anything on the screen until you press enter)
5-Enter the fourth unlock passcode digit "7" then press enter (Note: when you enter the digit the device will read it but it won't show anything on the screen until you press enter)
6-Enter the fifth unlock passcode digit "6" then press enter (Note: when you enter the digit the device will read it but it won't show anything on the screen until you press enter)
7-Enter the sixth unlock passcode digit "1" then press enter (Note: when you enter the digit the device will read it but it won't show anything on the screen until you press enter)
8-Repeat the previous steps to lock the device

Notes:
______
-If you enter an invalid characters other than digits from 0-9, the device will give you "Wrong Character" Message and will simply ignore it
-If you enter a wrong passcode for lock or unlock the device will give you "wrong passcode" message and will reset to enter a new 6 digits code
-Every time the user presses enter the device will consider it as a single digit input. the user must enter every single digit individually then press enter
-If the device is locked and you entered the lock code again it will still be unlocked
-Please Read the Security Device Memo.pdf for more instructions and details 

