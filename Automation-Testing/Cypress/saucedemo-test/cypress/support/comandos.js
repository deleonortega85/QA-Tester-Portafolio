Cypress.Commands.add('escribir', (selector, dato) => { 
   cy.get(selector).type(dato)
})

Cypress.Commands.add('miClick', (selector) => { 
   cy.get(selector).click()
})
