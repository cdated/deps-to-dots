deps-to-dots
============

Reads #include statements in C and C++ code to generate a graphviz dot file.

### Usage:

The script walks through a project given the project directory path and documents the include relationships.

```./make_dot.py [project_root] > example.dot```

### Example:
XML Indent makes a good example (https://github.com/penberg/xmlindent).  Clone xmlindent and set the [project root] to be the xmlindent project path.

```./make_dot.py ../xmlindent > example.dot```

#### Gephi Visualization:

Gephi is a great tool to visualize graphviz dot files.  Here is the result of loading the generated xmlindent dot file in Gephi: 
![Gephi Graph](https://raw.githubusercontent.com/cdated/deps-to-dots/master/example/example_gephi.png)
