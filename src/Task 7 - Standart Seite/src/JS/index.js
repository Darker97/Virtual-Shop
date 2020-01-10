import * as ui from './UI.js'
import * as api from './API.js'
import * as request from './request.js'
import * as data from './Data.js'

/**
 * Does Everything that controlls the Website
 */

// import doesnt work "TypeError: Error resolving module specifier: js-sha3"
// import * as sha from 'js-sha3'

// Tests 
console.log('test')
let test = ui.headline('text')

login()
loadData()


function login() { // script on load login in html!!
  // Check for Input
  document.getElementById('button1').addEventListener('click', function () {
    loadInput()
    // hashLoginData()
  })

// Load Input
    function loadInput() {
        let username = document.getElementById('username1').value
        let password = document.getElementById('password1').value
        console.log(username)
        console.log(password)
        return [username, password]
    }    

    // HASH Input with Library: https://github.com/emn178/js-sha3    Use sha3_256


    /*
      function hashLoginData() {
        var sha3_256 = require('js-sha3').sha3_256
        let usernameHashed = sha.sha3_256(loadInput()[0])
        let passwordHashed = sha.sha3_256(loadInput()[1])
        console.log(usernameHashed)
      }
    */

    // send Request to API via API.js

    // Check answer

    // Save Answer as Cookie
}

function loadData(params) {

    // Load Data
    // test
    let i = 0
    while(i !== 5) {
        let view = ui.view()
        let name = ui.headline('name')
        let price =ui.headline3('price')
        let text = ui.content('lalalala')
        let button = ui.button('See more')
        document.getElementById('grid').appendChild(view)
        document.querySelectorAll('artikel')[i].appendChild(name)
        document.querySelectorAll('artikel')[i].appendChild(price)
        document.querySelectorAll('artikel')[i].appendChild(text)
        document.querySelectorAll('artikel')[i].appendChild(button)
        i++
    }

    // Check for Cookie

    // if Cookie is there, load special Data

}