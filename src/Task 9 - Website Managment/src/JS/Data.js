/**
 * Gets an Object and saves it with the ID
 * @param {INT} ID
 * @param {Object} Object
 */
export function save (ID, Object) {
  localStorage.setItem(ID, Object)
}

/**
   * loads the data behind the ID
   * @param {INT} ID
   */
export function load (ID) {
  return localStorage.getItem(ID)
}

/**
   * safe data for this seassion under the name
   * @param {String} ID
   * @param {Object} Object
   */
export function seassionSafe (ID, Object) {
  sessionStorage.setItem(ID, Object)
}

/**
   * Load the seassion safe with the name
   * @param {String} ID
   */
export function sassionLoad (ID) {
  return sessionStorage.getItem(ID)
}
