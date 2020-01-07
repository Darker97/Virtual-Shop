/**
 * Does Everything that controlls the Website
 */
console.log('test')
console.log(document.getElementById('username1').innerText + ' yep')
login()
function login () {
  // Check for Input
  // let button = document.getElementsByTagName('button')
  document.getElementById('button1').addEventListener('click', loadInput) 
  
//   {
//     // loadInput()
//     let username = document.getElementById('username1').innerText
//     let password = document.getElementById('password1').innerText
//     console.log(username)
//     console.log('test2')
//     console.log(password)
//   })

  // Load Input
  function loadInput () {
    let username = document.getElementById('username1').value
    let password = document.getElementById('password1').value
    console.log(username)
    console.log(password)
  }

  // HASH Input with Library: https://github.com/emn178/js-sha3

  // send Request to API via API.js

  // Check answer

  // Save Answer as Cookie
}

function loadData (params) {

  // Load Data

  // Check for Cookie

  // if Cookie is there, load special Data

}
