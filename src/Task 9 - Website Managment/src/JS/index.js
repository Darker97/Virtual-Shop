import * as UI from 'UI.js'
import { Get } from './request'

/**
 * Does Everything that controlls the Website
 */

var Adress = 'localhost:5000/Data'

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
}

/**
 * What is bought the Most?
 * @param {} WorkingObject 
 */
function One (WorkingObject) {
  var QuestionId = 6
  var body = { SecurityCookie: 'hdash', QuestionID: QuestionId }
  var Data = Get(Adress, body)

  // Returns: Name, Price, charge

  // TODO: USE THAT
  console.log(Data)
  return ''
}

function Two (WorkingObject) {
  var QuestionId = 7
  var body = { SecurityCookie: 'hdash', QuestionID: QuestionId }
  var Data = Get(Adress, body)
}

function Three (WorkingObject) {
  var QuestionId = 8
  var body = { SecurityCookie: 'hdash', QuestionID: QuestionId }
  var Data = Get(Adress, body)


  // TODO: USE THAT
  console.log(Data)
  return ''
}

function Four (WorkingObject) {
  var QuestionId = 9
  var body = { SecurityCookie: 'hdash', QuestionID: QuestionId }
  var Data = Get(Adress, body)

  // TODO: USE THAT
  console.log(Data)
  return ''
}

function Five (WorkingObject) {
  var QuestionId = 10
  var body = { SecurityCookie: 'hdash', QuestionID: QuestionId }
  var Data = Get(Adress, body)

  // TODO: USE THAT
  console.log(Data)
  return ''
}
