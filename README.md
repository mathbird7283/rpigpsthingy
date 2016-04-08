# RPI GPS System

# INTRODUCTION

This is a currently ongoing project involving a customized GoogleMaps-like GPS system for the RPI campus. This is currently accessible as a Python file that inputs a few initial values and generates a list of successively improving paths between the two points.

# CONTRIBUTORS

Owen Goff (goffo@rpi.edu), with some assistance from Avi Weinstock.
If anyone else is interested in helping, shoot me an email!

# DESCRIPTION

The algorithm used is a version of Dijkstra's algorithm, applied on an adjustable list of coordinates. Every coordinate is the intersection of two paths, expressed as a two-element tuple of integers. An expanded version will likely generalize this to either 3- or 4-element tuples, or to a dictionary.

To use the algorithm, a total of six numerical values are imported: walking speed, debug boolean, and the 4 numbers indicating the start and end points of the path. The user can then obsevre the algorithm at work as it prints out faster and faster paths. At the moment the "speed" of the path is based solely on the number of separate routes it traverses and not the length of the routes, though this is coming in a later update. 

# VERSIONS

# Version 1.0.2
Added a dictionary that creates a priority queue structure

# Version 1.0.1
Improved start and end customization.

# Version 1.0.0

This currently has:

1) an improved algorithm that allows the analysis of the paths between a point in downtown Troy and a point on Freshman Hill in under one minute. This, however, I would like to improve further with Dijkstra's Algorithm.

2) A graphical representation for the campus, written using a Python graphics module developed by Wartburg College in Iowa.

# PREREQUISITES

Python 2.7. I believe 2.5-2.7 will all work. 3.x will not work properly because of the print function applied in later versions of python.

Some good values to start with are (1,2) to (9,10) or (1,2) to (61,63) (the former goes from downtown Troy to 8th and Peoples, the latter to Freshman Hill.)

# NOTES

Lgraphics.py is not my own file; it is a graphics module obtained from http://mcsp.wartburg.edu/zelle/python/graphics.py Also, Additional Documentation provided by Avi Weinstock.py is a transcription of code provided by fellow RCOS participant Avi Weinstock (see above).

April 8, 2016