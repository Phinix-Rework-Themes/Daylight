# Daylight · 晴昼

**请先通过 Steam 更新 Phinix Rework 主模组至 0.10.3 或更新版本，再安装主题。**

**Update the main Phinix Rework mod to 0.10.3 or newer through Steam before installing this theme.**

同一份纯数据主题包支持 RimWorld 1.6 和 1.7。可通过游戏内商店或本地导入安装，然后在主题设置中选择配色；安装不会自动改变当前主题。

One data-only ZIP supports both RimWorld 1.6 and 1.7. Install through the in-game store or local import, then select the palette in theme settings. Installation does not automatically apply it.

[主模组 / Main mod](https://steamcommunity.com/sharedfiles/filedetails/?id=3735269431)

## Packaging

Source XML and manifest configuration are under `theme/`. Use the trusted ManagedPackageTool from Phinix Rework:

```sh
python3 tools/package.py --tool /absolute/path/to/ManagedPackageTool.dll --output /fresh/output/directory
```

Release digests are recorded in SHA256SUMS. No game, Harmony, Host or plugin DLLs are distributed.
