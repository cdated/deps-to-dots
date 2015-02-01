deps-to-dots
============

Reads #include statements in C and C++ code to generate a graphviz dot file.

### Usage:

The script starts with the main file and stays within the project.

```./make_dot.py [project_root] > example.dot```

Example:
XML Indent makes a good example (https://github.com/penberg/xmlindent).  Clone xmlindent and set the [project root] to be the xmlindent project path.

```./make_dot.py ../xmlindent > example.dot```

### Example in Gephi:

Gephi is a great tool to visualize graphviz dot files.  Here is the result of loading the generated xmlindent dot file in Gephi: 
![Gephi Example](https://raw.githubusercontent.com/cdated/deps-to-dots/master/example/example_gephi.png)
