function Set-Wallpaper
{
    param(
        [Parameter(Mandatory=$true)]
        $Path,
  
        [ValidateSet('Center', 'Stretch')]
        $Style = 'Stretch'
    )
  
    Add-Type @"
using System;
using System.Runtime.InteropServices;
using Microsoft.Win32;
namespace Wallpaper
{
public enum Style : int
{
Center, Stretch
}
public class Setter {
public const int SetDesktopWallpaper = 20;
public const int UpdateIniFile = 0x01;
public const int SendWinIniChange = 0x02;
[DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
private static extern int SystemParametersInfo (int uAction, int uParam, string lpvParam, int fuWinIni);
public static void SetWallpaper ( string path, Wallpaper.Style style ) {
SystemParametersInfo( SetDesktopWallpaper, 0, path, UpdateIniFile | SendWinIniChange );
RegistryKey key = Registry.CurrentUser.OpenSubKey("Control Panel\\Desktop", true);
switch( style )
{
case Style.Stretch :
key.SetValue(@"WallpaperStyle", "10") ;
key.SetValue(@"TileWallpaper", "0") ;
break;
case Style.Center :
key.SetValue(@"WallpaperStyle", "1") ;
key.SetValue(@"TileWallpaper", "0") ;
break;
}
key.Close();
}
}
}
"@
  
    [Wallpaper.Setter]::SetWallpaper( $Path, $Style )
}
#第33行WallpaperStyle：10填充，6适应，2拉伸，平铺0，跨区22
#第58行sleep后面的数字表示每张图片的间隔时间，单位秒
while ($true)
{
foreach($picture in dir *.jpg,*.png,*.bmp)
{
clear
write-host 当前壁纸：$picture
Set-Wallpaper -Path $picture
sleep 1
}
}