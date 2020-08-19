# Godseye
Godseye is a CLI based virtual asisstant that is written in python 3.7.6 and external file in batch script
## Installation

download both bat file for wifi capabilities

download nltk library using pip-
```bash
pip install nltk
```
## Capabilities
user can open or use following commands and tools-
 - '--help'
 - say hello
 - ask date or time
 - open google chrome
 - visual studio code
 - windows media player
 - youtube, facebook, google
 - can run specificed url
 - open file/folder 
 - enable, disable wifi
 - search on google
 - calculator
 - shutdown, restart

to overcome problems in 'in' keyword, word_tokenize is used
## Usage
if you are using nltk library for the first time then include- 
```python
import nltk
nltk.download('punkt')
```

exceptable keywords for running program are- run, execute, open with few exceptions like - "run url [url]", "open [folder\file name]", "enabel wifi", "disable wifi", "search [query]", "shutdown", "restart"

for wifi capabilities copy path of bat files in source code

**if you disable wifi using godseye then do not forget to turn it on using godseye only otherwise there might be some issues**
