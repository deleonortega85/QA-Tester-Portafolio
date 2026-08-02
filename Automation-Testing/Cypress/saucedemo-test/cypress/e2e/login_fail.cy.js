/// <reference types="Cypress" />
import pantalla from "./selectores/pantalla"
//const pantalla = require("./selectores/pantalla");

describe('template spec', () => {

  var falloDatos;

  beforeEach('passes', () => {
    cy.visit('/');
    cy.fixture('./users_no').then(errarDatos => {
      falloDatos = errarDatos;
    });
  })

  it('passes', () => {
    falloDatos.forEach((reglon) => {
      cy.escribir(pantalla.login.usuario, reglon.usuario);
      cy.escribir(pantalla.login.clave, reglon.clave);
      cy.miClick(pantalla.login.btn_ingresar);
      cy.get(pantalla.login.sel_title).should('have.text', pantalla.login.msg_no);/*
      
      cy.get('#root > div > div.login_logo').should('have.text','Laboratorio') //aserción
   // este comando llama a el logout y a una aserción sobre el título encontrado en la web de respuesta
      */
    });
  })
})