# ebusd configurations with recoVAIR behind VR32

This repository mirrors the compiled CSV files from [eBUS/ebus.github.io](https://github.com/eBUS/ebus.github.io). A GitHub Actions workflow refreshes them daily and on demand. After every refresh, it copies `de/vaillant/08.recov.csv` to `de/vaillant/38.v32.recov.csv` and does the same for `en`. It also adds the new filename to each `vaillant/index.json`, which ebusd needs when reading configurations over HTTP.

The published German configuration path for ebusd is:

```text
https://dwapps.github.io/ebusd-config/de/
```

In the Home Assistant ebusd add-on, set these as separate additional ebusd options:

```text
--configpath=https://dwapps.github.io/ebusd-config/de/
--scanconfig
--latency=100000
```

The VR32 device is scanned as `V32` at slave address `38`. The filename `38.v32.recov.csv` matches that scan result while retaining `recov` as the circuit name. The added CSV is an address mapping of the official recoVAIR configuration, not a guarantee that every register is available through the VR32. Verify the loaded file with `ebusctl info` after restarting ebusd.

To refresh immediately, run the **Sync eBUS configurations** workflow manually from the Actions tab.
