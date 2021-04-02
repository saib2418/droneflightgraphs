# Drone Flight Data Graphs
Raw Data produced by drone flights converted into various graphs to optimize features such as battery voltage, and battery age resulting in maximizing drone flight success with Python. 

## Table of Contents 
* [About This Project] (#about-this-project)
* [Built With] (#built-with)
* [Setup] (#setup)
* [Usage] (#usage)
* [License] (#license)
* [Contact] (#contact)

## About This Project
After conducting many drone flight tests, the data of what battery was used, battery, tempearture, the voltage drop, how long the drone was flying, and weather the drone succeded or failed was recorded in the excel sheet titles "Battery Aging." 

<p>
Figure 1 plots failed flights [orange color] vs successful flights [blue color] over 30 second intervals, while the table quantifies this data. 
</p>

<div class="row">
  <div class="column">
    <img src="graph_images/fig1.png" style="width:100%">
  </div>
  <div class="column">
    <img src="graph_images/table.png" style="width:100%">
  </div>
</div>

<p>
Figure 2 plots Battery Voltage Drop vs Total Flight Time of the drones to see at what voltage drop and time a drone failed or succeeded. 
</p>

<img align = "left" width = "450" src="graph_images/fig2.png">

<p>
Figure 3 zooms in on the time stamps where the most failed flights occured.
</p>

<img align = "right"  width = "450" src="graph_images/fig3.png">

<p> Figure 4 plots Battery Age vs the Total Flight Time he drones to see at what voltage drop and time a drone failed or succeeded.</p>

<img src="graph_images/fig4.png" width = "600">

<p>Figure 5 plots Battery Age, Battery Voltage Drop, and Total Flight Time to see at what voltage drop, and batterry age a drone faield or succeeded.</p>

<img src="graph_images/fig5.png" width = "600">

## Built With
Project is Created With: 
* Python 3.8.2
* Pandas
* Numpy
* MatPlotLib
* Plotly
