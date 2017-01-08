# Installation
In order to use this program, I raccomend to create a `virtualenv`
```
python3 -m venv cw_env
source cw_env/bin/activate
```

Next, we need some dependencies
```
pip install -r requirements.txt
```

# Usage
There are two ways to use the program:
- Describing the problem using the interactive prompts   
`python numeric_crosswords.py`
- Using a JSON file that describes the problem. See the `examples` folder   
`python numeric_crosswords.py -cw examples/assignment_cw.json`   
