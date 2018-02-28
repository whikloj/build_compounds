# build_compounds.py

## Description

Takes a directory of image files and a directory of similarly named mods records (with extension .mods) and
generates a directory of large_image and compounds (if more than 2 images).

The output directory has 2 sub-directories generated (`compounds` and `large_images`) and all further objects are
generated inside those directories depending on whether they have more than 1 image in the sequence.

The script only processes the images available. So extra MODS records will not be used if there is not an complementary
image.

## Usage
```commandline
usage: build_compounds.py [-h] --images IMAGE_DIRECTORY --metadata
                          MODS_DIRECTORY --output OUTPUT_DIR [-w]

Copy multiple files from separate image and metadate directories in to a flat
structure for batch compounding.

optional arguments:
  -h, --help            show this help message and exit
  --images IMAGE_DIRECTORY
                        Directory of images to copy
  --metadata MODS_DIRECTORY
                        Directory of metadata files, with same basename as
                        images
  --output OUTPUT_DIR   Directory to build compounds under
  -w, --overwrite       Overwrite existing files.
```

## Expected Naming Conventions

### Images

Images have file names ending in one or more digits. These ending digits indicate sequence.

Example: Chapel1.tiff Chapel2.tiff Chapel3.tiff

### Metadata

MODS records are expected to have the same name as one of the images and the extension
`.mods`

Example: Chapel1.mods relates to Chapel1.tiff, Canyon33.mods relates to Canyon33.tiff, etc

## Full example

With a directory `/home/images` with contents
```commandline
> ls
TA-DB1.tif	TA-DB3.tif	TA-JD5.tif	TA-RS1.tif	TA-VK12.tif	TA-VK22.tif	TA-VK32.tif	TA-VT1.tif	TA-VT2.tif
TA-DB10.tif	TA-DB4.tif	TA-LM1.tif	TA-RS2.tif	TA-VK13.tif	TA-VK23.tif	TA-VK33.tif	TA-VT10.tif	TA-VT20.tif
TA-DB11.tif	TA-DB5.tif	TA-LM10.tif	TA-RS3.tif	TA-VK14.tif	TA-VK24.tif	TA-VK34.tif	TA-VT11.tif	TA-VT3.tif
TA-DB12.tif	TA-DB6.tif	TA-LM2.tif	TA-RS4.tif	TA-VK15.tif	TA-VK25.tif	TA-VK35.tif	TA-VT12.tif	TA-VT4.tif
TA-DB13.tif	TA-DB7.tif	TA-LM3.tif	TA-RS5.tif	TA-VK16.tif	TA-VK26.tif	TA-VK36.tif	TA-VT13.tif	TA-VT5.tif
TA-DB14.tif	TA-DB8.tif	TA-LM4.tif	TA-RS6.tif	TA-VK17.tif	TA-VK27.tif	TA-VK4.tif	TA-VT14.tif	TA-VT6.tif
TA-DB15.tif	TA-DB9.tif	TA-LM5.tif	TA-RS7.tif	TA-VK18.tif	TA-VK28.tif	TA-VK5.tif	TA-VT15.tif	TA-VT7.tif
TA-DB16.tif	TA-JD1.tif	TA-LM6.tif	TA-TI1.tif	TA-VK19.tif	TA-VK29.tif	TA-VK6.tif	TA-VT16.tif	TA-VT8.tif
TA-DB17.tif	TA-JD2.tif	TA-LM7.tif	TA-VK1.tif	TA-VK2.tif	TA-VK3.tif	TA-VK7.tif	TA-VT17.tif	TA-VT9.tif
TA-DB18.tif	TA-JD3.tif	TA-LM8.tif	TA-VK10.tif	TA-VK20.tif	TA-VK30.tif	TA-VK8.tif	TA-VT18.tif
TA-DB2.tif	TA-JD4.tif	TA-LM9.tif	TA-VK11.tif	TA-VK21.tif	TA-VK31.tif	TA-VK9.tif	TA-VT19.tif
```

and a directory `/home/metadata` with contents
```commandline
> ls *.mods
PA-AAR1.mods	PA-DWE1.mods	PA-RGS19.mods	RH-AVNBN2.mods	RH-TTD2.mods	TA-BG9.mods	TA-RT5.mods	TA-VKK16.mods	TA-VKK63.mods
PA-AAR10.mods	PA-DWE2.mods	PA-RGS2.mods	RH-AVNBN3.mods	RH-TTD3.mods	TA-DB1.mods	TA-RT6.mods	TA-VKK17.mods	TA-VKK64.mods
PA-AAR2.mods	PA-DWE3.mods	PA-RGS20.mods	RH-AVNBN4.mods	RH-TTD4.mods	TA-DB10.mods	TA-RT7.mods	TA-VKK18.mods	TA-VKK65.mods
PA-AAR3.mods	PA-DWE4.mods	PA-RGS3.mods	RH-AVNBN5.mods	RH-TTD5.mods	TA-DB11.mods	TA-RT8.mods	TA-VKK19.mods	TA-VKK66.mods
PA-AAR4.mods	PA-DWE5.mods	PA-RGS4.mods	RH-AVNBN6.mods	RH-TTD6.mods	TA-DB12.mods	TA-RT9.mods	TA-VKK2.mods	TA-VKK67.mods
PA-AAR5.mods	PA-DWE6.mods	PA-RGS5.mods	RH-AVNBN7.mods	RH-TTD7.mods	TA-DB13.mods	TA-TI1.mods	TA-VKK20.mods	TA-VKK68.mods
PA-AAR6.mods	PA-EBTHC1.mods	PA-RGS6.mods	RH-AVNBN8.mods	RH-TTD8.mods	TA-DB14.mods	TA-TI2.mods	TA-VKK21.mods	TA-VKK69.mods
PA-AAR7.mods	PA-EBTHC2.mods	PA-RGS7.mods	RH-AVNBN9.mods	RH-TTD9.mods	TA-DB15.mods	TA-TI3.mods	TA-VKK22.mods	TA-VKK7.mods
PA-AAR8.mods	PA-EBTHC3.mods	PA-RGS8.mods	RH-DRWU1.mods	RH-TTP1.mods	TA-DB16.mods	TA-TI4.mods	TA-VKK23.mods	TA-VKK70.mods
PA-AAR9.mods	PA-EBTHC4.mods	PA-RGS9.mods	RH-DRWU2.mods	RH-TTP2.mods	TA-DB17.mods	TA-VK1.mods	TA-VKK24.mods	TA-VKK71.mods
PA-AVU1.mods	PA-EBTHC5.mods	PA-RHRRP1.mods	RH-EVBSF1.mods	RH-TTQT1.mods	TA-DB18.mods	TA-VK10.mods	TA-VKK25.mods	TA-VKK72.mods
PA-AVU10.mods	PA-EBTHC6.mods	PA-RHRRP10.mods	RH-EVBSF10.mods	RH-TTQT2.mods	TA-DB2.mods	TA-VK11.mods	TA-VKK26.mods	TA-VKK73.mods
PA-AVU11.mods	PA-EBTHC7.mods	PA-RHRRP11.mods	RH-EVBSF11.mods	RH-TTRBF1.mods	TA-DB3.mods	TA-VK12.mods	TA-VKK27.mods	TA-VKK74.mods
PA-AVU12.mods	PA-EBTHC8.mods	PA-RHRRP12.mods	RH-EVBSF12.mods	RH-TTRBF2.mods	TA-DB4.mods	TA-VK13.mods	TA-VKK28.mods	TA-VKK75.mods
PA-AVU13.mods	PA-EM1.mods	PA-RHRRP13.mods	RH-EVBSF13.mods	RH-TTRBF3.mods	TA-DB5.mods	TA-VK14.mods	TA-VKK29.mods	TA-VKK76.mods
PA-AVU14.mods	PA-EM2.mods	PA-RHRRP14.mods	RH-EVBSF2.mods	RH-TTRD1.mods	TA-DB6.mods	TA-VK15.mods	TA-VKK3.mods	TA-VKK77.mods
PA-AVU15.mods	PA-EM3.mods	PA-RHRRP15.mods	RH-EVBSF3.mods	RH-TTRD2.mods	TA-DB7.mods	TA-VK16.mods	TA-VKK30.mods	TA-VKK78.mods
PA-AVU16.mods	PA-EM4.mods	PA-RHRRP16.mods	RH-EVBSF4.mods	RH-TTS1.mods	TA-DB8.mods	TA-VK17.mods	TA-VKK31.mods	TA-VKK79.mods
PA-AVU17.mods	PA-EM5.mods	PA-RHRRP17.mods	RH-EVBSF5.mods	RH-TTS2.mods	TA-DB9.mods	TA-VK18.mods	TA-VKK32.mods	TA-VKK8.mods
PA-AVU2.mods	PA-EM6.mods	PA-RHRRP18.mods	RH-EVBSF6.mods	RH-TTS3.mods	TA-JD1.mods	TA-VK19.mods	TA-VKK33.mods	TA-VKK80.mods
PA-AVU3.mods	PA-EM7.mods	PA-RHRRP19.mods	RH-EVBSF7.mods	RH-TTS4.mods	TA-JD2.mods	TA-VK2.mods	TA-VKK34.mods	TA-VKK81.mods
PA-AVU4.mods	PA-LMG1.mods	PA-RHRRP2.mods	RH-EVBSF8.mods	RH-TTSA1.mods	TA-JD3.mods	TA-VK20.mods	TA-VKK35.mods	TA-VKK82.mods
PA-AVU5.mods	PA-LMG10.mods	PA-RHRRP20.mods	RH-EVBSF9.mods	RH-TTSF1.mods	TA-JD4.mods	TA-VK21.mods	TA-VKK36.mods	TA-VKK83.mods
PA-AVU6.mods	PA-LMG11.mods	PA-RHRRP21.mods	RH-IESM1.mods	RH-TTSF2.mods	TA-JD5.mods	TA-VK22.mods	TA-VKK37.mods	TA-VKK9.mods
PA-AVU7.mods	PA-LMG12.mods	PA-RHRRP22.mods	RH-IESM2.mods	RH-TTSP1.mods	TA-LM1.mods	TA-VK23.mods	TA-VKK38.mods	TA-VT1.mods
PA-AVU8.mods	PA-LMG13.mods	PA-RHRRP3.mods	RH-IESM3.mods	RH-TTSP2.mods	TA-LM10.mods	TA-VK24.mods	TA-VKK39.mods	TA-VT10.mods
PA-AVU9.mods	PA-LMG14.mods	PA-RHRRP4.mods	RH-IESM4.mods	RH-TTSP3.mods	TA-LM2.mods	TA-VK25.mods	TA-VKK4.mods	TA-VT11.mods
PA-BBGP1.mods	PA-LMG15.mods	PA-RHRRP5.mods	RH-IESM5.mods	RH-TTTO1.mods	TA-LM3.mods	TA-VK26.mods	TA-VKK40.mods	TA-VT12.mods
PA-BBGP10.mods	PA-LMG2.mods	PA-RHRRP6.mods	RH-IESM6.mods	RH-TTTO2.mods	TA-LM4.mods	TA-VK27.mods	TA-VKK41.mods	TA-VT13.mods
PA-BBGP11.mods	PA-LMG3.mods	PA-RHRRP7.mods	RH-IESM7.mods	RH-TTTT1.mods	TA-LM5.mods	TA-VK28.mods	TA-VKK42.mods	TA-VT14.mods
PA-BBGP12.mods	PA-LMG4.mods	PA-RHRRP8.mods	RH-JSOAM1.mods	RH-TTTT2.mods	TA-LM6.mods	TA-VK29.mods	TA-VKK43.mods	TA-VT15.mods
PA-BBGP13.mods	PA-LMG5.mods	PA-RHRRP9.mods	RH-JSOAM2.mods	RH-TTYT1.mods	TA-LM7.mods	TA-VK3.mods	TA-VKK44.mods	TA-VT16.mods
PA-BBGP14.mods	PA-LMG6.mods	PA-RJC1.mods	RH-JSOAM3.mods	RH-TTYT2.mods	TA-LM8.mods	TA-VK30.mods	TA-VKK45.mods	TA-VT17.mods
PA-BBGP2.mods	PA-LMG7.mods	PA-RJC2.mods	RH-JSOAM4.mods	RH-TTYT3.mods	TA-LM9.mods	TA-VK31.mods	TA-VKK46.mods	TA-VT18.mods
PA-BBGP3.mods	PA-LMG8.mods	PA-RJC3.mods	RH-JSOAM5.mods	RH-WLCZ1.mods	TA-RS1.mods	TA-VK32.mods	TA-VKK47.mods	TA-VT19.mods
PA-BBGP4.mods	PA-LMG9.mods	PA-RJC4.mods	RH-JSOAM6.mods	RL-DW1.mods	TA-RS2.mods	TA-VK33.mods	TA-VKK48.mods	TA-VT2.mods
PA-BBGP5.mods	PA-MJLR1.mods	PA-RJC5.mods	RH-LMBBBD1.mods	SJ-AS1.mods	TA-RS3.mods	TA-VK34.mods	TA-VKK49.mods	TA-VT20.mods
PA-BBGP6.mods	PA-MJLR2.mods	PA-RJC6.mods	RH-LMBBBD2.mods	SJ-MO1.mods	TA-RS4.mods	TA-VK35.mods	TA-VKK5.mods	TA-VT3.mods
PA-BBGP7.mods	PA-MJLR3.mods	PA-SCF1.mods	RH-LMBBBD3.mods	SJ-TTGTWL1.mods	TA-RS5.mods	TA-VK36.mods	TA-VKK50.mods	TA-VT4.mods
PA-BBGP8.mods	PA-MJLR4.mods	PA-WS1.mods	RH-LMBBBD4.mods	SJ-TTUT1.mods	TA-RS6.mods	TA-VK4.mods	TA-VKK51.mods	TA-VT5.mods
PA-BBGP9.mods	PA-MJLR5.mods	PA-WS2.mods	RH-LMBBBD5.mods	TA-BG1.mods	TA-RS7.mods	TA-VK5.mods	TA-VKK52.mods	TA-VT6.mods
PA-BU1.mods	PA-MJLR6.mods	PA-WS3.mods	RH-LMBBBD6.mods	TA-BG10.mods	TA-RT1.mods	TA-VK6.mods	TA-VKK53.mods	TA-VT7.mods
PA-BU10.mods	PA-RGS1.mods	PA-WS4.mods	RH-LMBBBD7.mods	TA-BG11.mods	TA-RT10.mods	TA-VK7.mods	TA-VKK54.mods	TA-VT8.mods
PA-BU11.mods	PA-RGS10.mods	PA-WS5.mods	RH-PMWW1.mods	TA-BG12.mods	TA-RT11.mods	TA-VK8.mods	TA-VKK55.mods	TA-VT9.mods
PA-BU2.mods	PA-RGS11.mods	PA-WS6.mods	RH-RBCSF1.mods	TA-BG13.mods	TA-RT12.mods	TA-VK9.mods	TA-VKK56.mods
PA-BU3.mods	PA-RGS12.mods	PA-WS7.mods	RH-RBCSF2.mods	TA-BG2.mods	TA-RT13.mods	TA-VKK1.mods	TA-VKK57.mods
PA-BU4.mods	PA-RGS13.mods	RH-AVNBN1.mods	RH-RBCSF3.mods	TA-BG3.mods	TA-RT14.mods	TA-VKK10.mods	TA-VKK58.mods
PA-BU5.mods	PA-RGS14.mods	RH-AVNBN10.mods	RH-TTCF1.mods	TA-BG4.mods	TA-RT15.mods	TA-VKK11.mods	TA-VKK59.mods
PA-BU6.mods	PA-RGS15.mods	RH-AVNBN11.mods	RH-TTCF2.mods	TA-BG5.mods	TA-RT16.mods	TA-VKK12.mods	TA-VKK6.mods
PA-BU7.mods	PA-RGS16.mods	RH-AVNBN12.mods	RH-TTD1.mods	TA-BG6.mods	TA-RT2.mods	TA-VKK13.mods	TA-VKK60.mods
PA-BU8.mods	PA-RGS17.mods	RH-AVNBN13.mods	RH-TTD10.mods	TA-BG7.mods	TA-RT3.mods	TA-VKK14.mods	TA-VKK61.mods
PA-BU9.mods	PA-RGS18.mods	RH-AVNBN14.mods	RH-TTD11.mods	TA-BG8.mods	TA-RT4.mods	TA-VKK15.mods	TA-VKK62.mods
```

And a directory `/home/output` for the final compounds.

```commandline
> ./build_compounds.py --images /home/images --metadata /home/metadata --output /home/output
Copied /home/images/TA-JD4.tif -> /home/output/compounds/ta_jd/4/OBJ.tif
Copied /home/metadata/TA-JD4.mods -> /home/output/compounds/ta_jd/4/MODS.xml
Copied /home/images/TA-JD5.tif -> /home/output/compounds/ta_jd/5/OBJ.tif
Copied /home/metadata/TA-JD5.mods -> /home/output/compounds/ta_jd/5/MODS.xml
Copied /home/images/TA-JD2.tif -> /home/output/compounds/ta_jd/2/OBJ.tif
Copied /home/metadata/TA-JD2.mods -> /home/output/compounds/ta_jd/2/MODS.xml
Copied /home/images/TA-VT9.tif -> /home/output/compounds/ta_vt/9/OBJ.tif
Copied /home/metadata/TA-VT9.mods -> /home/output/compounds/ta_vt/9/MODS.xml
Copied /home/images/TA-JD3.tif -> /home/output/compounds/ta_jd/3/OBJ.tif
Copied /home/metadata/TA-JD3.mods -> /home/output/compounds/ta_jd/3/MODS.xml
Copied /home/images/TA-VT8.tif -> /home/output/compounds/ta_vt/8/OBJ.tif
Copied /home/metadata/TA-VT8.mods -> /home/output/compounds/ta_vt/8/MODS.xml
Copied /home/images/TA-JD1.tif -> /home/output/compounds/ta_jd/1/OBJ.tif
Copied /home/metadata/TA-JD1.mods -> /home/output/compounds/ta_jd/1/MODS.xml
Copied /home/metadata/TA-JD1.mods -> /home/output/compounds/ta_jd/MODS.xml
Copied /home/images/TA-VK33.tif -> /home/output/compounds/ta_vk/33/OBJ.tif
Copied /home/metadata/TA-VK33.mods -> /home/output/compounds/ta_vk/33/MODS.xml
Copied /home/images/TA-VK27.tif -> /home/output/compounds/ta_vk/27/OBJ.tif
Copied /home/metadata/TA-VK27.mods -> /home/output/compounds/ta_vk/27/MODS.xml
Copied /home/images/TA-DB12.tif -> /home/output/compounds/ta_db/12/OBJ.tif
Copied /home/metadata/TA-DB12.mods -> /home/output/compounds/ta_db/12/MODS.xml
Copied /home/images/TA-DB8.tif -> /home/output/compounds/ta_db/8/OBJ.tif
Copied /home/metadata/TA-DB8.mods -> /home/output/compounds/ta_db/8/MODS.xml
Copied /home/images/TA-DB9.tif -> /home/output/compounds/ta_db/9/OBJ.tif
Copied /home/metadata/TA-DB9.mods -> /home/output/compounds/ta_db/9/MODS.xml
Copied /home/images/TA-DB13.tif -> /home/output/compounds/ta_db/13/OBJ.tif
Copied /home/metadata/TA-DB13.mods -> /home/output/compounds/ta_db/13/MODS.xml
Copied /home/images/TA-VK26.tif -> /home/output/compounds/ta_vk/26/OBJ.tif
Copied /home/metadata/TA-VK26.mods -> /home/output/compounds/ta_vk/26/MODS.xml
Copied /home/images/TA-VK32.tif -> /home/output/compounds/ta_vk/32/OBJ.tif
Copied /home/metadata/TA-VK32.mods -> /home/output/compounds/ta_vk/32/MODS.xml
Copied /home/images/TA-VK24.tif -> /home/output/compounds/ta_vk/24/OBJ.tif
Copied /home/metadata/TA-VK24.mods -> /home/output/compounds/ta_vk/24/MODS.xml
Copied /home/images/TA-VK30.tif -> /home/output/compounds/ta_vk/30/OBJ.tif
Copied /home/metadata/TA-VK30.mods -> /home/output/compounds/ta_vk/30/MODS.xml
Copied /home/images/TA-VK18.tif -> /home/output/compounds/ta_vk/18/OBJ.tif
Copied /home/metadata/TA-VK18.mods -> /home/output/compounds/ta_vk/18/MODS.xml
Copied /home/images/TA-DB11.tif -> /home/output/compounds/ta_db/11/OBJ.tif
Copied /home/metadata/TA-DB11.mods -> /home/output/compounds/ta_db/11/MODS.xml
Copied /home/images/TA-VT20.tif -> /home/output/compounds/ta_vt/20/OBJ.tif
Copied /home/metadata/TA-VT20.mods -> /home/output/compounds/ta_vt/20/MODS.xml
Copied /home/images/TA-DB10.tif -> /home/output/compounds/ta_db/10/OBJ.tif
Copied /home/metadata/TA-DB10.mods -> /home/output/compounds/ta_db/10/MODS.xml
Copied /home/images/TA-VK19.tif -> /home/output/compounds/ta_vk/19/OBJ.tif
Copied /home/metadata/TA-VK19.mods -> /home/output/compounds/ta_vk/19/MODS.xml
Copied /home/images/TA-VK31.tif -> /home/output/compounds/ta_vk/31/OBJ.tif
Copied /home/metadata/TA-VK31.mods -> /home/output/compounds/ta_vk/31/MODS.xml
Copied /home/images/TA-VK25.tif -> /home/output/compounds/ta_vk/25/OBJ.tif
Copied /home/metadata/TA-VK25.mods -> /home/output/compounds/ta_vk/25/MODS.xml
Copied /home/images/TA-VK21.tif -> /home/output/compounds/ta_vk/21/OBJ.tif
Copied /home/metadata/TA-VK21.mods -> /home/output/compounds/ta_vk/21/MODS.xml
Copied /home/images/TA-VK35.tif -> /home/output/compounds/ta_vk/35/OBJ.tif
Copied /home/metadata/TA-VK35.mods -> /home/output/compounds/ta_vk/35/MODS.xml
Copied /home/images/TA-VK8.tif -> /home/output/compounds/ta_vk/8/OBJ.tif
Copied /home/metadata/TA-VK8.mods -> /home/output/compounds/ta_vk/8/MODS.xml
Copied /home/images/TA-DB14.tif -> /home/output/compounds/ta_db/14/OBJ.tif
Copied /home/metadata/TA-DB14.mods -> /home/output/compounds/ta_db/14/MODS.xml
Copied /home/images/TA-LM8.tif -> /home/output/compounds/ta_lm/8/OBJ.tif
Copied /home/metadata/TA-LM8.mods -> /home/output/compounds/ta_lm/8/MODS.xml
Copied /home/images/TA-VT19.tif -> /home/output/compounds/ta_vt/19/OBJ.tif
Copied /home/metadata/TA-VT19.mods -> /home/output/compounds/ta_vt/19/MODS.xml
Copied /home/images/TA-VT18.tif -> /home/output/compounds/ta_vt/18/OBJ.tif
Copied /home/metadata/TA-VT18.mods -> /home/output/compounds/ta_vt/18/MODS.xml
Copied /home/images/TA-LM9.tif -> /home/output/compounds/ta_lm/9/OBJ.tif
Copied /home/metadata/TA-LM9.mods -> /home/output/compounds/ta_lm/9/MODS.xml
Copied /home/images/TA-DB15.tif -> /home/output/compounds/ta_db/15/OBJ.tif
Copied /home/metadata/TA-DB15.mods -> /home/output/compounds/ta_db/15/MODS.xml
Copied /home/images/TA-VK9.tif -> /home/output/compounds/ta_vk/9/OBJ.tif
Copied /home/metadata/TA-VK9.mods -> /home/output/compounds/ta_vk/9/MODS.xml
Copied /home/images/TA-VK34.tif -> /home/output/compounds/ta_vk/34/OBJ.tif
Copied /home/metadata/TA-VK34.mods -> /home/output/compounds/ta_vk/34/MODS.xml
Copied /home/images/TA-VK20.tif -> /home/output/compounds/ta_vk/20/OBJ.tif
Copied /home/metadata/TA-VK20.mods -> /home/output/compounds/ta_vk/20/MODS.xml
Copied /home/images/TA-VK36.tif -> /home/output/compounds/ta_vk/36/OBJ.tif
Copied /home/metadata/TA-VK36.mods -> /home/output/compounds/ta_vk/36/MODS.xml
Copied /home/images/TA-VK22.tif -> /home/output/compounds/ta_vk/22/OBJ.tif
Copied /home/metadata/TA-VK22.mods -> /home/output/compounds/ta_vk/22/MODS.xml
Copied /home/images/TA-DB17.tif -> /home/output/compounds/ta_db/17/OBJ.tif
Copied /home/metadata/TA-DB17.mods -> /home/output/compounds/ta_db/17/MODS.xml
Copied /home/images/TA-TI1.tif -> /home/output/large_images/ta_ti/OBJ.tif
Copied /home/metadata/TA-TI1.mods -> /home/output/large_images/ta_ti/MODS.xml
Copied /home/images/TA-DB16.tif -> /home/output/compounds/ta_db/16/OBJ.tif
Copied /home/metadata/TA-DB16.mods -> /home/output/compounds/ta_db/16/MODS.xml
Copied /home/images/TA-VK23.tif -> /home/output/compounds/ta_vk/23/OBJ.tif
Copied /home/metadata/TA-VK23.mods -> /home/output/compounds/ta_vk/23/MODS.xml
Copied /home/images/TA-VK12.tif -> /home/output/compounds/ta_vk/12/OBJ.tif
Copied /home/metadata/TA-VK12.mods -> /home/output/compounds/ta_vk/12/MODS.xml
Copied /home/images/TA-VK7.tif -> /home/output/compounds/ta_vk/7/OBJ.tif
Copied /home/metadata/TA-VK7.mods -> /home/output/compounds/ta_vk/7/MODS.xml
Copied /home/images/TA-LM10.tif -> /home/output/compounds/ta_lm/10/OBJ.tif
Copied /home/metadata/TA-LM10.mods -> /home/output/compounds/ta_lm/10/MODS.xml
Copied /home/images/TA-DB1.tif -> /home/output/compounds/ta_db/1/OBJ.tif
Copied /home/metadata/TA-DB1.mods -> /home/output/compounds/ta_db/1/MODS.xml
Copied /home/metadata/TA-DB1.mods -> /home/output/compounds/ta_db/MODS.xml
Copied /home/images/TA-LM7.tif -> /home/output/compounds/ta_lm/7/OBJ.tif
Copied /home/metadata/TA-LM7.mods -> /home/output/compounds/ta_lm/7/MODS.xml
Copied /home/images/TA-VT16.tif -> /home/output/compounds/ta_vt/16/OBJ.tif
Copied /home/metadata/TA-VT16.mods -> /home/output/compounds/ta_vt/16/MODS.xml
Copied /home/images/TA-RS5.tif -> /home/output/compounds/ta_rs/5/OBJ.tif
Copied /home/metadata/TA-RS5.mods -> /home/output/compounds/ta_rs/5/MODS.xml
Copied /home/images/TA-RS4.tif -> /home/output/compounds/ta_rs/4/OBJ.tif
Copied /home/metadata/TA-RS4.mods -> /home/output/compounds/ta_rs/4/MODS.xml
Copied /home/images/TA-VT17.tif -> /home/output/compounds/ta_vt/17/OBJ.tif
Copied /home/metadata/TA-VT17.mods -> /home/output/compounds/ta_vt/17/MODS.xml
Copied /home/images/TA-LM6.tif -> /home/output/compounds/ta_lm/6/OBJ.tif
Copied /home/metadata/TA-LM6.mods -> /home/output/compounds/ta_lm/6/MODS.xml
Copied /home/images/TA-VK6.tif -> /home/output/compounds/ta_vk/6/OBJ.tif
Copied /home/metadata/TA-VK6.mods -> /home/output/compounds/ta_vk/6/MODS.xml
Copied /home/images/TA-VK13.tif -> /home/output/compounds/ta_vk/13/OBJ.tif
Copied /home/metadata/TA-VK13.mods -> /home/output/compounds/ta_vk/13/MODS.xml
Copied /home/images/TA-VK11.tif -> /home/output/compounds/ta_vk/11/OBJ.tif
Copied /home/metadata/TA-VK11.mods -> /home/output/compounds/ta_vk/11/MODS.xml
Copied /home/images/TA-DB18.tif -> /home/output/compounds/ta_db/18/OBJ.tif
Copied /home/metadata/TA-DB18.mods -> /home/output/compounds/ta_db/18/MODS.xml
Copied /home/images/TA-VK4.tif -> /home/output/compounds/ta_vk/4/OBJ.tif
Copied /home/metadata/TA-VK4.mods -> /home/output/compounds/ta_vk/4/MODS.xml
Copied /home/images/TA-DB2.tif -> /home/output/compounds/ta_db/2/OBJ.tif
Copied /home/metadata/TA-DB2.mods -> /home/output/compounds/ta_db/2/MODS.xml
Copied /home/images/TA-LM4.tif -> /home/output/compounds/ta_lm/4/OBJ.tif
Copied /home/metadata/TA-LM4.mods -> /home/output/compounds/ta_lm/4/MODS.xml
Copied /home/images/TA-RS6.tif -> /home/output/compounds/ta_rs/6/OBJ.tif
Copied /home/metadata/TA-RS6.mods -> /home/output/compounds/ta_rs/6/MODS.xml
Copied /home/images/TA-VT15.tif -> /home/output/compounds/ta_vt/15/OBJ.tif
Copied /home/metadata/TA-VT15.mods -> /home/output/compounds/ta_vt/15/MODS.xml
Copied /home/images/TA-VT14.tif -> /home/output/compounds/ta_vt/14/OBJ.tif
Copied /home/metadata/TA-VT14.mods -> /home/output/compounds/ta_vt/14/MODS.xml
Copied /home/images/TA-RS7.tif -> /home/output/compounds/ta_rs/7/OBJ.tif
Copied /home/metadata/TA-RS7.mods -> /home/output/compounds/ta_rs/7/MODS.xml
Copied /home/images/TA-LM5.tif -> /home/output/compounds/ta_lm/5/OBJ.tif
Copied /home/metadata/TA-LM5.mods -> /home/output/compounds/ta_lm/5/MODS.xml
Copied /home/images/TA-DB3.tif -> /home/output/compounds/ta_db/3/OBJ.tif
Copied /home/metadata/TA-DB3.mods -> /home/output/compounds/ta_db/3/MODS.xml
Copied /home/images/TA-VK5.tif -> /home/output/compounds/ta_vk/5/OBJ.tif
Copied /home/metadata/TA-VK5.mods -> /home/output/compounds/ta_vk/5/MODS.xml
Copied /home/images/TA-VK10.tif -> /home/output/compounds/ta_vk/10/OBJ.tif
Copied /home/metadata/TA-VK10.mods -> /home/output/compounds/ta_vk/10/MODS.xml
Copied /home/images/TA-VK28.tif -> /home/output/compounds/ta_vk/28/OBJ.tif
Copied /home/metadata/TA-VK28.mods -> /home/output/compounds/ta_vk/28/MODS.xml
Copied /home/images/TA-VK14.tif -> /home/output/compounds/ta_vk/14/OBJ.tif
Copied /home/metadata/TA-VK14.mods -> /home/output/compounds/ta_vk/14/MODS.xml
Copied /home/images/TA-VK1.tif -> /home/output/compounds/ta_vk/1/OBJ.tif
Copied /home/metadata/TA-VK1.mods -> /home/output/compounds/ta_vk/1/MODS.xml
Copied /home/metadata/TA-VK1.mods -> /home/output/compounds/ta_vk/MODS.xml
Copied /home/images/TA-DB7.tif -> /home/output/compounds/ta_db/7/OBJ.tif
Copied /home/metadata/TA-DB7.mods -> /home/output/compounds/ta_db/7/MODS.xml
Copied /home/images/TA-LM1.tif -> /home/output/compounds/ta_lm/1/OBJ.tif
Copied /home/metadata/TA-LM1.mods -> /home/output/compounds/ta_lm/1/MODS.xml
Copied /home/metadata/TA-LM1.mods -> /home/output/compounds/ta_lm/MODS.xml
Copied /home/images/TA-RS3.tif -> /home/output/compounds/ta_rs/3/OBJ.tif
Copied /home/metadata/TA-RS3.mods -> /home/output/compounds/ta_rs/3/MODS.xml
Copied /home/images/TA-VT10.tif -> /home/output/compounds/ta_vt/10/OBJ.tif
Copied /home/metadata/TA-VT10.mods -> /home/output/compounds/ta_vt/10/MODS.xml
Copied /home/images/TA-VT11.tif -> /home/output/compounds/ta_vt/11/OBJ.tif
Copied /home/metadata/TA-VT11.mods -> /home/output/compounds/ta_vt/11/MODS.xml
Copied /home/images/TA-RS2.tif -> /home/output/compounds/ta_rs/2/OBJ.tif
Copied /home/metadata/TA-RS2.mods -> /home/output/compounds/ta_rs/2/MODS.xml
Copied /home/images/TA-DB6.tif -> /home/output/compounds/ta_db/6/OBJ.tif
Copied /home/metadata/TA-DB6.mods -> /home/output/compounds/ta_db/6/MODS.xml
Copied /home/images/TA-VK15.tif -> /home/output/compounds/ta_vk/15/OBJ.tif
Copied /home/metadata/TA-VK15.mods -> /home/output/compounds/ta_vk/15/MODS.xml
Copied /home/images/TA-VK29.tif -> /home/output/compounds/ta_vk/29/OBJ.tif
Copied /home/metadata/TA-VK29.mods -> /home/output/compounds/ta_vk/29/MODS.xml
Copied /home/images/TA-VK17.tif -> /home/output/compounds/ta_vk/17/OBJ.tif
Copied /home/metadata/TA-VK17.mods -> /home/output/compounds/ta_vk/17/MODS.xml
Copied /home/images/TA-VK2.tif -> /home/output/compounds/ta_vk/2/OBJ.tif
Copied /home/metadata/TA-VK2.mods -> /home/output/compounds/ta_vk/2/MODS.xml
Copied /home/images/TA-DB4.tif -> /home/output/compounds/ta_db/4/OBJ.tif
Copied /home/metadata/TA-DB4.mods -> /home/output/compounds/ta_db/4/MODS.xml
Copied /home/images/TA-LM2.tif -> /home/output/compounds/ta_lm/2/OBJ.tif
Copied /home/metadata/TA-LM2.mods -> /home/output/compounds/ta_lm/2/MODS.xml
Copied /home/images/TA-VT13.tif -> /home/output/compounds/ta_vt/13/OBJ.tif
Copied /home/metadata/TA-VT13.mods -> /home/output/compounds/ta_vt/13/MODS.xml
Copied /home/images/TA-RS1.tif -> /home/output/compounds/ta_rs/1/OBJ.tif
Copied /home/metadata/TA-RS1.mods -> /home/output/compounds/ta_rs/1/MODS.xml
Copied /home/metadata/TA-RS1.mods -> /home/output/compounds/ta_rs/MODS.xml
Copied /home/images/TA-VT12.tif -> /home/output/compounds/ta_vt/12/OBJ.tif
Copied /home/metadata/TA-VT12.mods -> /home/output/compounds/ta_vt/12/MODS.xml
Copied /home/images/TA-LM3.tif -> /home/output/compounds/ta_lm/3/OBJ.tif
Copied /home/metadata/TA-LM3.mods -> /home/output/compounds/ta_lm/3/MODS.xml
Copied /home/images/TA-DB5.tif -> /home/output/compounds/ta_db/5/OBJ.tif
Copied /home/metadata/TA-DB5.mods -> /home/output/compounds/ta_db/5/MODS.xml
Copied /home/images/TA-VK3.tif -> /home/output/compounds/ta_vk/3/OBJ.tif
Copied /home/metadata/TA-VK3.mods -> /home/output/compounds/ta_vk/3/MODS.xml
Copied /home/images/TA-VK16.tif -> /home/output/compounds/ta_vk/16/OBJ.tif
Copied /home/metadata/TA-VK16.mods -> /home/output/compounds/ta_vk/16/MODS.xml
Copied /home/images/TA-VT6.tif -> /home/output/compounds/ta_vt/6/OBJ.tif
Copied /home/metadata/TA-VT6.mods -> /home/output/compounds/ta_vt/6/MODS.xml
Copied /home/images/TA-VT7.tif -> /home/output/compounds/ta_vt/7/OBJ.tif
Copied /home/metadata/TA-VT7.mods -> /home/output/compounds/ta_vt/7/MODS.xml
Copied /home/images/TA-VT5.tif -> /home/output/compounds/ta_vt/5/OBJ.tif
Copied /home/metadata/TA-VT5.mods -> /home/output/compounds/ta_vt/5/MODS.xml
Copied /home/images/TA-VT4.tif -> /home/output/compounds/ta_vt/4/OBJ.tif
Copied /home/metadata/TA-VT4.mods -> /home/output/compounds/ta_vt/4/MODS.xml
Copied /home/images/TA-VT1.tif -> /home/output/compounds/ta_vt/1/OBJ.tif
Copied /home/metadata/TA-VT1.mods -> /home/output/compounds/ta_vt/1/MODS.xml
Copied /home/metadata/TA-VT1.mods -> /home/output/compounds/ta_vt/MODS.xml
Copied /home/images/TA-VT3.tif -> /home/output/compounds/ta_vt/3/OBJ.tif
Copied /home/metadata/TA-VT3.mods -> /home/output/compounds/ta_vt/3/MODS.xml
Copied /home/images/TA-VT2.tif -> /home/output/compounds/ta_vt/2/OBJ.tif
Copied /home/metadata/TA-VT2.mods -> /home/output/compounds/ta_vt/2/MODS.xml

```

results in
```commandline
> ls /home/output
compounds	large_images

> ls /home/output/compounds
ta_db	ta_jd	ta_lm	ta_rs	ta_vk	ta_vt

> ls /home/output/compounds/ta_db
1		12		15		18		4		7		MODS.xml
10		13		16		2		5		8
11		14		17		3		6		9

> ls /home/output/compounds/ta_db/1
MODS.xml	OBJ.tif
```

## License
MIT