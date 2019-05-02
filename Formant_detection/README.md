
The Estimation model can be downloaded here 
[tracking_model.mat] (https://drive.google.com/open?id=0Bxkc5_D0JjpiZWx4eTU1d0hsVXc)


For vowel formant estimation, call the main script in a terminal with the following inputs: wav file, formant output filename, and the vowel begin and end times:

```
python formants.py data/Example.wav data/ExamplePredictions.csv --begin 1.2 --end 1.3
```

or the vowel begin and end times can be taken from a TextGrid file (here the name of the TextGrid is Example.TextGrid and the vowel is taken from a tier called "VOWEL"):

```
python formants.py data/Example.wav data/examplePredictions.csv --textgrid_filename data/Example.TextGrid \
          --textgrid_tier VOWEL
```

For formant tracking, just call the script with the wav file and output filename:

```
python formants.py data/Example.wav data/ExamplePredictions.csv
```
