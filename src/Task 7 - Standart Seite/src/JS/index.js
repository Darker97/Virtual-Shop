import * as ui from './UI.js'
import * as api from './API.js'
import * as request from './request.js'
import * as data from './Data.js'

/**
 * Does Everything that controlls the Website
 */
var adress = 'localhost:5000/Data'
// import doesnt work "TypeError: Error resolving module specifier: js-sha3"
// import * as sha from 'js-sha3'

// Tests 
console.log('test')
let test = ui.headline('text')

login()
loadData()


function login() { // script on load login in html!!
    // Check for Input
    document.getElementById('buttonLog').addEventListener('click', function () {
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
   /* let message = {
        SecurityCookie: 'cookie',
        QuestionID: 0
    }
    let answer = request.Get(adress, message)
    let aLength = answer.length
    console.log(answer)
    let i = 0
    while (i !== aLength) {
        let product = arr[i]
        product.split(',')
        let view = ui.view()
        let name = ui.headline(product[1])
        let price = ui.headline3(product[11] + '€')
        let text = ui.content('Calories: ' + product[3] + '\nProtein: ' + product[4] + '\nFat: ' + product[5] + '\nSodium: ' + product[6] + '\nFiber: ' + product[7] + '\nCarbo: ' + product[8] + '\nSugar: ' + product[9] + '\nVitamins: ' + product[10])
        let button = ui.button('See more')
        document.getElementById('grid').appendChild(view)
        document.querySelectorAll('artikel')[i].appendChild(name)
        document.querySelectorAll('artikel')[i].appendChild(price)
        document.querySelectorAll('artikel')[i].appendChild(text)
        document.querySelectorAll('artikel')[i].appendChild(button)
        document.querySelectorAll('button')[1].addEventListener('click', function () {
            let storage = ui.headline3('10x in Storage')  //muss natürlich noch individualisiert werden
            document.querySelectorAll('artikel')[1+i].appendChild(storage)
        })
        i++
    }
*/
    //tests
    var i = 0

   while( i != 20) {
        let view = ui.view()
        let name = ui.headline('headline')
        let price = ui.headline3('10€')
        let text = ui.content('Calories: 4 \nProtein: \nFat: 4 \nSodium:4 \nFiber: 4 \nCarbo: 44 \nSugar: 4 \nVitamins: 5')
        let buttonStorage = ui.button('in Store')
        let buttonReview = ui.button('See more')
        // sets ID for button 
        buttonStorage.id = 'button' + i
        buttonReview.id = 'RevButton' + i
        document.getElementById('grid').appendChild(view)
        document.querySelectorAll('artikel')[i].appendChild(name)
        document.querySelectorAll('artikel')[i].appendChild(price)
        document.querySelectorAll('artikel')[i].appendChild(text)
        document.querySelectorAll('artikel')[i].appendChild(buttonStorage)
        
        let e = i
        //let storage = ui.headline3('10x in Storage')
       // document.querySelectorAll('artikel')[0].appendChild(storage)
       let there = 0
       
        document.getElementById('button' + i).addEventListener('click', function () { // auslagern!
            if (there === 0) {
                let storage = ui.headline3('10x in Storage')
                console.log(document.querySelectorAll('artikel'))
                console.log(e)
                document.querySelectorAll('artikel')[e].appendChild(storage)
                there = 1
            }    
        })
        let is = 0
        document.querySelectorAll('artikel')[i].appendChild(buttonReview)
        document.getElementById('RevButton' + i).addEventListener('click', function () { // auslagern!
            if (is === 0) {
                let storage = ui.headline3('Rev')
                console.log(document.querySelectorAll('artikel'))
                console.log(e)
                document.querySelectorAll('artikel')[e].appendChild(storage)
                is = 1
            }    
        })

        i++
    }



    
    // Check for Cookie

    // if Cookie is there, load special Data

}