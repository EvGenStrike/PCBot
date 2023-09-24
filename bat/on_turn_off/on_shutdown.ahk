;==============================
;Set the path to your batch file.
path    := "C:\topsecrets\coding\Projects\PCBot\bat\on_turn_off\batch.bat"
;==============================

; Run script as admin. This will allow your batch file to be ran with admin priv.
if not A_IsAdmin
{
   Run *RunAs "%A_ScriptFullPath%"  ; Requires v1.0.92.01+
   ExitApp
}

; Only allow one instance of the script to run.
#SingleInstance, Force

; If you don't want an icon to show in the tray,
; remove the semicolon from the line below.
;#NoTrayIcon

; When script detects WM_QUERYENDSESSION (a shutdown), run OnShutDown function.
OnMessage(0x11, "OnShutDown")
return

OnShutDown(){
    ; Run the batch file.
    Run, % path
    ExitApp
}