Audio_classification
==============================
Project: Classify sound for pil og flue (work in progress)
------------

Project Organization
-----------
    ├── csv                                 <- CSV files
    │   ├── raw.csv
    │   └── validation.csv      
    │    
    ├── nbs                                 <- Jupyter notebooks. 
    │     ├── ensemble_modeling.ipynb
          ├── move_spectogram.ipynb
          ├── preprocessing.ipynb
    │     ├── spectogram_classification.ipynb
    │     └── waveform_classification.ipynb
    ├── audio_files.zip                     <- WAV audio files  
    └── README.md                           <-The top-level README for developers using this project.
--------
## Notebooks
`ensemble_modeling.ipynb`: Combining the trained waveform classification model and spectogram classification model to predict input data. 
</br>
`move_spectogram.ipynb`: Move spectograms to validation folder. 
</br>
`preprocessing.ipynb`:Creating spectogram, waveform data, and splitting the data into training set and validation set.
</br>
`spectogram_classification.ipynb`: Training a spectogram classification model
</br>
`waveform_classification.ipynb`: Training a waveform classification model
</br>
## csv
`raw.csv`: waveform features
</br>
`validation.csv`: filenames of validation data
