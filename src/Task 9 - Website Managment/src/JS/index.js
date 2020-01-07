import * as CanvasJS from CanvasJS;

/**
 * Does Everything that controlls the Website
 */

function loadCharts(params) {

    // MostBrougth

    var Data = LoadMostBrougth()

    var chart = new CanvasJS.Chart("MostBrougth", {
        animationEnabled: true,
        axisX:{
            interval: 1
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Number of Companies"
        },
        data: [{
            type: "bar",
            name: "companies",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: Data
        }]
    });
    chart.render();

    // Rating

    var Data = LoadsRating()

    var chart = new CanvasJS.Chart("Rating", {
        animationEnabled: true,
        axisX:{
            interval: 1
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Number of Companies"
        },
        data: [{
            type: "bar",
            name: "companies",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: Data
        }]
    });
    chart.render();

    // WhatInStock
    var Data = loadsWhatInStock()

    var chart = new CanvasJS.Chart("WhatInStock", {
        animationEnabled: true,
        axisX:{
            interval: 1
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Number of Companies"
        },
        data: [{
            type: "bar",
            name: "companies",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: Data
        }]
    });
    chart.render();

    // MostCommentsProduct
    var Data = LoadsMostCommentsProduct()

    var chart = new CanvasJS.Chart("MostCommentsProduct", {
        animationEnabled: true,
        axisX:{
            interval: 1
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Number of Companies"
        },
        data: [{
            type: "bar",
            name: "companies",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: Data
        }]
    });
    chart.render();

    // MostCommenstUser
    var Data = LoadsMostCommenstUser()

    var chart = new CanvasJS.Chart("MostCommenstUser", {
        animationEnabled: true,
        axisX:{
            interval: 1
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
            title: "Number of Companies"
        },
        data: [{
            type: "bar",
            name: "companies",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: Data
        }]
    });
    chart.render();
    
}

function loadData(params) {

}

function LoadMostBrougth(params) {
    // y, label
}

function LoadsRating(params) {
    // y, label
}

function loadsWhatInStock(params) {
    // y, label
}

function LoadsMostCommentsProduct(params) {
    // y, label
}

function LoadsMostCommenstUser(params) {
    // y, label
}