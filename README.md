# HOW TO RUN

1. Install the required packages in `requirements.txt`, using `pip install -r requirements.txt`
2. Download the AI models from [Google Drive](https://drive.google.com/drive/folders/1mWHrCmWuCyjJ9Dat3zD2FutL4G3UG9-6?usp=sharing)
3. Extract the AI models to the folder `model_instances` directly under the root of the project.  
The project tree should look like this now:  
```
.  
├── README.md  
├── config  
│   └── gemini.py  
├── lib  
│   ├── analysis  
│   │   ├── ...  
├── main.py  
├── model_instances  
│   ├── Blstm_model_vf.h5  
│   └── Cnn_model_vf.keras  
└── requirements.txt  
```
4. Run `python main.py`
