/// <reference types="Cypress" />
//import "cypress-real-events";
import pantalla from "./selectores/pantalla"

describe('template spec', () => {

  var misDatos;

  beforeEach('passes', () => {
    cy.visit('/')
    //cy.viewport(1100,900)
    cy.fixture('./users_ok').then(mis_test => {
       misDatos = mis_test;//lo que llega, lo cargo en misDatos
    }); //cuando llegan todos los datos.
  })

  it('passes', () => {
    misDatos.forEach((reglon) => { //obtengo un conjubnto de datos que me da json
      //cy.get(pantalla.login.usuario).type(reglon.usuario)
      cy.escribir(pantalla.login.usuario, reglon.usuario)
      //cy.get(pantalla.login.clave).type(reglon.clave)
      cy.escribir(pantalla.login.clave, reglon.clave)
      //cy.get(pantalla.login.btn_ingresar).click()	
      cy.miClick(pantalla.login.btn_ingresar)
      //menú abrir menú hamburguesa
      //cy.get(pantalla.menu.icon_burger).click()	
      cy.miClick(pantalla.menu.icon_burger)
      //cy.screenshot('imagen')
      //cy.get(pantalla.menu.btn_logout).click()	
      cy.miClick(pantalla.menu.btn_logout)
      cy.get(pantalla.login.sel_title).should('have.text', pantalla.login.msg_title) //aserción
      // este comando llama a el logout y a una aserción sobre el título encontrado en la web de respuesta
    });
  })

})