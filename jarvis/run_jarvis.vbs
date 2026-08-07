Set WshShell = CreateObject("WScript.Shell")
' உங்க பைதான் ஃபைலை பேக்ரவுண்டில் சத்தமில்லாமல் ரன் செய்யும் மேஜிக் லைன் சார்
WshShell.Run "python assistant.py", 0, False