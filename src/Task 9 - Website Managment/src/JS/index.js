import * as CanvasJS from CanvasJS;
import load from Data;

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

function LoadMostBrougth(params) {
    var Link = ""
    // y, label
    var Data = []
    var cookie = load("Cookie")

    // SecurityCookie, QuestionID
    Message = {
        "SecurityCookie": cookie,
        "QuestionID": "1"
            }
    var rohData = Get(Link, Message)

    // remake rohData

    return Data
}

function LoadsRating(params) {
    var Link = ""
    // y, label
    var Data = []
    var cookie = load("Cookie")

    // SecurityCookie, QuestionID
    Message = {
        "SecurityCookie": cookie,
        "QuestionID": "1"
            }
    var rohData = Get(Link, Message)

    // remake rohData

    return Data
}

function loadsWhatInStock(params) {
    var Link = ""
    // y, label
    var Data = []
    var cookie = load("Cookie")

    // SecurityCookie, QuestionID
    Message = {
        "SecurityCookie": cookie,
        "QuestionID": "1"
            }
    var rohData = Get(Link, Message)

    // remake rohData

    return Data
}

function LoadsMostCommentsProduct(params) {
    var Link = ""
    // y, label
    var Data = []
    var cookie = load("Cookie")

    // SecurityCookie, QuestionID
    Message = {
        "SecurityCookie": cookie,
        "QuestionID": "1"
            }
    var rohData = Get(Link, Message)

    // remake rohData

    return Data
}

function LoadsMostCommenstUser(params) {
    var Link = ""
    // y, label
    var Data = []
    var cookie = load("Cookie")

    // SecurityCookie, QuestionID
    Message = {
        "SecurityCookie": cookie,
        "QuestionID": "1"
            }
    var rohData = Get(Link, Message)

    // remake rohData

    return Data
}