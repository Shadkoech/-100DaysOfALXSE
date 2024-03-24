const body = document.body
const div = document.querySelector("div")
const spanHi = document.querySelector('#hi')
const spanok = document.querySelector('#okay')

// Removing an element
spanHi.remove()
console.log(spanHi.getAttribute("id"))
console.log(spanHi.dataset.test)

// add new class under a given div
spanHi.classList.add("new-class")