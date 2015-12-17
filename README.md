deps-to-dots
============

Reads #include statements in C and C++ code to generate a graphviz dot file.

### Usage:

The script walks through a project given the project directory path and documents the include relationships.

```./make_dot.py [project_root]```

### Example:
XML Indent makes a good example (https://github.com/penberg/xmlindent).  Clone xmlindent and set the [project root] to be the xmlindent project path.

```./make_dot.py ../xmlindent```

#### Graph Output:

For xmlindent, ```make_dots.py``` will render the following graph and save the corresponding dot file: 
![GV Graph](https://raw.githubusercontent.com/cdated/deps-to-dots/master/example/xmlindent.png)
