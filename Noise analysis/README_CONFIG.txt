Configuration (12/02/2024)

Hardware
- GWINSTEK GFG-8216A function generator
- SIGLENT SPD3303X-E power supply with +/- 5V range
- SIGLENT SDS 1104X-E scope to view waveforms in the meantime
(not connected during data collection)
- CANBERRA analog shaper with NIM bin Model 2020
- CAEN V2740B digitizer with only CH1 connected

Soft Settings
- Frequency of sq wave = 115.7 Hz
- Amplitude of sq wave in file name (measured only with scope and fn gen w/ 50 Ohm termination)
- Fine gain on shaper set to lowest (within the same shaping time), else set to make peak height ~970 mV
- Coarse gain on shaper set to lowest (within the same shaping time), else set to make peak height ~970 mV
- Shaping time in file name
- Auto + self trigger with WaveDump2 (with mask over only CH1)
- WD2 Threshold 101.59 mV
- Record length = 200 us
- Pre-trigger = 16 us


