# rpigpsthingy

# INTRODUCTION

This is a currently ongoing project involving a customized GoogleMaps-like GPS system for the RPI campus. This is currently accessible as a Python file that inputs a few initial values and generates a list of successively improving paths between the two points.

# CONTRIBUTORS

Owen Goff (goffo@rpi.edu). If anyone lese is interested in helping, shoot me an email!

# DESCRIPTION

The algorithm used is a version of Dijkstra's algorithm, applied on an adjustable list of coordinates. Every coordinate is the intersection of two paths, expressed as a two-element tuple of integers. An expanded version will likely generalize this to either 3- or 4-element tuples, or to a dictionary.

To use the 

# VERSIONS

Version 1.0

This currently has:
1) an improved algorithm that allows the analysis of the paths between a point in downtown Troy and a point on Freshman hill in under one minute. This, however, I would like to improve further with Dijkstra's Algorithm.

2) A graphical representation for the campus, written using a Kalamazoo.edu-generated graphics module in Python

# PREREQUISITES

Python 2.7. I believe 2.5-2.7 will al work. 3.x will not work properly because of the print function.

# 