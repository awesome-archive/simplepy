New-Item "$($profile | split-path)\Modules\AudioDeviceCmdlets" -Type directory -ForceCopy-Item "AudioDeviceCmdlets.dll" "$($profile | split-path)\Modules\AudioDeviceCmdlets\AudioDeviceCmdlets.dll"
Set-Location "$($profile | Split-Path)\Modules\AudioDeviceCmdlets"
Get-ChildItem | Unblock-File
Import-Module AudioDeviceCmdlets
Set-AudioDevice -RecordingMuteToggle