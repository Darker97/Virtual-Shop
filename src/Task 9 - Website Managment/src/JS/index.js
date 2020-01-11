import * as UI from './UI.js'
import { Get } from './request.js'

/**
 * Does Everything that controlls the Website
 */

var Adress = 'http://localhost:5000/Data'

loadCharts()

function loadCharts (params) {
  // Load the UI For the specific Parts of the Page
  var Work = document.getElementById('One')
  One(Work)

  Work = document.getElementById('Two')
  Two(Work)

  Work = document.getElementById('Three')
  Three(Work)

  Work = document.getElementById('Four')
  Four(Work)

  Work = document.getElementById('Five')
  Five(Work)

  Work = document.getElementById('Six')
  Six(Work)

  Work = document.getElementById('Seven')
  Seven(Work)
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

  // TODO: USE THAT
  console.log(Data)
  return ''
}

// what is rated highest
function Two (WorkingObject) {
  var QuestionId = 7
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Returns: Name, Score

  // TODO: USE THAT
  console.log(Data)
  return ''
}

// What do we have in stock
function Three (WorkingObject) {
  var QuestionId = 8
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)
  // returns Name and charge

  // TODO: USE THAT
  console.log(Data)
  return ''
}

// Product with the most comments
function Four (WorkingObject) {
  var QuestionId = 9
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // Returns Name and Charge

  // TODO: USE THAT
  console.log(Data)
  return ''
}

// User who made the most Comments
function Five (WorkingObject) {
  var QuestionId = 10
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // TODO: USE THAT
  console.log(Data)
  return ''
}

// Umsatz pro Produkt
function Six (WorkingObject) {
  var QuestionId = 10
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // TODO: USE THAT
  console.log(Data)
  return ''
}

// GesamtUmsatz
function Seven (WorkingObject) {
  var QuestionId = 10
  
  var form = new FormData()
  form.append('SecurityCookie', 'dasd')
  form.append('QuestionID', QuestionId)
  var Data = Get(Adress, form)

  // TODO: USE THAT
  console.log(Data)
  return ''
}
