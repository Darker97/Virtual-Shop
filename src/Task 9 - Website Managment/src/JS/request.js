/**
   * Put-request to the given Link
   * @param {String} Link
   * @param {String} Message
   */
export function Post (Link, Message) {
  fetch(Link, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    Form: Message
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
    method: 'PUT',
    headers: { 'content-type': 'application/json' },
    Form: Message
  })
    .then(response => {
      console.log(response)
      return response
    })
    .catch(err => {
      console.log(err)
    })
}
