# Testing_demo
Testing

## Link 
[Git Handbook](https://guides.github.com/introduction/git-handbook/)

<img src="https://th.bing.com/th/id/R.724794164fb289dd2f7d69dde7ac3bc0?rik=0Ubh3aP6JzCPcw&riu=http%3a%2f%2fpngimg.com%2fuploads%2fgithub%2fgithub_PNG40.png&ehk=vDH1g6b2G5qphfQR7RsUJ7HmqSSwIMycien%2fvBj03ZU%3d&risl=&pid=ImgRaw&r=0" alt="Github" width="300" height="300">

## Code for Logging
```Python
import logging
import os
logging_str="[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
logging_dir= "../logs"
os.makedirs(logging_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(logging_dir,"running_logs.log"),level=logging.INFO,format=logging_str,filemode="a")
```

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)]

