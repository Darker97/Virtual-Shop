import * as UI from './UI.js'
import { Get } from './request.js'
import * as CanvasJS from 'canvasjs'

/**
 * Does Everything that controlls the Website
 */

var Adress = 'http://localhost:5000/Data'

loadCharts()

function loadCharts (params) {
  // Load the UI For the specific Parts of the Page
  var Work = document.getElementById('One')
  One(Work)

  setTimeout(function() {
    Work = document.getElementById('Two')
    Two(Work)
  }, 1000)
  
  setTimeout(function() {
    Work = document.getElementById('Three')
    Three(Work)
  }, 1000)

  setTimeout(function() {
    Work = document.getElementById('Four')
    Four(Work)
  }, 1000)

  setTimeout(function() {
    Work = document.getElementById('Five')
    Five(Work)
  }, 1000)

  setTimeout(function() {
    Work = document.getElementById('Six')
    Six(Work)
  }, 1000)

  setTimeout(function() {
    Work = document.getElementById('Seven')
    Seven(Work)
  }, 1000)
}

/**
 * What is bought the Most?
 * @param {} WorkingObject
 */
function One (WorkingObject) {
  var QuestionId = 6
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Returns: Name, Price, charge
  var Temp = Data.6
  var datapointsTemp = []
  Temp.forEach(element => datapointsTemp.push({y:element.Rating, label: Products_Name}));


  var chart = new CanvasJS.Chart("One", {
	animationEnabled: false,
	
	axisX:{
		interval: 1
	},
	axisY2:{
		interlacedColor: "rgba(1,77,101,.2)",
		gridColor: "rgba(1,77,101,.1)",
		title: "Names"
	},
	data: [{
		type: "bar",
		name: "Bought",
		axisYType: "secondary",
		color: "#014D65",
		dataPoints: datapointsTemp
	}]
    })
chart.render();

}

// what is rated highest
function Two (WorkingObject) {
  var QuestionId = 7
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Returns: Name, Score

  var Temp = Data.7
  var datapointsTemp = []
  Temp.forEach(element => datapointsTemp.push({y:element.Score, label: element.Name}));


  var chart = new CanvasJS.Chart("Two", {
	animationEnabled: false,
	
	axisX:{
		interval: 1
	},
	axisY2:{
		interlacedColor: "rgba(1,77,101,.2)",
		gridColor: "rgba(1,77,101,.1)",
		title: "Names"
	},
	data: [{
		type: "bar",
		name: "Rating",
		axisYType: "secondary",
		color: "#014D65",
		dataPoints: datapointsTemp
	}]
    })
chart.render();
}

// What do we have in stock
function Three (WorkingObject) {
  var QuestionId = 8
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)
  // returns Name and charge

  var Temp = Data.8

  // TODO: USE THAT
  var newtablle = document.createElement("table")
  var newLine = document.createElement("tr")

  // Add the first line
  var newName = document.createElement("th")
  newName.innerText = "Name"
  newLine.appendChild(newName)

  var newCharge = document.createElement("th")
  newCharge.innerText = "Charge"
  newCharge.appendChild(newName)

  newtablle.appendChild(newLine)

  // Load Names
  var NameRow = document.createElement("tr")
  Temp.forEach(element => {
      var tempElement = document.createElement("th")
      tempElement.innerText = element.Name
      NameRow.appendChild(tempElement)
  })
  newtablle.appendChild(NameRow)

  // Load charge
  var ChargeRow =  document.createElement("tr")
  Temp.forEach(element => {
    var tempElement = document.createElement("th")
    tempElement.innerText = element.Name
    ChargeRow.appendChild(tempElement)
  })
  newtablle.appendChild(ChargeRow)

  WorkingObject.appendChild(newtablle)
}

// Product with the most comments
function Four (WorkingObject) {
  var QuestionId = 9
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Returns Name and Charge

  var Temp = Data.9
  var datapointsTemp = []
  Temp.forEach(element => datapointsTemp.push({y:element.Charge, label: element.Name}));


  var chart = new CanvasJS.Chart("Four", {
	animationEnabled: false,
	
	axisX:{
		interval: 1
	},
	axisY2:{
		interlacedColor: "rgba(1,77,101,.2)",
		gridColor: "rgba(1,77,101,.1)",
		title: "Names"
	},
	data: [{
		type: "bar",
		name: "Charge",
		axisYType: "secondary",
		color: "#014D65",
		dataPoints: datapointsTemp
	}]
    })
}

// User who made the most Comments
function Five (WorkingObject) {
  var QuestionId = 10
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Return name, charge

  var Temp = Data.10
  var datapointsTemp = []
  Temp.forEach(element => datapointsTemp.push({y:element.charge, label: element.name}));


  var chart = new CanvasJS.Chart("Five", {
	animationEnabled: false,
	
	axisX:{
		interval: 1
	},
	axisY2:{
		interlacedColor: "rgba(1,77,101,.2)",
		gridColor: "rgba(1,77,101,.1)",
		title: "Names"
	},
	data: [{
		type: "bar",
		name: "charge",
		axisYType: "secondary",
		color: "#014D65",
		dataPoints: datapointsTemp
	}]
    })

// Umsatz pro Produkt
function Six (WorkingObject) {
  var QuestionId = 11
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  var Temp = Data.11
  var datapointsTemp = []
  Temp.forEach(element => datapointsTemp.push({y:element.Revenue, label: element.Name}));


  var chart = new CanvasJS.Chart("Six", {
	animationEnabled: false,
	
	axisX:{
		interval: 1
	},
	axisY2:{
		interlacedColor: "rgba(1,77,101,.2)",
		gridColor: "rgba(1,77,101,.1)",
		title: "Names"
	},
	data: [{
		type: "bar",
		name: "Revenue",
		axisYType: "secondary",
		color: "#014D65",
		dataPoints: datapointsTemp
	}]
    })
}

// GesamtUmsatz
function Seven (WorkingObject) {
  var QuestionId = 12
  
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  var newHeadline = UI.headline(Data.12[0].Revenue)
}
