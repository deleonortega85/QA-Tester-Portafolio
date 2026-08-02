/// <reference types="Cypress" />
import pantalla from "./selectores/pantalla"
//const pantalla = require("./selectores/pantalla");

describe('template spec', () => {

  var bloqueo;

  beforeEach('passes', () => {
    cy.visit('/');
    cy.fixture('./users_blocked').then(bloque => {
      bloqueo = bloque;
    });
  })

  it('passes', () => {
    bloqueo.forEach((reglon) => {
      cy.escribir(pantalla.login.usuario, reglon.usuario);
      cy.escribir(pantalla.login.clave, reglon.clave);
      cy.miClick(pantalla.login.btn_ingresar);
      cy.get(pantalla.login.sel_title).should('have.text',pantalla.login.msg_locked); //aserción
    });
    // este comando llama a el logout y a una aserción sobre el título encontrado en la web de respuesta
  })
})