/**
 * returns a view of type artikel
 */
export function view () {
    const temp = document.createElement('artikel')
    return temp
  }
  
  /**
   * returns button with a name
   * @param {String} name
   */
  export function button (name) {
    const temp = document.createElement('button')
    temp.innerText = name
    return temp
  }
  
  /**
   * returns label with the text
   * @param {String} text
   */
  export function label (text) {
    const temp = document.createElement('p')
    temp.innerText = text
    return temp
  }
  /**
   * returns a headline2 with the text
   * @param {String} text
   */
  export function headline (text) {
    const temp = document.createElement('h2')
    temp.innerText = text
    return temp
  }
  /**
   * returns a headline3 with the text
   * @param {String} text
   */
  export function headline3 (text) {
    const temp = document.createElement('h3')
    temp.innerText = text
    return temp
  }
  
  /**
   * builds an Input
   * @param {String} name
   */
  export function input (name) {
    const temp = document.createElement('input')
    temp.type = 'text'
    temp.placeholder = name
    return temp
  }
  
  /**
   * inserts a line into your page
   */
  export function line () {
    const temp = document.createElement('hr')
    return temp
  }
  
  /**
   * footer
   */
  export function footer () {
    const temp = document.createElement('footer')
    temp.appendChild(headline('Made with 🖥 and ❤️'))
    temp.appendChild(label('Always Happy Coding'))
    return temp
  }