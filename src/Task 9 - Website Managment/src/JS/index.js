import * as UI from './UI.js'
import { Get } from './request.js'
// import * as CanvasJS from 'canvasjs'
// import * as fs from 'fs'

// Constanses
var Adress = 'http://localhost:5000/Data'

const maxPoints = 10

loadCharts()


/**
 * Does Everything that controlls the Website
 */
function loadCharts (params) {
  // Load the UI For the specific Parts of the Page
  var Work = document.getElementById('One')
  One(Work)

  setTimeout(function () {
    Work = document.getElementById('Two')
    Two(Work)
  }, 1000)

  setTimeout(function () {
    Work = document.getElementById('Three')
    Three(Work)
  }, 1000)

  setTimeout(function () {
    Work = document.getElementById('Four')
    Four(Work)
  }, 1000)

  setTimeout(function () {
    Work = document.getElementById('Five')
    Five(Work)
  }, 1000)

  setTimeout(function () {
    Work = document.getElementById('Six')
    Six(Work)
  }, 1000)

  setTimeout(function () {
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
  var Temp = Data.sechs
  var datapointsTemp = []
  for (var i = maxPoints; i >0; i--){
    datapointsTemp.push({ y: parseInt(Temp[i].price), label: Temp[i].name })
  }

  var chart = new CanvasJS.Chart('One', {
    animationEnabled: false,

    axisX: {
      interval: 1
    },
    axisY2: {
      interlacedColor: 'rgba(1,77,101,.2)',
      gridColor: 'rgba(1,77,101,.1)'
    },
    data: [{
      type: 'bar',
      name: 'Bought',
      axisYType: 'secondary',
      color: '#014D65',
      dataPoints: datapointsTemp
    }]
  })
  chart.render()

}

// what is rated highest
function Two (WorkingObject) {
  var QuestionId = 7
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Returns: Name, Score

  var Temp = Data.sieben
  var datapointsTemp = []
  for (var i = maxPoints; i >0; i--){
    datapointsTemp.push({ y: parseInt(Temp[i].score), label: Temp[i].name })
  }

  var chart = new CanvasJS.Chart('Two', {
    animationEnabled: false,

    axisX: {
      interval: 1
    },
    axisY2: {
      interlacedColor: 'rgba(1,77,101,.2)',
      gridColor: 'rgba(1,77,101,.1)',
      title: 'Rating Score'
    },
    data: [{
      type: 'bar',
      name: 'Rating',
      axisYType: 'secondary',
      color: '#014D65',
      dataPoints: datapointsTemp
    }]
  })
  chart.render()
}

// What do we have in stock
function Three (WorkingObject) {
  var QuestionId = 8
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)
  // returns Name and charge

  var Temp = Data.acht

  // TODO: USE THAT
  var newtablle = document.createElement('table')

  var newLine = document.createElement('tr')
  // Add the first line
  var newName = document.createElement('th')
  newName.innerText = 'Name'
  newLine.appendChild(newName)

  var newCharge = document.createElement('th')
  newCharge.innerText = 'Charge'
  newCharge.appendChild(newName)

  newtablle.appendChild(newLine)

  // Load Names
  var NameRow = document.createElement('tr')
  Temp.forEach(element => {
    var tempElement = document.createElement('tr')

    var TempName = document.createElement('th')
    TempName.innerText = element.name
    tempElement.appendChild(TempName)
    
    var TempCharge = document.createElement('th')
    TempCharge.innerText = element.charge
    tempElement.appendChild(TempCharge)

    newtablle.appendChild(tempElement)
  })
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

  var Temp = Data.neun
  var datapointsTemp = []
  for (var i = maxPoints; i >0; i--){
    datapointsTemp.push({ y: parseInt(Temp[i].charge), label: Temp[i].name })
  }

  var chart = new CanvasJS.Chart('Four', {
    animationEnabled: false,

    axisX: {
      interval: 1
    },
    axisY2: {
      interlacedColor: 'rgba(1,77,101,.2)',
      gridColor: 'rgba(1,77,101,.1)'
    },
    data: [{
      type: 'bar',
      name: 'Charge',
      axisYType: 'secondary',
      color: '#014D65',
      dataPoints: datapointsTemp
    }]
  })
  chart.render()
}

// User who made the most Comments
function Five (WorkingObject) {
  var QuestionId = 10
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Return name, charge

  var Temp = Data.zehn
  var datapointsTemp = []
  for (var i = maxPoints; i >0; i--){
    datapointsTemp.push({ y: parseInt(Temp[i].charge), label: Temp[i].name })
  }


  var chart = new CanvasJS.Chart('Five', {
    animationEnabled: false,

    axisX: {
      interval: 1
    },
    axisY2: {
      interlacedColor: 'rgba(1,77,101,.2)',
      gridColor: 'rgba(1,77,101,.1)'
    },
    data: [{
      type: 'bar',
      name: 'charge',
      axisYType: 'secondary',
      color: '#014D65',
      dataPoints: datapointsTemp
    }]
  })
  chart.render()
}

// Umsatz pro Produkt
function Six (WorkingObject) {
  var QuestionId = 11
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  var Temp = Data.elf
  var datapointsTemp = []
  for (var i = maxPoints; i >0; i--){
    datapointsTemp.push({ y: parseInt(Temp[i].Revenue), label: Temp[i].Name })
  }

  var chart = new CanvasJS.Chart('Six', {
    animationEnabled: false,

    axisX: {
      interval: 1
    },
    axisY2: {
      interlacedColor: 'rgba(1,77,101,.2)',
      gridColor: 'rgba(1,77,101,.1)',
      title: 'Names'
    },
    data: [{
      type: 'bar',
      name: 'Revenue in €',
      axisYType: 'secondary',
      color: '#014D65',
      dataPoints: datapointsTemp
    }]
  })
  chart.render()
}

// GesamtUmsatz
function Seven (WorkingObject) {
  var QuestionId = 12

  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  WorkingObject.appendChild(UI.headline((Data.zwölf[0].Revenue) + '€'))
}


