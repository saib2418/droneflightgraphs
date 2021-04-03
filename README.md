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
<style>
  .content {
    max-width: 1024px;
    width: 100%;
    text-align: center;
    margin: auto;
  }
  p {
    text-align: left;
  }
  .container {
    display: flex;
  }
</style>

<div class="content">
  <p>
    Figure 1 plots failed flights [orange color] vs successful flights [blue color] over 30 second intervals, while the table quantifies this data. 
  </p>
  
  <div class="container">
    <img src="graph_images/fig1.png" alt="graph 1">
    <img src="graph_images/table.png" alt="graph 1 info">
  </div>
  
  <p>
  Figure 2 plots Battery Voltage Drop vs Total Flight Time of the drones to see at what voltage drop and time a drone failed or succeeded. 
  </p>
  
  <div class="container">
    <img src="graph_images/fig2.png" alt="graph 2">
  </div>
  
  <p>
  Figure 3 zooms in on the time stamps where the most failed flights occurred.
  </p>
  
  <div class="container">
    <img src="graph_images/fig3.png" alt="graph 3">
  </div>
</div>

<p> 
  Figure 4 plots Battery Age vs the Total Flight Time he drones to see at what voltage drop and time a drone failed or succeeded. 
</p>

<p align="center">
  <img width="600" src="graph_image/fig4.png">
</p>


<p> 
  Figure 5 plots Battery Age, Battery Voltage Drop, and Total Flight Time to see at what voltage drop, and batterry age a drone faield or succeeded. 
</p>

<p align="center">
  <img width="600" src="graph_image/fig5.png">
</p>


## Built With
Project is Created With: 
* Python 3.8.2
* Pandas
* Numpy
* MatPlotLib
* Plotly
