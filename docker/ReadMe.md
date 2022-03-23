# Objective
Write a program that calculates pixel coordinate values 
for an image that is to be displayed on a two dimensional 
surface given the dimensions of the image and the corner 
points of the image.

**Output:** Program calculates and returns the x and y coordinates 
at which to plot each pixel in the input image such that 
the pixels are evenly spaced within the rectangle defined 
by the corner points.

## Features
<ul>
    <li>Corner points can be provided in any order, 
    program determines which is the bottom left, top right etc.</li>
    <li>Uses Flask to return response to POST request containing
    the inputs in the body of the payload</li>
    <li>Packaged in Docker container</li>
</ul>

## Preinstall 

Please make sure you install docker on your OS environment.

## How to run

docker-compose up<br>
runs on http://localhost:5000/ (make sure that this is the url used)

## Input structure

<code>{
                "image_dimensions": (10, 12),
                "corner_points": [
                    (1.5, 1.5),
                    (4.0, 1.5),
                    (1.5, 8.0),
                    (4.0, 8.0)
                ]
            }</code>

**Note:** If using Postman, input must be lists instead of tuples
