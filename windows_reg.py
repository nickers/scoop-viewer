import winreg as wreg

def runAsIE11():
  print ("hello windows")
  print(__file__)

  current_file = __file__
  if ".pyc" in current_file:
    value = "browser.exe"
  else:
    value = "python.exe"
  key = wreg.CreateKey(wreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_BROWSER_EMULATION")
  wreg.SetValueEx(key, value, 0, wreg.REG_DWORD, 11001)