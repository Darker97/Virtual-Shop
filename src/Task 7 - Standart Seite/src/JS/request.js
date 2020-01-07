/**
   * Put-request to the given Link
   * @param {String} Link
   * @param {String} Message
   */
export function Put (Link, Message) {
  fetch(Link, {
    method: 'PUT',
    headers: { 'content-type': 'application/json' },
    body: Message
  })
    .then(response => {
      console.log(response)
      return response
    })
    .catch(err => {
      console.log(err)
    })
}

/**
   * Get-request to the given Link
   * @param {String} Link
   * @param {String} Message
   */
export function Get (Link, Message) {
  fetch(Link, {
    method: 'GET',
    headers: { 'content-type': 'application/json' },
    body: Message
  })
    .then(response => {
      console.log(response)
      return response
    })
    .catch(err => {
      console.log(err)
    })
}
